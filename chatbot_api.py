import openai
import os
from system_text import system_text

# Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key="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"

# load system text
system_text = system_text()

def get_chatbot_response(user_message, conversation=[]):
    # Append the new user message to the existing conversation
    conversation.append({"role": "user", "content": user_message})

    # Prepend the system message to the conversation
    messages = [{"role": "system", "content": system_text}] + conversation

    # Request gpt-3.5-turbo for chat completion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Get the response from the chatbot
    chat_message = response['choices'][0]['message']['content']
    
    # Append the chatbot response to the conversation
    conversation.append({"role": "assistant", "content": chat_message})
    
    return chat_message