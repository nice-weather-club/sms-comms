from src.db_conn import connect


def test_connection():
    """
    GIVEN credentials exist in .env
    WHEN the connect() func is run
    THEN check a connection exists
    """
    resp = connect()
    assert resp is not None
