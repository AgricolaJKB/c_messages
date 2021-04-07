import pandas as pd

def processData(df):
    # exclude old datasets
    df = df[df['betreffsjahr'].str.startswith('20')]

    return df