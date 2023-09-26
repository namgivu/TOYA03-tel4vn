import requests

#region load GITHUB_API_KEY
import os
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()
GITHUB_API_KEY = os.environ.get('GITHUB_API_KEY')  # ref https://developers.google.com/maps/documentation/geocoding/get-api-key
#endregion load GITHUB_API_KEY


#region make request
headers = {
  'Authorization': f'token {GITHUB_API_KEY}',
}

repo_name =  'namgivu/TOYA03-tel4vn'  #NOTE use repo that belong to you ie you are repo owner <-- only onwer can create new tag
url       = f'https://api.github.com/repos/{repo_name}/tags'

res = requests.get(url, headers=headers)
print(f'{res.status_code=}')
print(res.json())

'''
[{'name': 'v0', 'zipball_url': 'https://api.github.com/repos/namgivu/TOYA03-tel4vn/zipball/refs/tags/v0', 'tarball_url': 'https://api.github.com/repos/namgivu/TOYA03-tel4vn/tarball/refs/tags/v0', 'commit': {'sha': 'd2a218fede9d827b92ccd402299bd87ebe45ccdb', 'url': 'https://api.github.com/repos/namgivu/TOYA03-tel4vn/commits/d2a218fede9d827b92ccd402299bd87ebe45ccdb'}, 'node_id': 'REF_kwDOKYhA4qxyZWZzL3RhZ3MvdjA'}]
'''
d = res.json()
lastest_tag_d = d[0]
print(f'''\nlatest tag\n{lastest_tag_d['name']}''')
#endregion make request
