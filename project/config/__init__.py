# Contains default secrets to stop tests using them

# You can override with proper secrets to help local development with project.secrets.extra
# Note extra.py MUST be a subset of these to keep test execution safe i.e. always add your stub secrets here first.

SECRET_KEY = 'secret'
DB_URL = 'postgis://postgres:postgres@db:5432/postgres'
