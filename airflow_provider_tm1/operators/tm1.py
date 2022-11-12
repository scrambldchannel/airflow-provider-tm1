from typing import Optional

from airflow.models import BaseOperator

from airflow_provider_tm1.hooks.tm1 import TM1Hook


class TM1CheckPulseOperator(BaseOperator):
    def __init__(
        self,
        process_name: str,
        tm1_conn_id: str = "tm1_default",
        parameters: Optional[dict] = None,
        *args,
        **kwargs,
    ) -> None:

        super().__init__(*args, **kwargs)

        self.tm1_conn_id = tm1_conn_id
        self.process_name = process_name
        self.parameters = parameters

    def execute(self, context: dict) -> None:
        tm1_hook = TM1Hook(tm1_conn_id=self.tm1_conn_id)

        tm1 = tm1_hook.get_conn()

        if not tm1.processes.exists(self.process_name):
            raise Exception(f"Process {self.process_name} not found on TM1 server {tm1_hook.db}.")
        else:
            print(
                f"Process {self.process_name} executed on TM1 server {tm1_hook.db} with parameters {self.parameters}."
            )
            tm1.processes.execute(self.process_name, **self.parameters)


class TM1RunTIOperator(BaseOperator):
    """
    This operator runs a TI process

    :param process_name: The TI process to run.
    :type process_name: str
    :param tm1_conn_id: The Airflow connection used for TM1 credentials.
    :type tm1_conn_id: str
    """

    def __init__(
        self,
        process_name: str,
        tm1_conn_id: str = "tm1_default",
        parameters: Optional[dict] = None,
        *args,
        **kwargs,
    ) -> None:

        super().__init__(*args, **kwargs)

        self.tm1_conn_id = tm1_conn_id
        self.process_name = process_name
        self.parameters = parameters

    def execute(self, context: dict) -> None:
        tm1_hook = TM1Hook(tm1_conn_id=self.tm1_conn_id)

        tm1 = tm1_hook.get_conn()

        if not tm1.processes.exists(self.process_name):
            raise Exception(f"Process {self.process_name} not found on TM1 server {tm1_hook.db}.")
        else:
            print(
                f"Process {self.process_name} executed on TM1 server {tm1_hook.db} with parameters {self.parameters}."
            )
            tm1.processes.execute(self.process_name, **self.parameters)


class TM1RunChoreOperator(BaseOperator):
    """
    This operator runs a chore

    :param chore_name: The TI process to run.
    :type chore_name: str
    :param tm1_conn_id: The Airflow connection used for TM1 credentials.
    :type tm1_conn_id: str
    """

    def __init__(self, chore_name: str, tm1_conn_id: str = "tm1_default", *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

        self.tm1_conn_id = tm1_conn_id
        self.chore_name = chore_name

    def execute(self, context: dict) -> None:
        tm1_hook = TM1Hook(tm1_conn_id=self.tm1_conn_id)

        tm1 = tm1_hook.get_conn()

        if not tm1.chores.exists(self.chore_name):
            raise Exception(f"Chore {self.chore_name} not found on TM1 server {tm1_hook.db}.")
        else:
            print(f"Chore {self.chore_name} executed on TM1 server {tm1_hook.db}.")
            tm1.chores.execute(self.chore_name)
