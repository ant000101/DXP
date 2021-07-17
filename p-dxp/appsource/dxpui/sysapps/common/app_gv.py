# -*- coding: utf-8 -*-

# *********************************************************************** #
# Constants
# *********************************************************************** #
DATAMODE_CHOICES = (('A','Active'),('I', 'Inactive'),('D','Deleted'))
DATA_LOADED_BY_CHOICES = (("SYSTEM", "System"),("USER", "User")) # Data loaded by System or entered by User

CURRENCY_TYPE_CHOICES=(('P','Physical'),('D', 'Digital'))
VALID_LOOK_UP = [('iexact','Exact'),('istartswith','StartsWith'),('iendswith','Endswith'),('icontains','Contains'),('range','Range'),('lt','Less Than'),('lte','Less Than Equal To '),('gt','Greater Than'),('gte','Greater Than Equal To')]
GENDER = (('MALE','Male'),('FEMALE','Female'),('TRANS','Trans'))
REALATIONSHIP_STATUS = (('MARRIED','Married'),('SINGLE','single'),('DIVORCED','Divorced'),('WIDOWED','Widowed'))
SOCIAL_ACCOUNT_TYPE = (('GOOGLE','Google'),('FACEBOOK','Facebook'),('TWITTER','Twitter'),('LINKEDIN','LinkedIN'))

# *********************************************************************** #
# super user
# *********************************************************************** #
SUPER_USER_FIRSTNAME = "IT Support"
SUPER_USER_LASTNAME  = "IT Support"
SUPER_USER_NAME = "it-support"
SUPER_USER_EMAIL = "it-support@seaant.com"
SUPER_USER_PASSWORD = "secret123"
SUPER_USER_DATE_JOINED = 946688520 #set as Jan 01, 2000
SUPER_USER_LAST_LOGIN = 946688520  #set as Jan 01, 2000
SUPER_USER_IS_STAFF = True
SUPER_USER_IS_SUPERUSER = True
SUPER_USER_ACTIVE = True
SUPER_USER_EMAIL_VERIFIED = True