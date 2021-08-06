from main import hello


def test_hello_route():
    response = hello()
    assert response is not None
