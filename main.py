from flask import Flask
from shortcuts.routes import shortcuts
from twilio_webhook.routes import twilio_api
import os

app = Flask(__name__)
app.register_blueprint(shortcuts)
app.register_blueprint(twilio_api)

@app.route('/', methods=['GET', 'POST'])
def _welcome():
    return _run_validation_check()

def _run_validation_check():
    download_domain = os.environ.get("DOWNLOAD_DOMAIN")
    fast_download_domain = os.environ.get("FAST_DOWNLOAD_DOMAIN")
    base_url = os.environ.get("TERA_BASE_URL")
    key = os.environ.get("TERA_KEY")
    link_param = os.environ.get("LINK_PARAM")

    values = [download_domain, fast_download_domain, base_url, key, link_param]
    variable_names = ['download_domain', 'fast_download_domain', 'base_url', 'key', 'link_param']

    for name, value in zip(variable_names, values):
        if value is None:
            return (f"validation failed for '{name}' ")
    return "validation check passed!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ.get("PORT", 5000),use_reloader=True,threaded=True)
