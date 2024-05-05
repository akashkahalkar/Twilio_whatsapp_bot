from flask import Blueprint, jsonify, request
import re
from downloader.teradownloader import TeraDownloader
from local_downloader.downloader import VideoDownloader

tester = Blueprint('tester', __name__, url_prefix='/test')

@tester.route('/', methods=['POST', 'GET'])
def extract_urls():
    raw = str(request.data)
    url_pattern = r"https?://\S+"

# Find all URLs in the text
    urls = re.findall(url_pattern, raw) 
    clean = []
    for url in urls:
        cleaned_url = re.sub(r'(\\n\d*|\\n\')+?$', '', url)
        clean.append(cleaned_url)
    
    data = {
        "urls": clean
    }
    dlinks = TeraDownloader().bulk_fetch_download_links(clean)
    VideoDownloader().download_videos(dlinks)
    return jsonify(data)


@tester.route('/bulk', methods=['POST', 'GET'])
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

        data = {
            "urls": dlinks
        }
        return jsonify(data)
    else:
        return "Error"

# Find all URLs in the text
    
