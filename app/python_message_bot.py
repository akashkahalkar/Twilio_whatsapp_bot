from flask import Flask, request
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse
from twilio.rest import Client
from url_parse import ReelsParser
import urllib.parse as urlparse


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def check_server():
    return "Hello there"

@app.route("/whatsapp", methods=["GET", "POST"])
def reply_whatsapp():
    print(request.values)

    response = MessagingResponse()
    
    #get value of body parameter from request
    input_msg = str(request.values.get("Body"))
    #check if given is url for any instagram resource
    result = check_for_insta_url(input_msg)
    print("result from url parser: ", result)
    if isinstance(result, str):
        print("passed as string")
        message = Message()
        #only single result
        if "http" in result:
            
            #create response body by appending text and media url
            message.body("Here is the image/video")
            message.media(result)
        else:
            #create response body by appending text and media url
            message.body(result)
        response.append(message)
    else:
        #array
        print("passed as array")
        for url in result:
            if url is not None:
                message = Message()
                message.media(url)
                response.append(message)
        msg = Message()
        msg.body("Here is the image/video")
        response.append(msg)
    print('final response', str(response))
    return str(response)

#https://www.instagram.com/reel/CEUqwfFpgo0/?igshid=10veydqls6mx4
def check_for_insta_url(msg):
    if 'instagram.com/' in msg:
        return ReelsParser().get_reels_videoUrl(msg)
    else:
        return "send instagram link!"

if __name__ == "__main__":
    app.run()
