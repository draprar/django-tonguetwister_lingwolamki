import pytest
from django.core import mail
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import AsyncClient, Client
from tonguetwister.models import Twister, Articulator, Exercise, Trivia, Funfact, OldPolish, UserProfileTwister, UserProfileArticulator, UserProfileExercise
from tonguetwister.views import chatbot_instance
from tonguetwister.forms import ContactForm


@pytest.mark.django_db
class TestMainViews:
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
class TestContentManagementViews:

    @pytest.fixture
    def admin_user(self):
        return User.objects.create_superuser(username='adminuser', password='adminpassword', email='admin@example.com', is_staff=True)

    @pytest.fixture
    def regular_user(self):
        return User.objects.create_user(username='user', password='userpassword', email='user@example.com')

    def test_content_management_unauthenticated(self, client):
        url = reverse('content_management')
        response = client.get(url)

        assert response.status_code == 302

    def test_content_management_user(self, client, regular_user):
        client.login(username='user', password='userpassword')
        url = reverse('content_management')
        response = client.get(url)

        assert response.status_code == 302

    def test_content_management_admin(self, client, admin_user):
        client.force_login(admin_user)
        url = reverse('content_management')
        response = client.get(url)

        assert response.status_code == 200
        assert 'admin/settings.html' in [t.name for t in response.templates]

    @pytest.fixture(params=[
        ('articulator_list', 'articulator_add', 'articulator_edit', 'articulator_delete', Articulator),
        ('exercise_list', 'exercise_add', 'exercise_edit', 'exercise_delete', Exercise),
        ('twister_list', 'twister_add', 'twister_edit', 'twister_delete', Twister),
        ('trivia_list', 'trivia_add', 'trivia_edit', 'trivia_delete', Trivia),
        ('funfact_list', 'funfact_add', 'funfact_edit', 'funfact_delete', Funfact),
        ('oldpolish_list', 'oldpolish_add', 'oldpolish_edit', 'oldpolish_delete', OldPolish),
    ])
    def model_data(self, request):
        return request.param

    def test_list_view(self, client, model_data):
        list_url = reverse(model_data[0])
        response = client.get(list_url)

        assert response.status_code == 302

    def test_list_view_user(self, client, regular_user, model_data):
        client.login(username='user', password='userpassword')
        list_user_url = reverse(model_data[0])
        response = client.get(list_user_url)

        assert response.status_code == 302

    def test_list_view_admin(self, client, admin_user, model_data):
        client.force_login(admin_user)
        list_admin_url = reverse(model_data[0])
        response = client.get(list_admin_url)

        assert response.status_code == 200

    def test_add_view(self, client, admin_user, model_data):
        client.force_login(admin_user)
        add_url = reverse(model_data[1])
        if model_data[1] == 'oldpolish_add':
            form_data = {'old_text': 'old_text', 'new_text': 'new_text'}
        else:
            form_data = {'text': 'test'}
        response = client.post(add_url, data=form_data)

        assert response.status_code == 302

    def test_edit_view(self, client, admin_user, model_data):
        client.force_login(admin_user)
        if model_data[2] == 'oldpolish_edit':
            model_instance = model_data[4].objects.create(old_text='old_text', new_text='new_text')
        else:
            model_instance = model_data[4].objects.create(text='test')
        edit_url = reverse(model_data[2], args=[model_instance.pk])
        if model_data[2] == 'oldpolish_edit':
            form_data = {'old_text': 'new_old_text', 'new_text': 'new_new_text'}
        else:
            form_data = {'text': 'new_test'}
        response = client.post(edit_url, data=form_data)

        assert response.status_code == 302

    def test_delete_view(self, client, admin_user, model_data):
        client.force_login(admin_user)
        if model_data[3] == 'oldpolish_delete':
            model_instance = model_data[4].objects.create(old_text='old_text', new_text='new_text')
        else:
            model_instance = model_data[4].objects.create(text='test')
        delete_url = reverse(model_data[3], args=[model_instance.pk])
        response = client.post(delete_url)

        assert response.status_code == 302
        assert not model_data[4].objects.filter(pk=model_instance.pk).exists()


@pytest.mark.django_db
class TestErrorViews:
    def test_error_404_view(self, client, settings):
        response = client.get('/non-existing-url/')

        assert 'tonguetwister/404.html' in [t.name for t in response.templates]


@pytest.mark.django_db
class TestContactViews:
    @pytest.fixture
    def url(self):
        return reverse('contact')

    @pytest.fixture
    def valid_form_data(self):
        return {
            'name': 'testuser',
            'email': 'test@example.com',
            'message': 'Test Message'
        }

    def test_contact_get_request(self, client, url):
        response = client.get(url)

        assert response.status_code == 200
        assert 'tonguetwister/partials/static/contact.html' in [t.name for t in response.templates]
        assert isinstance(response.context['form'], ContactForm)

    def test_contact_post_valid(self, client, url, valid_form_data):
        response = client.post(url, data=valid_form_data)

        assert response.status_code == 302
        assert response.url == url

        messages = list(get_messages(response.wsgi_request))
        assert str(messages[0]) == 'Twoja wiadomość została Nam przekazana'

        assert len(mail.outbox) == 1
        sent_email = mail.outbox[0]
        assert sent_email.subject == f'Kontakt od {valid_form_data["name"]}'
        assert sent_email.body == f"Od: {valid_form_data['email']}\n\n{valid_form_data['message']}"

    def test_contact_post_invalid(self, client, url):
        invalid_data = {
            'name': '',
            'email': 'invalid email',
            'message': ''
        }
        response = client.post(url, data=invalid_data)

        assert response.status_code == 200
        assert isinstance(response.context['form'], ContactForm)
        assert response.context['form'].is_valid() is False

    def test_contact_post_email_error(self, mocker, client, url, valid_form_data):
        mock_send_mail = mocker.patch('tonguetwister.views.send_mail', side_effect=Exception('Email error'))
        response = client.post(url, data=valid_form_data)

        assert response.status_code == 302
        assert response.url == url

        messages = list(get_messages(response.wsgi_request))
        assert str(messages[0]) == 'Błąd przy wysyłaniu wiadomości: Email error'
        assert len(mail.outbox) == 0
