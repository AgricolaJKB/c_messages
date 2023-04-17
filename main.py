import os
import requests as req
from loguru import logger
from getData import getData
from processData import processData
from writeMessages import writeMessages
from dotenv import load_dotenv

logger.add('logs/main.log', format='{time} {level} {message}', level='INFO', rotation='1 week', compression='zip')

load_dotenv()

if __name__ == '__main__':
    logger.info('Starting main.py')

    # get data from db for yesterday and process it
    df = getData()
    df = processData(df)

    # craft messages from data
    messages = writeMessages(df)

    # assemble webhook-url
    webhookUrl = f'https://hooks.slack.com/services/{os.environ.get("S_WORKSPACE")}/{os.environ.get("S_WEBHOOK_TOKEN")}'

    # post to slack channel
    for i in range(0, len(messages["blocks"]), 10):
        resp = req.post(webhookUrl, json={
            "blocks": messages["blocks"][i:i+10]
        })
        if (resp.status_code != 200):
            print(f'c_messages error: {resp.status_code} [{resp.text}]')

    logger.info('Finished main.py')

