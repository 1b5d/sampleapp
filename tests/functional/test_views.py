from http import HTTPStatus
import pytest


@pytest.mark.django_db
def test_home(client, django_db_setup):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK.value


@pytest.mark.parametrize('name', [
    'Demo Site',
    'ABC Site',
    'XYZ Site'
])
@pytest.mark.django_db
def test_sites(name, client, django_db_setup):
    response = client.get('/sites/')

    assert response.status_code == HTTPStatus.OK.value
    assert name in response.content.decode('utf8')


@pytest.mark.parametrize('site_id,a_value,b_value', [
    (1, '12.00', '16.00'),
    (1, '20.00', '100.00'),
    (1, '20.00', '80.00'),
    (2, '5.00', '15.00'),
    (3, '5.00', '15.00'),
    (3, '5.00', '15.00'),
])
@pytest.mark.django_db
def test_site(site_id, a_value, b_value, client, django_db_setup):
    response = client.get('/sites/{site_id}/'.format(site_id=site_id))

    assert response.status_code == HTTPStatus.OK.value
    assert a_value in response.content.decode('utf8')
    assert b_value in response.content.decode('utf8')


@pytest.mark.parametrize('a_value,b_value', [
    ('52.00', '196.00'),
    ('5.00', '15.00'),
    ('10.00', '30.00'),
])
@pytest.mark.django_db
def test_sum(a_value, b_value, client, django_db_setup):
    response = client.get('/summary/')

    assert response.status_code == HTTPStatus.OK.value
    assert a_value in response.content.decode('utf8')
    assert b_value in response.content.decode('utf8')


@pytest.mark.parametrize('a_value,b_value', [
    ('17.33', '65.33'),
    ('5.00', '15.00'),
    ('5.00', '15.00'),
])
@pytest.mark.django_db
def test_sum(a_value, b_value, client, django_db_setup):
    response = client.get('/summary-average/')

    assert response.status_code == HTTPStatus.OK.value
    assert a_value in response.content.decode('utf8')
    assert b_value in response.content.decode('utf8')
