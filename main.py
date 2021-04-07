import pandas as pd
import requests as req
from getData import getData
from processData import processData
from writeMessages import writeMessages


if __name__ == '__main__':
    # get data from db for yesterday and process it
    df = getData()
    df = processData(df)

    # craft messages from data
    messages = writeMessages(df)

    # post to slack channel
    for message in messages:
        req.post('https://hooks.slack.com/services/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', json=message)



