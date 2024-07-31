from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_return_ok_and_helloWord():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    # assert (garanta que o status code da resposta é igual a ok)
    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'message': 'Olá mundo'}
