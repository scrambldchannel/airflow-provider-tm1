from unittest import mock

import pytest
from airflow.models.connection import Connection

from airflow_provider_tm1.hooks.tm1 import TM1Hook


@pytest.mark.mocked
def test_mock_connection(mock_connection_uri):

    with mock.patch.dict("os.environ", AIRFLOW_CONN_TM1_DEFAULT=mock_connection_uri):

        Connection.get_connection_from_secrets(conn_id="tm1_default")

        assert Connection.get_connection_from_secrets(conn_id="tm1_default").conn_type == "tm1"


def test_hook_init(mock_connection_uri):

    with mock.patch.dict("os.environ", AIRFLOW_CONN_TM1_DEFAULT=mock_connection_uri):

        Connection.get_connection_from_secrets(conn_id="tm1_default")

        tm1_hook = TM1Hook(tm1_conn_id="tm1_default")

        assert tm1_hook
