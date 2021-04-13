import requests as req
from env import env
from getData import getData
from processData import processData
from writeMessages import writeMessages


if __name__ == '__main__':
    # get data from db for yesterday and process it
    df = getData()
    df = processData(df)

    # craft messages from data
    messages = writeMessages(df)

    # assemble webhook-url
    webhookUrl = f'https://hooks.slack.com/services/{env("S_WORKSPACE")}/{env("S_WEBHOOK_TOKEN")}'

    # post to slack channel
    for message in messages:
        req.post(webhookUrl, json=message)



