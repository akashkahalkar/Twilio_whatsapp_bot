from flask import Blueprint, request
import validators
from app.handler import URLHandler
from app.twilio_webhook.twilio_message_handler import TwilioMessageHandler

twilio_api = Blueprint('twilio', __name__, url_prefix='/twilio')

@twilio_api.route('/', methods=['GET'])
def checkServer():
    return '<P>Ahoy, landlubber! What be yer business sailin these treacherous seas?<p>'

@twilio_api.route('/whatsapp', methods=['GET', 'POST'])
def handle_whatsapp_webhook():

    message_handler = TwilioMessageHandler()
    receivedUrl = str(request.values.get("Body"))
    if not validators.url(receivedUrl):
        return message_handler.get_error_message("Invalid url")
    downloadLink = URLHandler().handle(receivedUrl)
    return message_handler.get_message(downloadLink)