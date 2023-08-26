import requests
import os

def get_sentiment(question) : 
    response = requests.post(
        "https://api.sapling.ai/api/v1/tone",
        json={
            "key": "G85HRMB0LLC16MBQ78BN4KI4CO1NCOAE",
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