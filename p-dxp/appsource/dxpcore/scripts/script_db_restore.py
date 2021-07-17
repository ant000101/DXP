import os
import datetime
import traceback
import raw_input
from config import settings
from sysapps.common import app_logger

logger = app_logger.createLogger("app_scripts")

dbengine = settings.DATABASES['default']['ENGINE']
dbname   = settings.DATABASES['default']['NAME']
dbhost   = settings.DATABASES['default']['HOST']
dbuser   = settings.DATABASES['default']['USER']
dbpass   = settings.DATABASES['default']['PASSWORD']

@app_logger.functionlogs(log="app_scripts")
def restore_database():
    result=False
    try:
        if dbengine == "django.db.backends.sqlite3":
            #pass
            #TODO: restore sqlite3 database
            result=True
        
        if dbengine == "mysql.connector.django":
            sql_backup_path = raw_input("Please enter full path of sql backup : ")
            print ("Please Wait .... ")
            os.popen("mysql -u %s -p%s -h %s %s < %s" % (dbuser, dbpass, dbhost, dbname, sql_backup_path))
            print ("database restored")
            logger.debug("database restored from : %s" %(sql_backup_path))
            result=True

        if dbengine == "django.db.backends.postgresql_psycopg2":
            #pass
            #TODO: restore Postgres database
            result=True

    except Exception as error:
        logger.error(traceback.format_exc())
        raise error
    return result    

@app_logger.functionlogs(log="app_scripts")
def run():
    logger.info("Starting ...")
    restore_database()    
    logger.info("End !!!")


