from flask import Flask
from .shortcuts.routes import shortcuts
from .twilio_webhook.routes import twilio_api

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(shortcuts)
    app.register_blueprint(twilio_api)

    @app.route('/')
    def welcome():
        return "<B>Ahoy, landlubber!</B> <br><p>What be yer business sailin' these treacherous seas?<p>"
    return app

