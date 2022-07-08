import json
import requests
from helper_files.config import *

def pretty_print_json_response(r):
    json_object = json.loads(r.content)
    json_formatted_str = json.dumps(json_object, indent=2)
    print(json_formatted_str)

def assert_response_code_is_200(res):
    assert res.status_code == 200, "Response Code is not a 200."
    print("Sucessfully asserted Response Code is 200.")

def assert_response_code_is_400(res):
    assert res.status_code == 400, "Response Code is not a 400."
    print("Successfully asserted Response Code is 400")

def assert_response_code_is_201(res):
    assert res.status_code == 201, "Response Code is not a 201."
    print("Sucessfully asserted Response Code is 201.")

def assert_response_code_is_401(res):
    assert res.status_code == 401, "Response Code is not a 401."
    print("Sucessfully asserted Response Code is 401.")

def assert_value_is_present_in_response(data, key, assert_val):
    data = data.json()
    
    assert data[key] == assert_val
    print("Sucessfully asserted " + str(key) + " with value of " + str(assert_val) + " is present")

def assert_json_response_is_of_length(data, assert_num):
    data = data.json()

    assert len(data) >= assert_num, "Number not as expected."

def send_get_request_and_store_response(base_url, headers, payload):
    res = requests.request("GET", base_url, headers=headers, data=payload)

    return res

def send_post_request_and_store_response(base_url, headers, payload):
    res = requests.request("POST", base_url, headers=headers, data=payload)

    return res

def send_put_request_and_store_response(base_url, headers, payload):
    res = requests.request("PUT", base_url, headers=headers, data=payload)

    return res

def send_patch_request_and_store_response(base_url, headers, payload):
    res = requests.request("PATCH", base_url, headers=headers, data=payload)

    return res