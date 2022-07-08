import requests
import json
import pytest
from helper_files.helperfuncs import *
from helper_files.config import *

BASE_URL = pytest.config_url + "/api/v1/login"

class TestUserCanLogin():
  def test_user_can_login(self):
    good_payload = json.dumps({
      "email":"email1@email.com",
      "password":"passwordval",
    })
    
    response = send_post_request_and_store_response(BASE_URL, non_authenticated_header, good_payload)
  
    assert_response_code_is_200(response)

  def test_400_bad_request_response(self):
    bad_payload = json.dumps({
      "email":"email1@email.com",
      "password":"wrongpasswordval",
    })

    response = send_post_request_and_store_response(BASE_URL, non_authenticated_header, bad_payload)
    assert_response_code_is_400(response)
  
