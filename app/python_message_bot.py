from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
#from url_parse import ReelsParser
from teradownloader import TeraDownloader
from yt_downlaoder import YTLoader
import requests
import validators

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def check_server():
    return "Hello there"

@app.route("/shortcuts", methods=["GET", "POST"])
def handle_shortcuts():
    input_msg = str(request.values.get("Body"))
    result = __url_hander(input_msg)
    response = MessagingResponse()
    message = Message()
    message.body(result)
    response.append(message)
    return str(response)

@app.route("/whatsapp", methods=["GET", "POST"])
def reply_whatsapp():    
    #get value of url query parameter from request
    input_msg = str(request.values.get("Body"))
    result = __url_hander(input_msg)
    
    mediaSize = __get_media_size(result)
    response = MessagingResponse()
    message = Message()
    if  mediaSize > 0 and mediaSize < 20:
        message.body("Requested video")
        message.media(result)
    else:
        message.body(f"✅ Here is the Download Link: \n {result}")
        response.append(message)
    return str(response)

def __url_hander(url):
    dlink = ""
    all_supported_domain = {'instagram.com', 'x.com', 'youtube.com', 'teraboxapp.com'}
    ytdlp_suported_domain = {'instagram.com', 'x.com', 'youtube.com'}

    if validators.url(url) and any(domain in url for domain in all_supported_domain) :
        if any(domain in url for domain in ytdlp_suported_domain):
            dlink = YTLoader().getUrl(url)
        elif 'teraboxapp.com' in url:
            dlink = TeraDownloader().get_fast_download_link(url)
    else:
        dlink = "❌ Invalid Link 💦 \n Please send a valid *video* link from given domains, Youtube | x.com | terabox | instagram \n 🍑" 
    return dlink

def __get_media_size(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            size = int(response.headers.get('content-length', 0))
            inMb = size / (1024 * 1024)
            return int(inMb)
        else:
            return -1
    except Exception as e:
       return 0

if __name__ == "__main__":
    app.run()
