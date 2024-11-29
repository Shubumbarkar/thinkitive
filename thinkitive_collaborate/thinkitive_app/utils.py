import requests

def get_ai_suggestions(text):
    response = requests.post('https://api.languagetool.org/v2/check', data={
        'text': text,
        'language': 'en-US',
    })
    return response.json()
