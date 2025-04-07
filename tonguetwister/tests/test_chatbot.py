import pytest
from unittest.mock import patch
from django.urls import reverse
import wikipedia
from ..chatbot import chatbot_instance

@pytest.mark.django_db
@pytest.mark.asyncio
async def test_chatbot_view_with_keyword(async_client):
    response = await async_client.get(reverse("chatbot"), {"message": "rejestracja"})
    expected = chatbot_instance.get_response("rejestracja")
    assert response.status_code == 200
    assert response.json() == {"response": expected}


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_chatbot_view_empty(async_client):
    response = await async_client.get(reverse("chatbot"))
    assert response.status_code == 200
    assert response.json() == {"response": "Nie rozumiem."}

@pytest.mark.parametrize("text", ["hej", "cześć", "witaj", "siema"])
def test_greeting_detection(text):
    response = chatbot_instance.get_response(text)
    assert any(word in response.lower() for word in ["cześć", "hej", "witaj"])


def test_positive_sentiment():
    response = chatbot_instance.get_response("super fajnie świetnie")
    assert "pozytywne" in response.lower()


def test_negative_sentiment():
    response = chatbot_instance.get_response("okropnie źle tragicznie")
    assert "przykro" in response.lower()


def test_fallback_for_noise():
    response = chatbot_instance.get_response("???!!!...")
    assert "nie zrozumiałem" in response.lower()


@patch("tonguetwister.chatbot.wikipedia.summary")
def test_wikipedia_lookup_success(mock_summary):
    mock_summary.return_value = "To jest testowa odpowiedź z Wikipedii."
    response = chatbot_instance.get_response("co to jest Python?")
    assert "testowa odpowiedź" in response.lower()


@patch("tonguetwister.chatbot.wikipedia.summary", side_effect=wikipedia.exceptions.PageError("Test"))
def test_wikipedia_page_error(_):
    response = chatbot_instance.get_response("co to jest asdfghjk?")
    assert "nie znalazłem dokładnej informacji" in response.lower()


def test_unhandled_question_fallback():
    response = chatbot_instance.get_response("lalalalala")
    assert "jak mogę pomóc" in response.lower() or "dziękuję za wiadomość" in response.lower()


@patch("tonguetwister.chatbot.sentry_sdk.capture_exception")
def test_general_exception(mock_sentry):
    # Symulujemy wyjątek w czasie działania get_response
    with patch("tonguetwister.chatbot.Chatbot.get_custom_sentiment", side_effect=Exception("Boom")):
        response = chatbot_instance.get_response("coś powoduje wyjątek")
        mock_sentry.assert_called_once()
        assert "wystąpił błąd" in response.lower()
