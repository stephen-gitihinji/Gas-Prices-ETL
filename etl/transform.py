import pandas as pd

def transform_data(raw_data):
    #extracting the neccessary data from the json data
    required_data = raw_data.get('result')

    #converting the data to a dataframe
    df = pd.DataFrame(required_data)

    df = df.rename(columns= {'name': 'state'})

    #removing the $ sign from the price column values
    cols = ["regular", "midGrade", "premium", "diesel"]
    df[cols] = df[cols].apply(
        lambda col: col.str.replace("$", "", regex=False)
    )
    #changing the prices data types to float
    df[cols] = df[cols].astype(float)

    df = df[["state", "currency", "regular", "midGrade", "premium", "diesel"]]
    return df