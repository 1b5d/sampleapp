from http import HTTPStatus
import pytest


@pytest.mark.django_db
def test_home(client, django_db_setup):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK.value
