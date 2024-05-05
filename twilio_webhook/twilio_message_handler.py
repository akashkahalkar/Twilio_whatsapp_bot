from twilio.twiml.messaging_response import Message, MessagingResponse
import requests

class TwilioMessageHandler:

    def get_error_message(self, error_message):
        response = MessagingResponse()
        message = Message()
        message.body(error_message)
        response.append(message)
        return str(response)

    def get_message(self, url):
        
        mediaSize = self.__get_media_size(url)
        response = MessagingResponse()
        message = Message()

        if  mediaSize > 0 and mediaSize < 15:
            message.body("Requested video \n ")
            message.media(url)
        else:
            message.body(f"✅ Avast ye matey! Take heed and follow this map to the treasure: \n {url}")
        
        response.append(message)
        return str(response)
    
    def __get_media_size(self, url):
        try:
            response = requests.head(url)
            if response.status_code == 200:
                size_in_bytes = int(response.headers.get('content-length', 0))
                size_in_mb = size_in_bytes / (1024 * 1024)
                return int(size_in_mb)
            else:
                return -1
        except Exception as e:
            return -1
    