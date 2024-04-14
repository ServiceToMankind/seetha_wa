import os
from flask import Flask, render_template, request, jsonify
import chatbot_api  # Assuming your chatbot code is in chatbot_api.py
from pywa import WhatsApp
from pywa.handlers import MessageHandler, CallbackButtonHandler

from wa_handlers import handle_callback_button, handle_message
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
wa = WhatsApp(
    phone_id=os.getenv("WA_PHONE_ID"),
    token=os.getenv("WA_TOKEN"),
    server=app,
    callback_url=os.getenv("WA_CALLBACK_URL"),
    verify_token=os.getenv("WA_VERIFY_TOKEN"),
    app_id=os.getenv("WA_APP_ID"),
    app_secret=os.getenv("WA_APP_SECRET"),
)
wa.add_handlers(
    MessageHandler(handle_message),
    CallbackButtonHandler(handle_callback_button)
)

@app.route('/')
@app.route('/index')
def home():
    return render_template('chat.html')


@app.route('/chatbot', methods=['POST'])
def chatbot_endpoint():
    data = request.get_json()  # Parse the JSON payload
    print(data['message'])

    if data and 'message' in data:
        user_message = data['message']
        chatbot_response = chatbot_api.get_chatbot_response(user_message)
        print(chatbot_response)
        
        #Chatbot Response
        return jsonify({"response": chatbot_response})

    return jsonify({"error": "Invalid request format"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=80)
