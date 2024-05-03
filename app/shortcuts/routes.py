from flask import Blueprint
from flask import request
from app.handler import URLHandler

shortcuts = Blueprint('shortcuts', __name__, url_prefix='/shortcuts')

@shortcuts.route('/', methods=['GET'])
def get_download_link():
    input_url = str(request.values.get("Body"))
    download_link = URLHandler().handle(input_url)
    if download_link is None:
        return "Failed to fetch!, link is broken!"
    return str(download_link)