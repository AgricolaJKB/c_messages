import pandas as pd

def writeParagraph(title, subtitle, detail, link):
    combined_title = title + ' / ' + subtitle if subtitle else title
    detail_dict = {'Länderdaten': 'Länderebene',
                   'Kreisdaten': 'Kreisebene',
                   'Gemeindedaten': 'Gemeindeebene',
                   'Regierungsbezirke': 'Ebene der Regierungsbezirke',
                   'Sonstiges': 'unbekannte Genauigkeit'}


    paragraph = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f":page_with_curl:   *{ combined_title }*, aufgeschlüsselt bis auf *{ detail_dict[detail] }*. <{ link }|Hier abrufbar>"
        }
    }

    return paragraph

def writeMainMessage(df_subset, region):
    paragraphs = [writeParagraph(row.title, row.subtitle, row.min_level, row.url) for i, row in df_subset.iterrows()]

    message = {
        "blocks": [
            {
                "type": "divider"
            },
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ':round_pushpin:' + region,
                    "emoji": True
                }
            }
        ] + paragraphs
    }

    return message


def writeMainMessages(df, regions):
    messages = [writeMainMessage(df[df.region == region], region) for region in regions]

    return messages