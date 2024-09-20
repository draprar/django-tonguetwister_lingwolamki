import pytest
from tonguetwister.chatbot import Chatbot


@pytest.fixture
def chatbot():
    return Chatbot()


def test_chatbot_keyword_response(chatbot):
    respone = chatbot.get_response('rejestracja')
    assert respone == "Aby się zarejestrować, kliknij przycisk 'Logowanie'. Zarejestruj się już teraz, aby korzystać z pełni funkcji naszej aplikacji!"


def test_chatbot_positive_response(chatbot):
    response = chatbot.get_response('super')
    assert response == "Cieszę się, że masz pozytywne nastawienie! Jak mogę Ci jeszcze pomóc?"


def test_chatbot_negative_response(chatbot):
    response = chatbot.get_response('okropne')
    assert response == "Przykro mi, że masz negatywne odczucia. Może mogę jakoś pomóc?"


def test_chatbot_neutral_or_unrecognized_response(chatbot):
    response = chatbot.get_response('czemu')
    assert response == "Dziękuję za wiadomość. Jak mogę pomóc?"
