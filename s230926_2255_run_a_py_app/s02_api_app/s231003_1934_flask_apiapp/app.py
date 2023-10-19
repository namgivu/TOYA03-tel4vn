from flask import Flask, jsonify  # pip install flask
import requests  # pip install requests


app = Flask(__name__)

@app.route('/')
def index():
  return ''

@app.route('/github/latesttag')
def github_latesttag():
  #      https://api.github.com/repos/:owner/:repo/tags        CAUTION no / attheend
  url = 'https://api.github.com/repos/pyenv/pyenv/tags'

  GITHUB_API_KEY = 'yourkey'
  header         = { 'Authorization': f'Bearer {GITHUB_API_KEY}' }  #TODO it seems github now allow to call /tags endpoint without a github api key
  res = requests.get(url, header)

  d = res.json()
  latest_tag = d[0] ['name']
  return jsonify({'latest_tag': latest_tag})

  '''
  HTTP/1.1 200 OK
  {
      "latest_tag": "v20160726"
  }
  '''


if __name__=='__main__':
  app.run()

'''
$ http http://127.0.0.1:5000
HTTP/1.1 200 OK
'''
