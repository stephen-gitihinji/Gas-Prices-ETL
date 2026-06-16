from etl.extract import extract_gas_prices
from etl.transform import transform_data
from etl.load import load_data

def run_pipeline():
    raw_data = extract_gas_prices()
    transformed_data = transform_data(raw_data)
    load_data(transformed_data)
    
if __name__ == "__main__":
    run_pipeline()