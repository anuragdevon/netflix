# Imports
from .base import *
import os

# Set Debug to "False" in .env
DEBUG = False

# Allowed hosts in Cloud Services
ALLOWED_HOSTS = ["*"]

# Database Initialization
# import psycopg2
# try:
#     conn = psycopg2.connect(
#     database="postgres", user='postgres', password='postgres', host='db', port= 5432
#     )
#     conn.autocommit = True
#     sql = "SELECT * FROM INFORMATION_SCHEMA.tables"
#     cur = conn.cursor()
#     print(cur.execute(sql))
#     # print("Database created successfully........")
# except (Exception, psycopg2.DatabaseError) as error:
#     print("ERRRRRRR: ",error)

#Closing the connection
# conn.close()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': 'db',
        'PORT': int(os.environ['DB_PORT'])
    }
}

# Production Server


# # Django Inbuilt Security Vars

# CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_HTTPONLY = True

# SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_SSL_REDIRECT = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# SESSION_COOKIE_SECURE = True
