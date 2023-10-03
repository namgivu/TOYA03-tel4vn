from flask import Flask
import os
import requests
import json
#
from dotenv import load_dotenv  # pip install python-dotenv



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


#region call github api to list tags
@app.route('/github/pyenv/tag')
def          github_pyenv_tag():
  load_dotenv()
  GITHUB_API_KEY = os.environ.get('GITHUB_API_KEY')  # ref https://developers.google.com/maps/documentation/geocoding/get-api-key
  headers = {
    'Authorization': f'Bearer {GITHUB_API_KEY}',
  }

  owner_reponame =  'pyenv/pyenv'  # Nam G VU 's favourite public github repo
  url            = f'https://api.github.com/repos/{owner_reponame}/tags'

  res = requests.get(url, headers=headers)
  return json.dumps(res.json())

#endregion call github api to list tags


# w/ this below block, we could debug run flask apiapp w/ Pycharm
if __name__ == '__main__':  #TODO explain later what is this line
  #  .run                                                  , debug=True to autoreload code wh changed
  app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000), debug=True)
  #                       port=run w/ custom port     3000 default port if envvar PORT not avail.
  #       host  0 0 0 0 to accept request fr anywhere
