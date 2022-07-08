import requests
import json
import pytest
import time
from helper_files.helperfuncs import *
from helper_files.config import *

BASE_URL = pytest.config_url + "/posts"

class TestUserCanCreatePost():
  def test_create_post(self):
    payload = json.dumps({ 'title': 'foo','body': 'bar','userId': 1 })

    response = send_post_request_and_store_response(BASE_URL, non_authenticated_header, payload)
    
    assert_response_code_is_201(response)

  