def writeStartMessage(regions, dataset_count):
    text = f":wave:   Moin! Gestern sind *{dataset_count} neue Datensätze* aus *{len(regions)} Bundesländern* erschienen. Sie stammen aus {', '.join(regions[:-1])} und {regions[-1]}."


    message = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": text
                }
            }
        ]
    }

    return message


if __name__ == '__main__':
    writeStartMessage("test")