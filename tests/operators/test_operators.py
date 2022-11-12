from airflow_provider_tm1.operators.tm1 import (
    TM1CheckPulseOperator,
    TM1RunChoreOperator,
    TM1RunTIOperator,
)


def test_check_pulse():

    op = TM1CheckPulseOperator()

    assert op


def test_run_ti_init():

    process = "Refresh_Feeders"

    op = TM1RunTIOperator(process_name=process, task_id=process)
    assert op


def test_run_chore_init():

    chore = "Backup"
    op = TM1RunChoreOperator(chore_name=chore, task_id=chore)
    assert op
