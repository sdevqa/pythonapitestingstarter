import requests
import json
import pytest
import time
from helper_files.helperfuncs import *
from helper_files.config import *

BASE_URL = pytest.config_url + "/posts/1"

class TestUserCanGetSinglePostById():
  def test_get_specific_post_by_id(self):
    payload = json.dumps({})

    response = send_get_request_and_store_response(BASE_URL, non_authenticated_header, payload)
    
    assert_value_is_present_in_response(response, "userId", 1)
    assert_response_code_is_200(response)

  