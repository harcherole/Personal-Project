from airflow import DAG
from airflow.operators.bash_operator import BashOperator

def subdag_factory(parent_dag_id, subdag_id, default_args) -> DAG:
    with DAG(f'{parent_dag_id}.{subdag_id}', default_args=default_args) as dag:
        for l in ['A', 'B', 'C']:
            BashOperator(task_id=f'processing_{l}', bash_command='ls')
    return dag