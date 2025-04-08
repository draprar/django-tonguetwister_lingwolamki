import pytest
from rest_framework.test import APIClient
from ..models import (
    OldPolish, Articulator, Twister, Exercise, Trivia, Funfact
)
from ..serializers import (
    OldPolishSerializer, ArticulatorSerializer, TwisterSerializer,
    ExerciseSerializer, TriviaSerializer, FunfactSerializer
)
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def auth_client():
    user = User.objects.create_user(username="testuser", password="pass123")
    token = RefreshToken.for_user(user).access_token
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return client

# ---------- OLD POLISH ----------
@pytest.mark.django_db
def test_oldpolish_list_success(api_client):
    obj = OldPolish.objects.create(old_text="ćwiczenie", new_text="ćwiczenie")
    response = api_client.get('/api/oldpolish/')
    assert response.status_code == 200
    assert response.data == OldPolishSerializer([obj], many=True).data

@pytest.mark.django_db
def test_oldpolish_list_not_found(api_client):
    response = api_client.get('/api/oldpolish/?search=xyz')
    assert response.status_code == 404

# ---------- ARTICULATORS ----------
@pytest.mark.django_db
def test_articulator_list_success(api_client):
    obj = Articulator.objects.create(text="Szczebrzeszyn")
    response = api_client.get('/api/articulators/')
    assert response.status_code == 200
    assert response.data == ArticulatorSerializer([obj], many=True).data

@pytest.mark.django_db
def test_articulator_list_not_found(api_client):
    response = api_client.get('/api/articulators/?search=nieistnieje')
    assert response.status_code == 404

# ---------- TWISTERS ----------
@pytest.mark.django_db
def test_twister_list_success(api_client):
    obj = Twister.objects.create(text="Król Karol kupił królowej Karolinie korale")
    response = api_client.get('/api/twisters/')
    assert response.status_code == 200
    assert response.data == TwisterSerializer([obj], many=True).data

@pytest.mark.django_db
def test_twister_list_not_found(api_client):
    response = api_client.get('/api/twisters/?search=xyz')
    assert response.status_code == 404

# ---------- EXERCISES ----------
@pytest.mark.django_db
def test_exercise_list_success(api_client):
    obj = Exercise.objects.create(text="Ćwicz: szosa, susza")
    response = api_client.get('/api/exercises/')
    assert response.status_code == 200
    assert response.data == ExerciseSerializer([obj], many=True).data

@pytest.mark.django_db
def test_exercise_list_not_found(api_client):
    response = api_client.get('/api/exercises/?search=xyz')
    assert response.status_code == 404

# ---------- TRIVIAS ----------
@pytest.mark.django_db
def test_trivia_list_success(api_client):
    obj = Trivia.objects.create(text="Polski alfabet ma 32 litery")
    response = api_client.get('/api/trivias/')
    assert response.status_code == 200
    assert response.data == TriviaSerializer([obj], many=True).data

@pytest.mark.django_db
def test_trivia_list_not_found(api_client):
    response = api_client.get('/api/trivias/?search=xyz')
    assert response.status_code == 404

# ---------- FUNFACTS (JWT protected) ----------
@pytest.mark.django_db
def test_funfact_list_success(auth_client):
    obj = Funfact.objects.create(text="W polskim są nosówki.")
    response = auth_client.get('/api/funfacts/')
    assert response.status_code == 200
    assert response.data == FunfactSerializer([obj], many=True).data

@pytest.mark.django_db
def test_funfact_list_unauthorized(api_client):
    response = api_client.get('/api/funfacts/')
    assert response.status_code == 401

@pytest.mark.django_db
def test_funfact_list_not_found(auth_client):
    response = auth_client.get('/api/funfacts/?search=xyz')
    assert response.status_code == 404

# ---------- AUTH (token obtain) ----------
@pytest.mark.django_db
def test_token_obtain_success(api_client):
    User.objects.create_user(username="testuser", password="pass123")
    response = api_client.post('/api/token/', data={"username": "testuser", "password": "pass123"})
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data

@pytest.mark.django_db
def test_token_obtain_fail(api_client):
    response = api_client.post('/api/token/', data={"username": "wrong", "password": "wrong"})
    assert response.status_code == 401
