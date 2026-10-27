import psycopg2
from src.refuge.config import db_settings

conn = psycopg2.connect(**db_settings())
try:
    with conn.cursor() as cur:
        cur.execute("SELECT version()")
        print(cur.fetchone()[0])
        cur.execute("SELECT current_database(), current_user")
        print(cur.fetchone())
finally:
    conn.close()