from flask import Flask, render_template
from flask_cors import CORS
from backend.api import api

app = Flask('GrabEC',
            static_folder="./dist/static",
            template_folder="./dist")
app.config.from_object('backend.config.BaseConfig')

app.register_blueprint(api, url_prefix="/api")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  return render_template("index.html")
