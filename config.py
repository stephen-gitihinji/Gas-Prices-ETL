from dotenv import load_dotenv
import os

load_dotenv()

#massive api key
MASSIVE_API_KEY = os.getenv("MASSIVE_API_KEY")

#DB connection
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")