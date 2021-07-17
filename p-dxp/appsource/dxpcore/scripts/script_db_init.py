import os
import datetime
import traceback
import sys
import shutil
import json
import glob
import ast
import traceback
from config import settings
from sysapps.common import app_logger, app_gv
from django.core.management import call_command
from django.contrib.auth.admin import User


logger = app_logger.createLogger("app_scripts")

dbengine = settings.DATABASES['default']['ENGINE']
dbname   = settings.DATABASES['default']['NAME']
dbhost   = settings.DATABASES['default']['HOST']
dbuser   = settings.DATABASES['default']['USER']
dbpass   = settings.DATABASES['default']['PASSWORD']


# @app_logger.functionlogs(log="app_scripts")
# def createDatabase():
#     result=False

#     try:
#         if dbengine == "django.db.backends.sqlite3":
#             import sqlite3
#             logger.debug("creating database...{0}".format(dbname))        
#             conn = sqlite3.connect(dbname)
#             logger.debug("created database...{0}".format(dbname))
#             result=True          

#         if dbengine == "mysql.connector.django":
#             import mysql.connector            
#             db = mysql.connector.connect(host=dbhost,user=dbuser,passwd=dbpass)
#             logger.debug("creating database...{0}".format(dbname))
#             cursor = db.cursor()
#             createsql = "create SCHEMA %s CHARACTER SET utf16 COLLATE utf16_general_ci"% (dbname)
#             cursor.execute(createsql)
#             cursor.close()
#             db.close()
#             logger.debug("created database...{0}".format(dbname))
#             result=True
        
#         if dbengine == "django.db.backends.postgresql_psycopg2":
#             import psycopg2
#             db = psycopg2.connect("dbname='master' user='{dbuser}' host='{dbhost}' password='{dbpass}'".format(dbuser=dbuser, dbpass=dbpass, dbhost=dbhost))
#             cursor = db.cursor()
#             logger.debug("creating database...{0}".format(dbname))
#             cursor = db.cursor()
#             createsql = "create SCHEMA %s CHARACTER SET utf16 COLLATE utf16_general_ci"% (dbname)
#             cursor.execute(createsql)
#             cursor.close()
#             db.close()
#             logger.debug("created database...{0}".format(dbname))
#             result=True
        
#     except Exception as error:
#         logger.error(traceback.format_exc())
#         raise error
#     return result

# @app_logger.functionlogs(log="app_scripts")
# def dropDatabase():
#     result=False
#     try:
#         if dbengine == "django.db.backends.sqlite3":
#             import sqlite3
#             logger.debug("droping database...{0}".format(dbname))        
#             os.remove(dbname)
#             result=True

#         if dbengine == "mysql.connector.django":
#             import mysql.connector            
#             db = mysql.connector.connect(host=dbhost,user=dbuser,passwd=dbpass)
#             cursor = db.cursor()
#             dropsql = 'drop SCHEMA %s' % (dbname)
#             logger.debug(dropsql)
#             logger.debug("droping database...{0}".format(dbname))
#             cursor.execute(dropsql)
#             cursor.close()
#             db.close()
#             logger.debug("dropped database...{0}".format(dbname))
#             result=True

#         if dbengine == "django.db.backends.postgresql_psycopg2":
#             import psycopg2
#             db = psycopg2.connect("dbname='master' user='{dbuser}' host='{dbhost}' password='{dbpass}'".format(dbuser=dbuser, dbpass=dbpass, dbhost=dbhost))
#             cursor = db.cursor()
#             dropsql = 'drop SCHEMA %s' % (dbname)
#             logger.debug(dropsql)
#             logger.debug("droping database...{0}".format(dbname))
#             cursor.execute(dropsql)
#             cursor.close()
#             db.close()
#             logger.debug("dropped database...{0}".format(dbname))
#             result=True


#     except Exception as error:
#         logger.error(traceback.format_exc())
#         raise error
#     return result

@app_logger.functionlogs(log="app_scripts")
def run_migrations():
    result = False
    try:
        #remove migration files
        app_list = [ app for app in settings.INSTALLED_APPS ]
        for apps in app_list:
            apps = apps.replace(".","/")
            migration_path = os.path.join(settings.BASE_DIR, '%s/migrations'%(apps))
            for file in glob.glob(migration_path+"/0*.py"):
                os.remove(file)

        all_app_list = [ app for app in settings.INSTALLED_APPS ]
        for apps in all_app_list:
            if apps.startswith("sysapps") or apps.startswith("bizapps"):
                apps = apps.rsplit(".",1)
                try:
                    call_command('makemigrations','--pythonpath', apps[0].replace(".","/"),apps[1], interactive=False)
                except Exception as error:
                    logger.error(traceback.format_exc())
                    raise error

        result = True
    except Exception as error:
        logger.error(traceback.format_exc())
        raise error

    call_command('makemigrations', interactive=False)
    call_command('migrate', interactive=False)

    return result

@app_logger.functionlogs(log="app_scripts")
def create_superuser():
    superuser = User()
    superuser.is_active = app_gv.SUPER_USER_ACTIVE
    superuser.is_superuser = app_gv.SUPER_USER_IS_SUPERUSER
    superuser.is_staff = app_gv.SUPER_USER_IS_STAFF
    superuser.username = app_gv.SUPER_USER_NAME
    superuser.email = app_gv.SUPER_USER_EMAIL
    superuser.set_password(app_gv.SUPER_USER_PASSWORD)
    superuser.first_name = app_gv.SUPER_USER_FIRSTNAME
    superuser.last_name = app_gv.SUPER_USER_LASTNAME
    superuser.save()    

@app_logger.functionlogs(log="app_scripts")
def run():
    logger.info("Starting ...")
    run_migrations()
    create_superuser()
    logger.info("End !!!")
