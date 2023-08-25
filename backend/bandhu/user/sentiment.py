import requests
import os
your_key  = os.environ["TONE_CHECKER"]

def get_sentiment(question) : 
    response = requests.post(
        "https://api.sapling.ai/api/v1/tone",
        json={
            "key": your_key,
            "text": question
        }
    )

    something = response.json()
    content = something["overall"]

    result = []

    for x in range (len(content)):
        dict = {content[x][1] : content[x][0]}
        result.append(dict)
    return result