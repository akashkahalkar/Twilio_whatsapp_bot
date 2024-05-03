from flask import Blueprint, request
import validators
#from handler import URLHandler
from twilio_webhook.twilio_message_handler import TwilioMessageHandler

twilio_api = Blueprint('twilio', __name__, url_prefix='/twilio')

@twilio_api.route('/', methods=['GET'])
def checkServer():
    return '<P>Ahoy, landlubber! What be yer business sailin these treacherous seas?<p>'

@twilio_api.route('/whatsapp', methods=['GET', 'POST'])
def handle_whatsapp_webhook():
    return "<H3>passed</H3>"
    # message_handler = TwilioMessageHandler()
    # error_message = message_handler.get_error_message("Arrr! I be at yer service, matey! Unfortunately,\n I can fetch links from the seven seas like YouTube or Instagram or X or terabox. 🏴‍☠️")
    # receivedUrl = str(request.values.get("Body"))
    # if not validators.url(receivedUrl):
    #     return error_message
    # downloadLink = URLHandler().handle(receivedUrl)
    # if downloadLink is None:
    #     return error_message
    # return message_handler.get_message(downloadLink)