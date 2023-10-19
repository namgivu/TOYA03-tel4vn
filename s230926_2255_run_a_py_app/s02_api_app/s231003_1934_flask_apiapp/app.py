from flask import Flask  # pip install flask


app = Flask(__name__)

@app.route('/')
def index():
  return ''

if __name__=='__main__':
  app.run()

'''
$ http http://127.0.0.1:5000
HTTP/1.1 200 OK
'''
