# Generate default message

def writeDefaultMessage():
    text = f":wave:   Moin! Gestern sind leider *keine* neuen Datensätze erschienen."


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