import pytest
from django.urls import reverse, NoReverseMatch


@pytest.mark.parametrize("url_name, expected_status", [
    # Test for URLs with expected HTTP status codes
    ('main', 200),  # home page
    ('login', 200),  # login page
    ('logout', 302),  # logout (redirects)
    ('register', 200),  # registration page
    ('activate', 200),  # account activation
    ('password_reset', 200),  # password reset form
    ('password_reset_done', 200),  # password reset confirmation
    ('password_reset_confirm', 200),  # password reset confirmation step
    ('password_reset_complete', 200),  # password reset complete
    ('load_more_articulators', 200),  # load more articulators
    ('load_more_exercises', 200),  # load more exercises
    ('load_more_twisters', 200),  # load more twisters
    ('load_more_trivia', 200),  # load more trivia items
    ('load_more_funfacts', 200),  # load more fun facts
    ('load_more_old_polish', 200),  # load more Old Polish texts
    ('articulator_list', 302),  # articulator list (requires login)
    ('articulator_add', 302),  # add articulator (requires login)
    ('articulator_edit', 200),  # edit articulator
    ('articulator_delete', 200),  # delete articulator
    ('exercise_list', 302),  # exercise list (requires login)
    ('exercise_add', 302),  # add exercise (requires login)
    ('exercise_edit', 200),  # edit exercise
    ('exercise_delete', 200),  # delete exercise
    ('twister_list', 302),  # twister list (requires login)
    ('twister_add', 302),  # add twister (requires login)
    ('twister_edit', 200),  # edit twister
    ('twister_delete', 200),  # delete twister
    ('trivia_list', 302),  # trivia list (requires login)
    ('trivia_add', 302),  # add trivia (requires login)
    ('trivia_edit', 200),  # edit trivia
    ('trivia_delete', 200),  # delete trivia
    ('funfact_list', 302),  # fun fact list (requires login)
    ('funfact_add', 302),  # add fun fact (requires login)
    ('funfact_edit', 200),  # edit fun fact
    ('funfact_delete', 200),  # delete fun fact
    ('oldpolish_list', 302),  # old Polish list (requires login)
    ('oldpolish_add', 302),  # add Old Polish (requires login)
    ('oldpolish_edit', 200),  # edit Old Polish
    ('oldpolish_delete', 200),  # delete Old Polish
    ('user_content', 302),  # user content (requires login)
    ('add_articulator', 200),  # add articulator (additional)
    ('delete_articulator', 200),  # delete articulator (additional)
    ('add_exercise', 200),  # add exercise (additional)
    ('delete_exercise', 200),  # delete exercise (additional)
    ('add_twister', 200),  # add twister (additional)
    ('delete_twister', 200),  # delete twister (additional)
    ('contact', 200),  # contact page
    ('chatbot', 200),  # chatbot page
])
@pytest.mark.django_db
def test_urls(client, url_name, expected_status):
    # Test URL response codes, handling reverse URL lookup where possible
    try:
        url = reverse(url_name)
    except NoReverseMatch:
        url = url_name
    response = client.get(url)
    assert response.status_code == expected_status
