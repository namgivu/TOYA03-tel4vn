#region load GOOGLE_API_KEY
import os
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')  # ref https://developers.google.com/maps/documentation/geocoding/get-api-key
#endregion load GOOGLE_API_KEY

#region make request
"""
sample request via postman
https://www.postman.com/namgivu/workspace/tel4vn-toda/request/718205-e609de4f-5452-4717-8c30-2447859932f4
"""
import requests

url = 'https://maps.googleapis.com/maps/api/place/details/json?key=AIzaSyBgDiD_dRG_h-EI1420bnF0DQ3qikeYyok&place_id=ChIJNyqLpYUpdTERDwrREkcTGmA&fields=name'

res = requests.get(url)

print(res.json())
#endregion make request
