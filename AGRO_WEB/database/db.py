import psycopg2
from flask import current_app

def connect_to_db():
    conn = psycopg2.connect(current_app.config['DATABASE_URI'])
    return conn

def get_query_result_conect(conn):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT 1")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result
