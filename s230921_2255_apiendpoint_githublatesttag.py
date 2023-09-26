import requests

#region load GITHUB_API_KEY
import os
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()  # prepare .env in same folder w/ this .py file
GITHUB_API_KEY = os.environ.get('GITHUB_API_KEY')  # ref https://developers.google.com/maps/documentation/geocoding/get-api-key
#endregion load GITHUB_API_KEY


#region make request
headers = {
  'Authorization': f'token {GITHUB_API_KEY}',
}

repo_name =  'python/cpython'  # sample repo here  ref https://g.co/bard/share/772196cf382b  ref https://stackoverflow.com/a/32342630/248616
url       = f'https://api.github.com/repos/{repo_name}/tags'

res = requests.get(url, headers=headers)
print(f'{res.status_code=}')
print(res.json())
#endregion make request
