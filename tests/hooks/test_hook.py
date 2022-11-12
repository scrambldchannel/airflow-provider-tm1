from airflow_provider_tm1.hooks.tm1 import TM1Hook

from unittest import mock

from airflow.models.connection import Connection

def test_mock_connection(mock_connection_uri):

    with mock.patch.dict("os.environ", AIRFLOW_CONN_TM1_DEFAULT=mock_connection_uri):
        
        Connection.get_connection_from_secrets(conn_id="tm1_default")

        assert Connection.get_connection_from_secrets(conn_id="tm1_default").conn_type == "tm1"


def test_hook_init(mock_connection_uri):

    with mock.patch.dict("os.environ", AIRFLOW_CONN_TM1_DEFAULT=mock_connection_uri):
        
        Connection.get_connection_from_secrets(conn_id="tm1_default")

        assert TM1Hook(tm1_conn_id="tm1_default")
