from flask import Flask
import os
import requests
import json


app = Flask(__name__)

'''
api = list of endpoints

here our first endpoint
GET /    ->  hi
    /   route
'''
@app.route('/')
def index():
  return 'hi @ index /'


'''
GET /hi  ->  hi
    /hi route
'''
@app.route('/hi')
def          hi():
  return 'hi @ /hi'


@app.route('/demo_requests')
def          demo_requests():
  res =           requests.get('https://api.upcitemdb.com/prod/trial/lookup?upc=190199267961')
  return json.dumps(res.json())


if __name__ == '__main__':  #TODO explain later what is this line
  app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000) )  #TODO param to autoreload code wh changed
  #                       port=run w/ custom port     3000 default port if envvar PORT not avail.
  #       host  0 0 0 0 to accept request fr anywhere
