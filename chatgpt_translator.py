import openai
import json
with open("./credentials.json","r") as f:
    data = json.load(f)
    token = data["chatgpt_api_token"]
openai.api_key = token



def translate (text:str,language:str, gender:str)->str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "Chat translator to {language}".format(language = language)},
            {"role": "user", "content": "Translate: {text}".format(gender = gender, language = language, text=text)}
        ]
    )
    return (response['choices'][0]['message']['content'].rstrip("."))
