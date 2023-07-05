import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

def get_customer_info(name):
    conn = psycopg2.connect(
        database = "test",
        user = "root",
        # password = os.getenv("DB_PASSWORD"),
        password = "DB_PASSWORD",
        host = "localhost",
        port = "5432"
    )
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows

get_customer_info("Archer")
print("dfadsf")