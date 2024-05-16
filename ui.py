# streamlit run .\ui.py --theme.base="light" --server.port=11434 --server.address=0.0.0.0 --server.headless=true

# Importing necessary library
import streamlit as st
import uuid

from askingIA import askingIA
from utils import DataManager, UI, CategoryManager

# Config the streamlit page
UI.set_page()
ui_language = UI.ui_language()

# Import user config -> config.json
user_name, assistant_name, user_language, url, model = DataManager.get_user_config()

# Load the current history -> history.json
history = DataManager.load_data()

# Create the categories section in function of history.json
categories = DataManager.get_categories()
selected_categories = st.sidebar.selectbox(ui_language[user_language]["selected_categories"], categories)

# Create a delete and clear chat button
delete_category_button = st.button(ui_language[user_language]["delete_category_button"])
clear_category_button = st.button(ui_language[user_language]["clear_category_button"])

# Call the function for delete or clear chat
if delete_category_button:
    CategoryManager.delete_category(selected_categories, history)

if clear_category_button:
    CategoryManager.clear_category(selected_categories, history)

# Create an add category process
add_category_input = st.sidebar.text_input(ui_language[user_language]["add_category_input"], value="")
add_prompt_input = st.sidebar.text_area(ui_language[user_language]["add_prompt_input"], value="")
add_category_button = st.sidebar.button(ui_language[user_language]["add_category_button"])

# Call the function for add a category
if add_category_button:
    CategoryManager.add_category(add_category_input, add_prompt_input, history)

# Create the chat area and message container
user_input = st.chat_input(ui_language[user_language]["user_input"])
messages_container = st.container(height=550)

# Send a message
if user_input:

    # Get the user message and save it in the history
    message = user_input
    user_unique_id = str(uuid.uuid4())
    user_object = {
        "id": user_unique_id,
        "role": "user",
        "content": message
    }
    CategoryManager.add_object(user_object, selected_categories, history)

    # Get the current category history
    messages = CategoryManager.get_history(selected_categories, history)
    IA_response = askingIA(url, model, messages)

    # Get the IA response and save it in the history
    IA_unique_id = str(uuid.uuid4())
    IA_object = {
        "id": IA_unique_id,
        "role": "assistant",
        "content": IA_response
    }
    CategoryManager.add_object(IA_object, selected_categories, history)

# Get the current history
messages = CategoryManager.get_history(selected_categories, history)

# Display the chat
UI.display_chat(messages, messages_container, assistant_name, user_name)