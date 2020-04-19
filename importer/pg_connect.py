import psycopg2
from psycopg2 import pool


try:
    postgreSQL_pool = psycopg2.pool.ThreadedConnectionPool(1, 20, user = "postgres",
                                              password = "nguyennam12399",
                                              host = "localhost",
                                              port = "5432",
                                              database = "lawtech_test2")
    if postgreSQL_pool:
        print("Connection pool created successfully")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while connecting to PostgreSQL", error)

