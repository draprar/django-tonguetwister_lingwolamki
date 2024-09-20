import pytest
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from tonguetwister.models import Twister, Articulator, Exercise, Trivia, Funfact, OldPolish, UserProfileTwister, UserProfileArticulator, UserProfileExercise
from tonguetwister.views import chatbot_instance
from django.test import AsyncClient


@pytest.mark.django_db
class TestMainView:
    def test_main_unauthenticated(self, client):
        url = reverse('main')
        response = client.get(url)

        assert response.status_code == 200
        assert 'tonguetwister/main.html' in [t.name for t in response.templates]

        assert 'twisters' in response.context
        assert 'twisters' in response.context
        assert 'articulators' in response.context
        assert 'exercises' in response.context
        assert 'trivia' in response.context
        assert 'funfacts' in response.context
        assert 'old_polish_texts' in response.context

        assert 'user_twisters_texts' not in response.context
        assert 'user_articulators_texts' not in response.context
        assert 'user_exercises_texts' not in response.context

    def test_main_authenticated(self, client, django_user_model):
        user = django_user_model.objects.create_user(username='testuser', password='password')
        client.login(username=user.username, password='password')
        url = reverse('main')
        response = client.get(url)

        assert response.status_code == 200
        assert 'tonguetwister/main.html' in [t.name for t in response.templates]

        assert 'twisters' in response.context
        assert 'twisters' in response.context
        assert 'articulators' in response.context
        assert 'exercises' in response.context
        assert 'trivia' in response.context
        assert 'funfacts' in response.context
        assert 'old_polish_texts' in response.context
        assert 'user_twisters_texts' in response.context
        assert 'user_articulators_texts' in response.context
        assert 'user_exercises_texts' in response.context

    def test_main_view_internal_server_error(self, client, mocker):
        url = reverse('main')
        mocker.patch('tonguetwister.views.Twister.objects.all', side_effect=Exception("Test Exception"))
        response = client.get(url)

        assert response.status_code == 500
        assert "Internal Server Error" in response.content.decode()


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_chatbot_view_with_message():
    client = AsyncClient()

    response = await client.get(reverse('chatbot'), {'message': 'rejestracja'})

    assert response.status_code == 200
    assert isinstance(response, JsonResponse)

    expected_response = chatbot_instance.get_response('rejestracja')
    assert response.json() == {'response': expected_response}


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_chatbot_view_without_message():
    client = AsyncClient()

    response = await client.get(reverse('chatbot'))

    assert response.status_code == 200
    assert isinstance(response, JsonResponse)
    assert response.json() == {'response': 'Nie rozumiem.'}
