import pytest
from django.test import AsyncClient
from django.conf import settings


@pytest.fixture
def async_client():
    """Fixture providing an async test client."""
    return AsyncClient()


@pytest.fixture(autouse=True)
def use_locmem_email_backend(settings):
    """Use local memory email backend for tests."""
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"








