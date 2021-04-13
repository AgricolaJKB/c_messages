import pandas as pd
from messageGenerators.startMessage import writeStartMessage
from messageGenerators.mainMessage import writeMainMessages
from messageGenerators.defaultMessage import writeDefaultMessage


def writeMessages(df):
    messages = []

    # extract todays regions
    df_regions = pd.unique(df.region)

    # assemble messages if df is not empty
    if df.empty:
        messages = [writeDefaultMessage()]
    else:
        messages = [writeStartMessage(df_regions, len(df))] + writeMainMessages(df, df_regions)

    # convert python dict to json
    # messages = [json.dumps(message) for message in messages]

    # return messages
    return messages
