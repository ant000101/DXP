import os
import datetime
import traceback
from config import settings
from sysapps.common import app_logger

logger = app_logger.createLogger("app_scripts")

dbengine = settings.DATABASES['default']['ENGINE']
dbname   = settings.DATABASES['default']['NAME']
dbhost   = settings.DATABASES['default']['HOST']
dbuser   = settings.DATABASES['default']['USER']
dbpass   = settings.DATABASES['default']['PASSWORD']

@app_logger.functionlogs(log="app_scripts")
def backup_database():
    result=False
    try:
        if dbengine == "django.db.backends.sqlite3":
            #pass
            #TODO: backup sqlite3 database
            result=True

        if dbengine == "mysql.connector.django":
            today_date = datetime.datetime.now()
            filestamp = today_date.strftime('%Y-%m-%d-%H:%M:%S')
            filename = "%s-%s.sql" % (dbname, filestamp)
            destination_path = os.path.join(settings.BASE_DIR, 'backups', filename)
            os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s | gzip -c > %s.gz" % (dbuser, dbpass, dbhost, dbname, destination_path))
            logger.debug("database backed up : %s" %(destination_path))
            result=True

        if dbengine == "django.db.backends.postgresql_psycopg2":
            #pass
            #TODO: backup Postgres database
            result=True


    except Exception as error:
        logger.error(traceback.format_exc())
        raise error
    return result

@app_logger.functionlogs(log="app_scripts")
def run():
    logger.info("Starting ...")
    backup_database()    
    logger.info("End !!!")


