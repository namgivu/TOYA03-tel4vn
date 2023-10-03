from flask import Flask

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
def hi():
  return 'hi @ /hi'
