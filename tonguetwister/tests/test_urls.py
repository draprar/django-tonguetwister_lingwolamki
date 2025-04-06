import pytest
from django.urls import reverse, NoReverseMatch
from django.test import Client
from rest_framework.test import APIClient
from rest_framework import status

client = Client()

@pytest.fixture
def api_client():
    return APIClient()

# APIs from router
@pytest.mark.django_db
@pytest.mark.parametrize("endpoint", [
    '/api/oldpolish/',
    '/api/articulators/',
    '/api/funfacts/',
    '/api/exercises/',
    '/api/twisters/',
    '/api/trivias/',
])
def test_api_endpoint_is_accessible(api_client, endpoint):
    response = api_client.get(endpoint)
    assert response.status_code == status.HTTP_200_OK

# URLs without args
@pytest.mark.parametrize("url_name, expected_status", [
    ('main', 200),
    ('login', 200),
    ('logout', 302),
    ('register', 200),
    ('password_reset', 200),
    ('password_reset_done', 200),
    ('password_reset_complete', 200),
    ('password_reset_confirm', 200),
    ('load_more_articulators', 200),
    ('load_more_exercises', 200),
    ('load_more_twisters', 200),
    ('load_more_trivia', 200),
    ('load_more_funfacts', 200),
    ('load_more_old_polish', 200),
    ('articulator_list', 302),
    ('articulator_add', 302),
    ('exercise_list', 302),
    ('exercise_add', 302),
    ('twister_list', 302),
    ('twister_add', 302),
    ('trivia_list', 302),
    ('trivia_add', 302),
    ('funfact_list', 302),
    ('funfact_add', 302),
    ('oldpolish_list', 302),
    ('oldpolish_add', 302),
    ('user_content', 302),
    ('contact', 200),
    ('chatbot', 200),
])
def test_named_urls_no_args(url_name, expected_status):
    url = reverse(url_name)
    response = client.get(url)
    assert response.status_code == expected_status

# URLs with args (e.g. ID = 1)
@pytest.mark.parametrize("url_name, kwargs, expected_status", [
    ('articulator_edit', {'pk': 1}, 200),
    ('articulator_delete', {'pk': 1}, 200),
    ('exercise_edit', {'pk': 1}, 200),
    ('exercise_delete', {'pk': 1}, 200),
    ('twister_edit', {'pk': 1}, 200),
    ('twister_delete', {'pk': 1}, 200),
    ('trivia_edit', {'pk': 1}, 200),
    ('trivia_delete', {'pk': 1}, 200),
    ('funfact_edit', {'pk': 1}, 200),
    ('funfact_delete', {'pk': 1}, 200),
    ('oldpolish_edit', {'pk': 1}, 200),
    ('oldpolish_delete', {'pk': 1}, 200),
    ('add_articulator', {'articulator_id': 1}, 200),
    ('delete_articulator', {'articulator_id': 1}, 200),
    ('add_exercise', {'exercise_id': 1}, 200),
    ('delete_exercise', {'exercise_id': 1}, 200),
    ('add_twister', {'twister_id': 1}, 200),
    ('delete_twister', {'twister_id': 1}, 200),
])
def test_named_urls_with_args(url_name, kwargs, expected_status):
    try:
        url = reverse(url_name, kwargs=kwargs)
    except NoReverseMatch:
        url = url_name
    response = client.get(url)
    assert response.status_code in (expected_status, 302)
