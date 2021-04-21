# Generate main messages: A country section contains a country header and n paragraphs with the published datasets.
# This formula is repeated for each country for which data was published yesterday.


def writeParagraph(title, subtitle, detail, link):
    detail_dict = {'Länderdaten': 'Länderebene',
                   'Kreisdaten': 'Kreisebene',
                   'Gemeindedaten': 'Gemeindeebene',
                   'Regierungsbezirke': 'Ebene der Regierungsbezirke',
                   'Stadtbezirke': 'Ebene der Stadtbezirke',
                   'Wahlkreise': 'Wahlkreisebene',
                   'Statistische Regionen': 'unbekannte Genauigkeit',
                   'Sonstiges': 'unbekannte Genauigkeit'}

    combined_title = title + ' / ' + subtitle if subtitle else title
    try:
        detail_nicename = detail_dict[detail]
    except KeyError:
        detail_nicename = 'unbekannte Genauigkeit'

    paragraph = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"\n>:page_with_curl:   *{ combined_title }*, aufgeschlüsselt bis auf *{ detail_nicename }*. <{ link }|Hier abrufbar>"
        }
    }

    return paragraph

def writeSection(df_subset, region):
    paragraphs = [writeParagraph(row.title, row.subtitle, row.min_level, row.url) for i, row in df_subset.iterrows()]

    blocks = [{
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": ':round_pushpin:' + region,
            "emoji": True
        }
    }] + paragraphs

    return blocks


def writeMainMessages(df, regions):
    blocks = [writeSection(df[df.region == region], region) for region in regions]
    # messages = [writeSection(df[df.region == region], region) for region in regions]

    return blocks