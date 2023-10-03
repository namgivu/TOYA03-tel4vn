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


if __name__ == '__main__':  #TODO explain later what is this line
  app.run(host='0.0.0.0', port=3000)
  #                       port=run w/ custom port
  #       host  0 0 0 0 to accept request fr anywhere
