import psycopg2
from psycopg2 import pool
from config.config_project import PG_USER, PG_PASSWORD, PG_HOST, PG_PORT, PG_DB_NAME

try:
    postgreSQL_pool = psycopg2.pool.ThreadedConnectionPool(1, 20, user=PG_USER,
                                                           password=PG_PASSWORD,
                                                           host=PG_HOST,
                                                           port=PG_PORT,
                                                           database=PG_DB_NAME)
    if postgreSQL_pool:
        print("Connection Postgresql pool created successfully")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connecting to PostgreSQL: ", error)
