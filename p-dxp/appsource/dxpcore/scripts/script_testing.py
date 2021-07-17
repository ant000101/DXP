from django.core.management import call_command

from config import settings
from sysapps.common import app_logger

logger = app_logger.createLogger("app_scripts")

@app_logger.functionlogs(log="app_scripts")
def run():
    logger.info("Starting")
    call_command('makemigrations', interactive=False)
    call_command('migrate', interactive=False)