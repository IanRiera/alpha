# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 12:42:07 2018

@author: R325100
"""
import os, sys
from flask import Flask, request
from utils import wit_response
from chat import *
from pymessenger import Bot

app = Flask(__name__)

a = ChatInterface()

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)
    
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                
                # IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']
                
                if messaging_event.get('message'):
                    # Extracting text message
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                        
                    else:
                        messaging_text = 'no text'
                            
                    # Echo
                    response = None

                    entity, value = wit_response(messaging_text)

                    if entity == 'treballador_rol':
                        response = "Ok, buscaré al {} ".format(str(value))
                    a.send_text_message(sender_id, response)
                                                
    return "ok", 200
    
def log(message):
    print(message)
    sys.stdout.flush()
     
if __name__ == "__main__":
        app.run(debug = True, port = 80)
        
