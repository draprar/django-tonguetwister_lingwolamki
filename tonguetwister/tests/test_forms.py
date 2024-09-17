import pytest
import os
from django.contrib.auth.models import User, Group
from django.core.files.uploadedfile import SimpleUploadedFile
from tonguetwister.forms import CustomUserCreationForm, LoginForm, ContactForm, AvatarUploadForm
from tonguetwister.models import Profile


@pytest.mark.django_db
def test_custom_creation_form_valid_data():
    group = Group.objects.create(name='Regular Users')
    form_data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password1': 'StrongPassword!123',
        'password2': 'StrongPassword!123',
    }
    form = CustomUserCreationForm(data=form_data)
    assert form.is_valid()
    user = form.save()
    assert user.groups.filter(name='Regular Users').exists()


@pytest.mark.django_db
@pytest.mark.parametrize("data, error_field", [
    # Password too weak
    ({
        'username': 'testuser',
        'email': 'test@example.com',
        'password1': 'password',
        'password2': 'password',
    }, 'password1'),
    # Different passwords
    ({
        'username': 'testuser',
        'email': 'test@example.com',
        'password1': 'password123!Q',
        'password2': 'different_password123!Q',
    }, 'password2'),
    # Existing username
    ({
        'username': 'newuser',
        'email': 'new_test@example.com',
        'password1': 'password123!Q',
        'password2': 'password123!Q',
    }, 'username'),
    # Existing email
    ({
        'username': 'testuser',
        'email': 'test@example.com',
        'password1': 'password123!Q',
        'password2': 'password123!Q'
    }, 'email')
])
def test_custom_creation_form_cases(data, error_field):
    if data['username'] == 'testuser':
        User.objects.create(username='testuser', email='test@example.com')
    if data['username'] == 'newuser':
        User.objects.create(username='newuser', email='test@example.com')
    if data['username'] != 'testuser' and data['email'] == 'test@example.com':
        User.objects.create(username='otheruser', email='test@example.com')

    form = CustomUserCreationForm(data=data)

    assert not form.is_valid()
    assert error_field in form.errors


@pytest.mark.django_db
def test_login_form_valid_data():
    data = {'username': 'testuser', 'password': 'passwork123!Q'}
    form = LoginForm(data=data)
    assert form.is_valid()


@pytest.mark.django_db
def test_login_form_invalid_data():
    data = {'username': 'testuser'}
    form = LoginForm(data=data)
    assert not form.is_valid()
    assert 'password' in form.errors


@pytest.mark.django_db
def test_contact_form_valid_data():
    data = {
        'name': 'test_name',
        'email': 'test@example.com',
        'message': 'test_text',
    }
    form = ContactForm(data=data)
    assert form.is_valid()


@pytest.mark.django_db
def test_contact_form_invalid_data():
    data = {'username': 'testuser', 'message': 'test_text'}
    form = ContactForm(data=data)
    assert not form.is_valid()
    assert 'email' in form.errors


@pytest.mark.django_db
@pytest.mark.parametrize("file, is_valid, error", [
    # Valid image file
    (SimpleUploadedFile("avatar.png", open(os.path.join(os.path.dirname(__file__), 'test.png'), 'rb').read(), content_type="image/png"), True, None),
    # Invalid image type
    (SimpleUploadedFile("avatar.txt", b"file_content", content_type="text/plain"), False, 'avatar'),
    # Invalid image size
    (SimpleUploadedFile("avatar.png", b"x" * 2 * 1024 * 1024 + b"x", content_type="image/png"), False, 'avatar'),
    # No file upload
    (None, False, 'avatar')
])
def test_avatar_upload_form(file, is_valid, error):
    data = {'avatar': file} if file else {}
    form = AvatarUploadForm(data={}, files=data)

    print(form.errors)
    assert form.is_valid() == is_valid

    if not is_valid:
        assert error in form.errors
