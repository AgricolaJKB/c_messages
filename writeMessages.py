import pandas as pd
from messageGenerators.startMessage import writeStartMessage
from messageGenerators.mainMessage import writeMainMessages
from messageGenerators.defaultMessage import writeDefaultMessage


def writeMessages(df):
    # extract todays regions
    df_regions = pd.unique(df.region)

    # assemble messages if df is not empty
    if df.empty:
        messages = writeDefaultMessage()
    else:
	    # generate message blocks
        raw_blocks = [writeStartMessage(df_regions, len(df))] + writeMainMessages(df, df_regions)

        # outputted as list of lists; reducing to one dimension
        blocks = [i for row in raw_blocks for i in row]

        messages = {
            "blocks": blocks
        }

    # return messages
    return messages

