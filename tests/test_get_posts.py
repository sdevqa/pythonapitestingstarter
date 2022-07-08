import requests
import json
import pytest
import time
from helper_files.helperfuncs import *
from helper_files.config import *

BASE_URL = pytest.config_url + "/posts"

class TestUserCanGetAllPosts():
  @pytest.mark.smoke
  def test_get_posts(self):
    payload = json.dumps({})

    response = send_get_request_and_store_response(BASE_URL, non_authenticated_header, payload)
    
    data = response.json()

    # Example of asserting nested data values.
    assert data[1]['title'] == "qui est esse"

    assert_response_code_is_200(response)

  