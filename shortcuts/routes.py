from flask import Blueprint, jsonify
from flask import request
from downloader.teradownloader import TeraDownloader
from handler import URLHandler
import validators
import re

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

@shortcuts.route('/bulk', methods=['POST', 'GET'])
def get_urls():
    request_json = request.get_json()

# Check if 'data' key exists in the JSON and if the request has JSON data
    if request_json and 'data' in request_json:
        url_pattern = r"https?://\S+"
        response_raw = str(request_json['data'])
        urls = re.findall(url_pattern, response_raw) 
        clean = []
        for url in urls:
            cleaned_url = re.sub(r'(\\n\d*|\\n\')+?$', '', url)
            clean.append(cleaned_url)
        
        dlinks = TeraDownloader().bulk_fetch_download_links(clean)
        #VideoDownloader().download_videos(dlinks)

        data = {
            "urls": dlinks
        }
        return jsonify(data)
    else:
        return "Error"





