from flask import Flask
import json


app = Flask(__name__)


@app.route('/')
def index():
  return json.dumps({})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=9000, debug=True)
