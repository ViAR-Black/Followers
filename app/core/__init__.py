from .db import DatabaseConnection
from .config import max_pool_size, min_pool_size, db_connect_url

db_connection = DatabaseConnection(int(max_pool_size), int(min_pool_size), db_connect_url)