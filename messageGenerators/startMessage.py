# Generate intro message

def writeStartMessage(regions, dataset_count):
    text = f":wave:   Moin! Gestern sind *{dataset_count} neue Datensätze* aus *{len(regions)} Bundesländern* erschienen. Sie stammen aus {', '.join(regions[:-1])} $


    blocks = [
            {
             	"type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": text
                }
            }
	]

    return blocks

