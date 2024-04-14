from pywa import WhatsApp
from pywa.types import Message, CallbackButton, Button
from pywa.filters import text, callback
import chatbot_api  # Assuming your chatbot code is in chatbot_api.py



def handle_message(client: WhatsApp, message: Message):
    print("Message from: "+ message.from_user.name + "| Text Content: " +message.text)
    
    if(message.text == "Hi" or message.text == "Hello"):
        message.react('👋')
        message.reply_text(
            text=f'Hello {message.from_user.name}! I am Seetha from STM. How can I help you today?',
            # buttons=[
            #     Button(
            #         title='Click me!',
            #         callback_data='id:123'
            #     )
            # ]
        )
    else:
        chatbot_response = chatbot_api.get_chatbot_response(message.text)
        print("Response: " + chatbot_response)
        message.reply_text(chatbot_response)

def handle_callback_button(client: WhatsApp, clb: CallbackButton):
    print(clb.data)
    clb.reply_text('You clicked me!')