from airflow.models.connection import Connection
from TM1py.Services.RestService import RestService

import pytest

from unittest import mock

@pytest.fixture(scope="module")
def mock_connection_uri():

    conn = Connection(
        conn_id="tm1_default",
        conn_type="tm1",
        host="tm1",
        login="admin",
        password="apple",
        port=8080,
        extra={
            'ssl': True,
        },
    )

    conn_uri = conn.get_uri()
    
    return conn_uri


# @pytest.fixture(scope="function")
# def mock_rest_service(module_mocker):
#     """
#     Simple mock of TM1py's low level rest service
#     """

#     # These were necessary to get this working
#     module_mocker.patch.object(RestService, "_start_session", return_value=True)
#     module_mocker.patch.object(RestService, "set_version", return_value="testing version")

#     # It probably makes senese to mock other things like this
#     module_mocker.patch.object(RestService, "is_connected", return_value=None)

#     # set some necessary kwargs
#     mock_args = {"address": "localhost", "port": 8080}

#     return RestService(**mock_args)


# # @pytest.fixture(scope="module")
# # def mock_dim_service(module_mocker, mock_rest_service, dims_all):
# #     """
# #     Simple mock of TM1py's dimension service
# #     """

# #     # weird thing here where I find I need to add a param to the function
# #     # should I be passing some sort of mock thing?
# #     def get_all_names(none):
# #         return [d.name for d in dims_all]

# #     module_mocker.patch.object(DimensionService, "get_all_names", new=get_all_names)

# #     return DimensionService(mock_rest_service)
