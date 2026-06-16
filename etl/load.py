from sqlalchemy import create_engine
import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

conn_engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def load_data(df):
    try: 
        df.to_sql(name="us_state_gas_prices", con=conn_engine, if_exists="replace", index=False)
        print("Data loaded successfully!")
    except Exception as e:
        print("There was a problem loading the data to the DB!", e)