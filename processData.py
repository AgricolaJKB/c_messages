def processData(df):
    # exclude records before 2000
    df = df[df['betreffsjahr'].str.startswith('20')]

    return df