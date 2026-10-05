from http import HTTPStatus

from fastapi_zero.shemas import UserPublic


def test_root_deve_retornar_ola_mundo(client):

    response = client.get('/')

    assert response.json() == {'message': 'Olá, Mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Will',
            'password': '123456',
            'email': 'willtest@gmail.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'willtest@gmail.com',
        'username': 'Will',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'joalisson',
            'password': '2504',
            'email': 'joalisson@gmail.com',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'joalisson',
        'email': 'joalisson@gmail.com',
    }


def test_update_user_NOT_FOUND(
    client,
):
    response = client.put(
        '/users/3',
        json={
            'username': 'test',
            'password': 'testNOTFOUND',
            'email': 'testNOTFOUND@gmail.com',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_integrity_error(client, user):
    client.post(
        '/users',
        json={
            'username': 'fausto',
            'email': 'fausto@example.com',
            'password': 'secret',
        },
    )
    response = client.put(
        f'/users/{user.id}',
        json={
            'username': 'fausto',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Username or Email already exists'}


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_NOT_FOUND(client):
    response = client.delete(
        '/users/4',
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
