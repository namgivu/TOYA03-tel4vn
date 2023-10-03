from flask import Flask, request
import json
#
from dotenv import load_dotenv
import os
import requests


app = Flask(__name__)


@app.route('/')
def index():
  return json.dumps({})

@app.route('/tag')
def          tag():
  '''
  ?repo=<repo-name>  <-- request.args  ref https://stackoverflow.com/a/11774434/248616
  '''
  owner_reponame = request.args.get('repo')

  #region    call github api /tags
  load_dotenv()
  GITHUB_API_KEY = os.environ.get('GITHUB_API_KEY')  # ref https://developers.google.com/maps/documentation/geocoding/get-api-key
  headers = {
    'Authorization': f'Bearer {GITHUB_API_KEY}',
  }

  url = f'https://api.github.com/repos/{owner_reponame}/tags'

  res = requests.get(url, headers=headers)
  d   = res.json()

  latest_tag = d[0]['name']
  #endregion call github api /tags

  return json.dumps({
    'latest_tag': latest_tag,
  })

#endregion call github api to list tags



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=9000, debug=True)
