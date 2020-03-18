# Author: Ian Riera Smolinska
from wit import Wit

access_token = ""

client = Wit(access_token = access_token)

def wit_response(message_text):
	resp = client.message(message_text)
	return resp
