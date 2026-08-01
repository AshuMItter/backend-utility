import json
import httpx
import time
from typing import Any, Dict, Optional
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import jsonschema
from dotenv import load_dotenv
import os   
import base64


load_dotenv()  # Load environment variables from .env file

class HTTPXClient:
  def __init__(self, base_url: str, timeout: float = 10.0, max_retries: int = 3):
    self.base_url = base_url
    self.timeout = timeout
    self.max_retries = max_retries
    self.client = httpx.Client(base_url=self.base_url, timeout=self.timeout)
    self.headers = {
         "Accept": "application/json",
         "User-Agent": "Python HTTPX Client"
    }


  def FetchJsonData(self):
    try:
        response = httpx.get(self.base_url, headers=self.headers)
        #response.raise_for_status()  # Raise an exception for HTTP errors
        return response  # Return the JSON data
    except httpx.RequestError as e:
        print(f"An error occurred while requesting {e.request.url!r}.")
    except httpx.HTTPStatusError as e:
        print(f"Error response {e.response.status_code} while requesting {e.request.url!r}.")
    except json.JSONDecodeError:
        print("Failed to decode JSON from the response.")
    return None  # Return None if there was an error


# URL = 'https://raw.githubusercontent.com/AshuMItter/companies_detail/refs/heads/main/companies.json'
# TIMEOUT_SECONDS = 10.0
# MAX_RETRIES = 3


# EXPECTED_SCHEMA = {
    
#     "type": "array",
#     "properties": {
#         "company": {
#             "type": "object",
#             "properties": {
#                 "name": {"type": "string"},
#                 "founded": {"type": "integer"},
#                 "is_active": {"type": "boolean"},
#                 "rating": {"type": "number"},
#                 "headquarters": {
#                     "type": "object",
#                     "properties": {
#                         "city": {"type": "string"},
#                         "state": {"type": "string"},
#                         "country": {"type": "string"},
#                         "zip_code": {"type": "string"}
#                     },
#                     "required": ["city", "state", "country", "zip_code"]
#                 }
#             },
#             "required": ["name", "founded", "is_active", "rating", "headquarters"]
#         }
#     },
#     "required": ["company"]
    
# }

# headers = {

#     "Accept": "application/json",
#     "User-Agent": "Python HTTPX Client"
# }
# response  =   httpx.get(URL, timeout=TIMEOUT_SECONDS, headers=headers)
# print(f"HTTPX Response Status Code: {response.status_code}")




# if response.status_code == 200:
#     data = response.json()
    
#     print(data)   
#     print(jsonschema.validate(instance=data, schema=EXPECTED_SCHEMA))

# _____________________________________ section for POST to Github API _____________________________________________
# new_company = {
#     "name": "QuickTechLondon",
#     "founded": 2034,
#     "is_active": True,
#     "rating": 4.8,
#     "headquarters": {
#         "city": "Yorkshire",
#         "state": "London",
#         "country": "UK",
#         "zip_code": "456768"
#     }
# }



# github_acces = os.environ.get('git_access_token')
# github_url = 'https://api.github.com/repos/AshuMItter/companies_detail/contents/companies.json'
# github_user = "https://api.github.com/user"

# github_headers = {
#     "Authorization": f"Bearer {github_acces}",
#     "Accept": "application/vnd.github.v3+json"
#     }

# #checking the user authentication
# user_response = httpx.get(github_user, headers=github_headers)
# if user_response.status_code == 200:
#     print("GitHub User Authentication Successful")

#     #getcurrent comapnies details from github repo
#     # Get current list
#     r = httpx.get(github_url, headers=headers)
#     data = r.json()
#     companies = json.loads(base64.b64decode(data['content']).decode())
    
#     # Add new company
#     companies.append(new_company)
    
#     # Upload
#     payload = {
#         "message": f"Add {new_company['name']}",
#         "content": base64.b64encode(json.dumps(companies, indent=2).encode()).decode(),
#         "sha": data['sha']
#     }
    
#     r = httpx.put(github_url, headers=github_headers, json=payload)
#     print(r)