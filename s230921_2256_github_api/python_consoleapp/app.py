import os
from dotenv import load_dotenv  # pip install python-dotenv
#
import requests  # pip install requests <-- prepare .venv

'''
ref https://docs.github.com/en/rest/git/tags?apiVersion=2022-11-28  ref2 https://rapidapi.com/blog/directory/github-git-tags/#:~:text=The%20GitHub%20Git%20Tags%20API,to%20access%20to%20this%20API.
https://api.github.com/repos/:owner/:repo/tags/
https://api.github.com/repos/pyenv/pyenv/tags/
'''

#               url                                header
# requests.get('url -> github api endpoint', 'todo header w/ github apikey')


#      https://api.github.com/repos/:owner/:repo/git/tags/   WRONG
#      https://api.github.com/repos/:owner/:repo/tags        CAUTION no / attheend
url = 'https://api.github.com/repos/pyenv/pyenv/tags'


load_dotenv()
GITHUB_API_KEY = os.environ.get('GITHUB_API_KEY')
header         = { 'Authorization': f'Bearer {GITHUB_API_KEY}' }  #TODO it seems github now allow to call /tags endpoint without a github api key
res = requests.get(url, header)

# print(res.json())

d = res.json()
latest_tag = d[0] ['name']
print(f'{latest_tag=:>}')
