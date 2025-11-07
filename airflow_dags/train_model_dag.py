from datetime import datetime

from airflow.sdk import dag, task

from ml_core.train import train_models

default_args = {
    "owner": "mlops",
    "retries": 1,
}


@dag(
    dag_id="train_models_dag",
    default_args=default_args,
    description="Автоматический DAG для обучения ML моделей",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["ml", "training"],
    schedule="@once",
    is_paused_upon_creation=False,
)
def train_models_dag():
    @task
    def train_models_task():
        return train_models()

    train_models_task()


train_models_dag()
