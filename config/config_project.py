import os

INDEX_LAW = 'law_tech_test_2'
TYPE_DOCUMENT = '_doc'

ES_IP = os.environ.get('ES_IP', 'localhost')
ES_USER = os.environ.get('ES_USER', 'user')
ES_PASS = os.environ.get('ES_PASS', '12345678')
ES_PORT = os.environ.get('ES_PORT', '9202')

minimum_should_match_for_search = "100"

PG_USER = "postgres"
PG_PASSWORD = "nguyennam12399"
PG_HOST = "localhost"
PG_PORT = "5432"
PG_DB_NAME = "lawtech_test2"