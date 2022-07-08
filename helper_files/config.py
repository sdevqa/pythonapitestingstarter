import requests
import json
import pytest
from helper_files.helperfuncs import *

# Code example for handling authentication. Assumes token is returned by API.
def configure_auth_token():
	base_url = pytest.config_url + "/api/v1/login"

	payload = json.dumps({
   "email":"email1@gmail.com",
   "password":"passwordval",
	})

	headers = {
  	 'Content-Type': 'application/json'
	}

	response = requests.request("POST", base_url, headers=headers, data=payload)
	jsonResponse = response.json()
	
	token_val = jsonResponse['token_key_val_to_store']

	return token_val

#header_authcode_val = configure_auth_token()

authenticated_header = {
  'Content-Type': 'application/json',
  #'auth_code': header_authcode_val
}

non_authenticated_header = {
  'Content-Type': 'application/json'
}