from flask import Flask, abort
from markupsafe import escape
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)

app.config['ELASTIC_APM'] = {
  # Set required service name. Allowed characters:
  # a-z, A-Z, 0-9, -, _, and space
  'SERVICE_NAME': 'flask-app-1',

  # Use if APM integration requires a token
  'SECRET_TOKEN': '',

  # Set custom APM integration host and port (default: http://localhost:8200)
  'SERVER_URL': 'http://localhost:8200',
}

apm = ElasticAPM(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/path/<param>")
def path(param):
    return f'path {escape(param)}'

@app.route("/demo")
def demo():
    return "<p>Demo page</p>"


@app.route("/error")
def error_route():
    abort(500)
    return "Error page"

@app.errorhandler(500)
def page_not_found(e):
    return "Error page", 500
