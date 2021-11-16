import os

from pydantic import BaseSettings


class Config(BaseSettings):

    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    APP_BASE_URL = f"https://{os.getenv('APP_BASE_URL')}"  # prod settings
    # APP_BASE_URL = os.getenv('APP_BASE_URL')  # local settings


class CeleryConfig(BaseSettings):

    broker_url = os.getenv("CELERY_BROKER_URL")
    result_backend = os.getenv("CELERY_RESULT_BACKEND")
    imports = ["src.tasks.main_tasks"]
    enable_utc = True
    timezone = "Europe/Amsterdam"
    task_track_started = True
    result_persistent = True
    task_publish_retry = True
    # The acks_late setting would be used when you need the task to be executed again
    # if the worker (for some reason) crashes mid-execution
    task_acks_late = "Enabled"


app_config = Config()
celery_config = CeleryConfig()
