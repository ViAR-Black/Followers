from dotenv import load_dotenv
import os

load_dotenv()

pg_host = os.getenv('POSTGRES_HOST')
pg_port = os.getenv('POSTGRES_PORT')
pg_db = os.getenv('POSTGRES_DB')
pg_user = os.getenv('POSTGRES_USER')
pg_password = os.getenv('POSTGRES_PASSWORD')
db_connect_url = f"postgresql+psycopg://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}"
print(db_connect_url)
