# Importing necessary library
import requests
import json
import streamlit as st

from utils import UI, DataManager

ui_language = UI.ui_language()
user_name, assistant_name, user_language, url, model = DataManager.get_user_config()


# Function to return the ia response
def askingIA(url, model, messages):

    IA_response = ""
    data = {
        "model": model,
        "messages": messages,
    }

    st.toast(ui_language[user_language]["askingIA_success"])

    response = requests.post(url, json=data)

    response_content_str = response.content.decode('utf-8')
    lines = response_content_str.split("\n")
    jsonLines = [line for line in lines if line.strip() != "" and line.strip()[0] == '{' and line.strip()[-1] == '}']

    for line in jsonLines:
        try:
            obj = json.loads(line)
            if obj["message"]["content"]:
                IA_response += obj["message"]["content"]
        except Exception as error:
            print("Error with the JSON parse", error)
    
    return IA_response