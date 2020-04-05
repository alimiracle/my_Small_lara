from bot_config import *
from chatterbot import ChatBot
from flask import Flask, render_template, request
my_bot = ChatBot(name=bot_name, read_only=bot_read_only)

app = Flask(__name__)

@app.route("/get", methods = ['GET', 'POST'])
def get_bot_response():    
    userText = request.values.get('text')
    return str(my_bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()
