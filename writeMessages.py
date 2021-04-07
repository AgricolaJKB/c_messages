import pandas as pd
import json
from startMessage import writeStartMessage
from mainMessage import writeMainMessages

def writeMessages(df):
    messages = []

    # sort by region and extract todays regions
    df = df.sort_values(by=['region', 'title'])
    df_regions = pd.unique(df.region)

    # assemble messages
    messages = [writeStartMessage(df_regions, len(df))] + writeMainMessages(df, df_regions)

    # convert python dict to json
    #messages = [json.dumps(message) for message in messages]

    # return messages
    return messages