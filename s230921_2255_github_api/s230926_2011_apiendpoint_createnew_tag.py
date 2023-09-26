import requests
import datetime


#region load GITHUB_API_KEY
import os
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()
GITHUB_API_KEY = os.environ.get('GITHUB_API_KEY')  # ref https://developers.google.com/maps/documentation/geocoding/get-api-key
#endregion load GITHUB_API_KEY

owner_reponame = 'namgivu/TOYA03-tel4vn'  #NOTE use repo that belong to you ie you are repo owner <-- only onwer can create new tag

headers = {
  'Authorization': f'Bearer {GITHUB_API_KEY}',
}

#region get :lastest_tag
url_GET = f'https://api.github.com/repos/{owner_reponame}/tags'

res = requests.get(url_GET, headers=headers)
print(f'{res.status_code=}')
print(res.json())

'''
[{'name': 'v0', 'zipball_url': 'https://api.github.com/repos/namgivu/TOYA03-tel4vn/zipball/refs/tags/v0', 'tarball_url': 'https://api.github.com/repos/namgivu/TOYA03-tel4vn/tarball/refs/tags/v0', 'commit': {'sha': 'd2a218fede9d827b92ccd402299bd87ebe45ccdb', 'url': 'https://api.github.com/repos/namgivu/TOYA03-tel4vn/commits/d2a218fede9d827b92ccd402299bd87ebe45ccdb'}, 'node_id': 'REF_kwDOKYhA4qxyZWZzL3RhZ3MvdjA'}]
'''
d = res.json()
lastest_tag = d[0]['name']
print(f'''\nlatest tag\n{lastest_tag}''')
#endregion get :lastest_tag

#region increate tag +1
'''
Create new tag, by increase the latest tag by 1.
■ Example: latest tag: v2 -> new tag will be v3
'''
version_num = lastest_tag[1:]
#           =            [1:len()-1]

version_num  = int(version_num)
version_num += 1

new_tag = f'v{version_num}'

#region call github api endpoint to create :new_tag
'''
ref https://docs.github.com/en/rest/git/tags?apiVersion=2022-11-28#create-a-tag-object
'''

url_newtag = f'https://api.github.com/repos/{owner_reponame}/git/tags'

commit_hash="57debfa8127e60b8386f8ee53752cb056109098f"  #TODO call shutil to call git command to get latest commit of main - currently get commit 0th ie initialcommit hash

res = requests.post(
  url_newtag,
  headers = headers,

  json = {
    "tag"     : new_tag,
    "message" : "create new tag",

    "object"  : commit_hash,
    "type"    : "commit",

    # we can skip :tagger field  ref Bard > Removed the tagger key from the tag_details dictionary. This is no longer required, as it is automatically populated by the GitHub API.  ref https://g.co/bard/share/a88045629b30
    # "tagger":{
    #   "name"  : "Nam G VU",
    #   "email" : "namgivu@gmail.com",
    #   # "date"  : str(datetime.datetime.now()),  # left undefined to have it auto filled
    # }
  }
)
print()
print(res.status_code)
print(res.json())
'''
# result 00
{
  'message'           : 'Invalid request.\n\n"type" wasn\'t supplied.', 
  'documentation_url' : 'https://docs.github.com/rest/git/tags#create-a-tag-object'
}
'''

'''
# result 01
201
{'node_id': 'TA_kwDOKYhA4toAKDYzZGEzZWUxMmYzMjBhZWU1NGYwZTA2NTNlNzFhNDFmYzFkZjQ1ZDM', 'sha': '63da3ee12f320aee54f0e0653e71a41fc1df45d3', 'url': 'https://api.github.com/repos/namgivu/TOYA03-tel4vn/git/tags/63da3ee12f320aee54f0e0653e71a41fc1df45d3', 'tagger': {'name': 'Nam G VU', 'email': 'namgivu@gmail.com', 'date': '2023-09-26T14:06:16Z'}, 'object': {'sha': '57debfa8127e60b8386f8ee53752cb056109098f', 'type': 'commit', 'url': 'https://api.github.com/repos/namgivu/TOYA03-tel4vn/git/commits/57debfa8127e60b8386f8ee53752cb056109098f'}, 'tag': 'v1', 'message': 'create new tag', 'verification': {'verified': False, 'reason': 'unsigned', 'signature': None, 'payload': None}}
> 'verification': {'verified': False, 'reason': 'unsigned'
'''

#TODO how to get newtag really created?
#endregion call github api endpoint to create :new_tag

#endregion increate tag +1
