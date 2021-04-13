def processData(df):
    # sort by region and title
    df = df.sort_values(by=['region', 'title'])
    # exclude records before 2000
    df = df[df['betreffsjahr'].str.startswith('20')]

    return df