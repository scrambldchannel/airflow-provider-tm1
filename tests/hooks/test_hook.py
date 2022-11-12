from airflow_provider_tm1.hooks.tm1 import TM1Hook


def test_hook_init():

    hook = TM1Hook()

    assert hook
