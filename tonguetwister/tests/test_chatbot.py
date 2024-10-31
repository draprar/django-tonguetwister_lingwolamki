import pytest
from django.urls import reverse
from django.http import JsonResponse
from tonguetwister.views import chatbot_instance
from django.test import AsyncClient


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_chatbot_view_with_message():
    # Test chatbot response to a specific message
    client = AsyncClient()

    response = await client.get(reverse('chatbot'), {'message': 'rejestracja'})

    assert response.status_code == 200
    assert isinstance(response, JsonResponse)

    expected_response = chatbot_instance.get_response('rejestracja')
    assert response.json() == {'response': expected_response}


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_chatbot_view_without_message():
    # Test chatbot default response when no message is provided
    client = AsyncClient()

    response = await client.get(reverse('chatbot'))

    assert response.status_code == 200
    assert isinstance(response, JsonResponse)
    assert response.json() == {'response': 'Nie rozumiem.'}
