import requests
import json
import pytest
import time
from helper_files.helperfuncs import *
from helper_files.config import *

BASE_URL = pytest.config_url + "/posts"

# Modify auth code in config.py and remove code comments. Authenticated endpoints will then work by passing in the authenticated_header into each request.
class TestUserCanCreatePost():
  def test_create_post(self):
    payload = json.dumps({ "name":"My first post","body":"Lorem ipsum dolar."})

    response = send_post_request_and_store_response(BASE_URL, authenticated_header, payload)
    
    assert_response_code_is_200(response)

   def test_400_bad_request_for_create_post(self):
    payload = json.dumps({ "name":"","body":""})

    response = send_post_request_and_store_response(BASE_URL, authenticated_header, payload)
    assert_response_code_is_400(response)

  def test_401_response_for_create_post(self):
    payload = json.dumps({ "name":"My first post","body":"Lorem ipsum dolar."})

    # Non auth header will result in a 401.
    response = send_post_request_and_store_response(BASE_URL, non_authenticated_header, payload)
    
    assert_response_code_is_401(response)
