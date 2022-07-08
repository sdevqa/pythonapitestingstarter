import requests
import json
import pytest
import time
from helper_files.helperfuncs import *
from helper_files.config import *

BASE_URL = pytest.config_url + "/posts/1"

class TestUserCanUpdatePosts():
  @pytest.mark.smoke
  def test_update_post(self):
    payload = json.dumps({'id':1, 'title': 'foo', 'body': 'bar','userId': 1})

    response = send_put_request_and_store_response(BASE_URL, non_authenticated_header, payload)
    
    assert_response_code_is_200(response)

  