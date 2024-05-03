from flask import Flask
from shortcuts.routes import shortcuts
from twilio_webhook.routes import twilio_api
import os

app = Flask(__name__)
app.register_blueprint(shortcuts)
app.register_blueprint(twilio_api)

@app.route('/', methods=['GET', 'POST'])
def _welcome():
    return "<B>Ahoy, landlubber!</B> <br><p>What be yer business sailin' these treacherous seas?<p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ.get("PORT", 5000),use_reloader=True,threaded=True)
