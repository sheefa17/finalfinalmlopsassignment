import pandas as pd

def preprocess(df):
    # Ensure input is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        df = pd.DataFrame(df)

    # Fill missing values forward then backward
    df.ffill(inplace=True)
    df.bfill(inplace=True)

    return df.to_numpy()

