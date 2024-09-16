import pytest
from django.urls import reverse


@pytest.mark.parametrize("url_name, expected_status", [
    ('main', 200),
    ('login', 200),
    ('logout', 302),
    ('register', 200),
    ('activate', 200),
    ('password_reset', 200),
    ('password_reset_done', 200),
    ('password_reset_confirm', 200),
    ('password_reset_complete', 200),
    ('load_more_articulators', 200),
    ('load_more_exercises', 200),
    ('load_more_twisters', 200),
    ('load_more_trivia', 200),
    ('load_more_funfacts', 200),
    ('load_more_old_polish', 200),
    ('articulator_list', 302),
    ('articulator_add', 302),
    ('articulator_edit', 200),
    ('articulator_delete', 200),
    ('exercise_list', 302),
    ('exercise_add', 302),
    ('exercise_edit', 200),
    ('exercise_delete', 200),
    ('twister_list', 302),
    ('twister_add', 302),
    ('twister_edit', 200),
    ('twister_delete', 200),
    ('trivia_list', 302),
    ('trivia_add', 302),
    ('trivia_edit', 200),
    ('trivia_delete', 200),
    ('funfact_list', 302),
    ('funfact_add', 302),
    ('funfact_edit', 200),
    ('funfact_delete', 200),
    ('oldpolish_list', 302),
    ('oldpolish_add', 302),
    ('oldpolish_edit', 200),
    ('oldpolish_delete', 200),
    ('user_content', 302),
    ('add_articulator', 200),
    ('delete_articulator', 200),
    ('add_exercise', 200),
    ('delete_exercise', 200),
    ('add_twister', 200),
    ('delete_twister', 200),
    ('contact', 200),
    ('chatbot', 200),
])
@pytest.mark.django_db
def test_urls(client, url_name, expected_status):
    try:
        url = reverse(url_name)
    except:
        url = url_name
    response = client.get(url)
    assert response.status_code == expected_status
