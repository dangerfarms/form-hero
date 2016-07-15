from project.settings.test import *


DATABASES = {
    'default': dj_database_url.parse('postgis://postgres:postgres@127.0.0.1:5432/postgres')
}
