import requests
import json
import pytest
from helper_files.helperfuncs import *
from helper_files.config import *

BASE_URL = pytest.config_url + "/users"

class TestUserCanGetUsers():
  def test_get_user_data(self):
    payload = json.dumps({})

    response = send_get_request_and_store_response(BASE_URL, non_authenticated_header, payload)
    
    assert_json_response_is_of_length(response, 10)  
    assert_response_code_is_200(response)

