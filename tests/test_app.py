from http import HTTPStatus


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
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'Will',
                'email': 'willtest@gmail.com',
            }
        ]
    }


def test_update_user(client):
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


def test_update_user_NOT_FOUND(client):
    response = client.put(
        '/users/3',
        json={
            'username': 'test',
            'password': 'testNOTFOUND',
            'email': 'testNOTFOUND@gmail.com',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'joalisson',
        'email': 'joalisson@gmail.com',
    }


def test_delete_user_NOT_FOUND(client):
    response = client.delete(
        '/users/4',
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
