# 🗨️ Ollama AI Chat Interface

## Table of Contents
1. [📄 Description](#description)
2. [🔧 Prerequisites](#prerequisites)
3. [💻 Installation](#installation)
4. [⚙️ Configuration](#configuration)
5. [🚀 Using the Interface](#using-the-interface)
6. [📂 Managing Categories](#managing-categories)
7. [📝 History](#history)
8. [❓ Why JSON?](#why-json)
9. [🌐 Obtaining IPv4](#obtaining-ipv4)
10. [💡 Suggestions for Improvement](#suggestions-for-improvement)
11. [👨‍💻 Author](#author)

## 📄 Description
This project is a web interface for chat between a user and an AI, utilizing various AI models compatible with the Ollama API. Supported models include: **llama3**, **mistral**, **mini orca**, and any LLMs using the same API.

## 🔧 Prerequisites
- Install [Ollama](https://ollama.com) and launch a compatible model.
- Supported models: **llama3**, **mistral**, **mini orca**, etc.

## 💻 Installation
Follow these steps to install and launch the interface:

1. **Clone the project:**
`git clone https://github.com/TheValll/Ollama-AI-Chat-Interface`

2. **Install dependencies:**
`pip install -r requirements.txt`

3. **Run the Streamlit interface:**
`streamlit run./ui.py --theme.base="light" --server.port=11434 --server.address=0.0.0.0 --server.headless=true`

   Note: If the Ollama server URL is changed in the `config.json` file, the Streamlit port must match.

## ⚙️ Configuration
You can change the `config.json` file :
json { "user_name": "user", "assistant_name": "Llama", "language": "en", "url": "http://localhost:11434/api/chat", "model": "llama3:8b" }

- `user_name`: User's name.
- `assistant_name`: Assistant's name.
- `language`: Interface language (default is "en", fr and en is available).
- `url`: URL of the Ollama server (default is `http://localhost:11434/api/chat`).
- `model`: Model used on Ollama (default is `llama3:8b`).

## 🚀 Using the Interface
The interface will be accessible via the IPv4 of the host computer + the default port 11434, from any device connected to the same network.
Exemple : `192.168.1.2:11434`

## 📂 Managing Categories
The user can manage multiple conversations called categories:

- Default Category: A default category is provided and cannot be deleted.
- Add a Category: Add a new category with a required name and prompt.
- Clear a Category: Clear the chat history of a category without deleting the initial prompt.
- Delete a Category: Delete a user-created category.

## 📝 History
All chat histories are stored in a `history.json` file. This file keeps a record of all conversations in each category.

## ❓ Why JSON?
The JSON format is chosen for history because it is easy to transport and interchangeable with other JSON files. It allows for simple and efficient management of conversation data.

## 🌐 Obtaining IPv4
To access the interface from other devices on the same network, you will need to know the IPv4 of the host computer. Here's how to obtain your IPv4:

### On Windows:
Open Command Prompt (`cmd`).
Type the following command:
bash ipconfig

Look for the IPv4 address in the results under the network adapter in use (usually something like `192.168.x.x`).

### On macOS/Linux:
Open a terminal.
Type the following command:
bash ifconfig

Look for the IPv4 address in the results under the network interface in use (usually something like `192.168.x.x`).

Use this IPv4 address followed by port 11434 to access the interface from other devices connected to the same network.

## 💡 Suggestions for Improvement
Feel free to propose ideas or improvements for this project. Your feedback is valuable for enhancing the user experience and features of the interface.

## 👨‍💻 Author
This project was developed by Valentin Massonniere.
