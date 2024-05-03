from flask import Blueprint
from flask import request
from handler import URLHandler
import validators

shortcuts = Blueprint('shortcuts', __name__, url_prefix='/shortcuts')

@shortcuts.route('/', methods=['GET'])
def get_download_link():
    error = "❌ *Arrr! I be at yer service, matey! Unfortunately,* \n Check ya links aye! 🏴‍☠️"
    input_url = str(request.values.get("Body"))
    if not validators.url(input_url):
        return error
    download_link = URLHandler().handle(input_url)
    if download_link is None:
        return error
    return str(download_link)






