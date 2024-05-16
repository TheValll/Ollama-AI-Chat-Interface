# Importing necessary library
import json
import streamlit as st
import uuid

from PIL import Image
from streamlit_js_eval import streamlit_js_eval


# DataManager class, manage all the data here
class DataManager:

    # Get the history in the history.json
    @staticmethod
    def load_data():
        f = open('history.json')
        data = json.load(f)
        f.close()
        return data

    # Save a history in the history.json
    @staticmethod
    def save_data(data):
        with open('history.json', 'w') as f:
            json.dump(data, f, indent=4)

    # Get all categories name in the history.json
    @staticmethod
    def get_categories():
        categories = []
        data = DataManager.load_data()
        for key in data:
            categories.append(key)
        return categories

    @staticmethod
    def get_user_config():
        f = open('config.json')
        data = json.load(f)
        f.close()

        for key in data:
            match key:
                case "user_name":
                    user_name = data[key]
                case "assistant_name":
                    assistant_name = data[key]
                case "language":
                    user_language = data[key]
                case "url":
                    url = data[key]
                case "model":
                    model = data[key]

        return user_name, assistant_name, user_language, url, model


# UI class, manage the ui here
class UI:

    # Set the streamlit app settings
    @staticmethod
    def set_page():
        favicon = Image.open("./logo.png")

        st.set_page_config(
            page_title="Ollama chat",
            layout="wide",
            page_icon=favicon,
            initial_sidebar_state="auto",
        )

        # Remove the hamburger and footer streamlit menu
        padding_top = 5
        hide_streamlit_style = f"""
        <style>
        #MainMenu {{visibility: hidden;}}
        .appview-container .main .block-container{{padding-top: {padding_top}rem;}}
        footer {{visibility: hidden;}}
        </style>
        """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Display a conversation
    @staticmethod
    def display_chat(messages, messages_container, assistant_name, user_name):
        for message in messages[1:]:
            match message["role"]:
                case "assistant":
                    messages_container.chat_message("assistant", avatar="🦙").write(
                        f"{assistant_name}: {message["content"]}")
                case "user":
                    messages_container.chat_message("user", avatar="🐧").write(f"{user_name}: {message["content"]}")

    # Get the ui language for inputs and pop up
    @staticmethod
    def ui_language():
        f = open('ui_language.json')
        data = json.load(f)
        f.close()
        return data


ui_language = UI.ui_language()
user_name, assistant_name, user_language, url, model = DataManager.get_user_config()


# CategoryManager class, manage categories here
class CategoryManager:

    # Add a message in the history
    @staticmethod
    def add_object(obj, domain, history):
        for key in history:
            if key == domain:
                history[key].append(obj)
                DataManager.save_data(history)
                break

    # Get the history of a specific category
    @staticmethod
    def get_history(domain, history):
        for key in history:
            if key == domain:
                return history[key]

    # Add a new category
    @staticmethod
    def add_category(category_name, add_prompt_input, history):

        # Check if an input is not empty
        if category_name == "" or add_prompt_input == "":
            st.sidebar.error(ui_language[user_language]["add_category_error_1"], icon="🚨")

        for key in history:

            # Add the category if the category doesn't exist and if 0 inputs is empty
            if key != category_name and category_name != "" and add_prompt_input != "":
                category_id = str(uuid.uuid4())
                obj = {
                    "id": category_id,
                    "role": "user",
                    "content": add_prompt_input
                }
                history[category_name] = [obj]
                DataManager.save_data(history)
                st.sidebar.success(ui_language[user_language]["add_category_success"].format(category_name))
                streamlit_js_eval(js_expressions="parent.window.location.reload()")
            else:
                st.sidebar.error(ui_language[user_language]["add_category_error_2"], icon="🚨")

    # Delete a category
    @staticmethod
    def delete_category(category_name, history):
        match category_name:
            # Check if the streamlit input don't bug
            case "":
                st.sidebar.error(ui_language[user_language]["delete_category_error_1"], icon="🚨")
            # Cannot remove the default category cause break the app
            case "Default":
                st.sidebar.error(ui_language[user_language]["delete_category_error_2"], icon="🚨")
            # Check if the category exist if the streamlit input bug
            case category_name if category_name not in history:
                st.sidebar.error(ui_language[user_language]["delete_category_error_3"].format(category_name), icon="🚨")
            # Remove the category
            case _:
                del history[category_name]
                DataManager.save_data(history)
                st.sidebar.success(ui_language[user_language]["delete_category_success"].format(category_name))
                streamlit_js_eval(js_expressions="parent.window.location.reload()")

    # Clear a category chat without the prompt
    @staticmethod
    def clear_category(category_name, history):
        match category_name:
            # Check if the streamlit input don't bug
            case "":
                st.sidebar.error(ui_language[user_language]["clear_category_error_1"], icon="🚨")
            # Check if the category exist if the streamlit input bug
            case category_name if category_name not in history:
                st.sidebar.error(ui_language[user_language]["clear_category_error_2"].format(category_name), icon="🚨")
            # Clean the history without the prompt in the index 0
            case _:
                history[category_name] = history[category_name][:1]
                DataManager.save_data(history)
                st.sidebar.success(ui_language[user_language]["clear_category_success"].format(category_name))
                streamlit_js_eval(js_expressions="parent.window.location.reload()")