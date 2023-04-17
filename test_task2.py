import json
import pytest
import requests
from jsonschema import validate

base_url = 'https://jsonplaceholder.typicode.com'


@pytest.fixture
def request_url():
    API_endpoint = base_url + '/posts'
    return API_endpoint


"""1. To find the number of resources"""


def test_find_no_of_resources(request_url):
    posts_response = requests.get(request_url)
    print(posts_response.url)
    print(len(posts_response.json()))


"""2. For each type of resource, Get a specific resource data  and i. verify the response code and ii. Verify the
response body """


def test_get_resource_from_post(request_url):
    get_resource_endpoint = request_url
    query_param = {
        "id": 4
    }
    get_resource_response = requests.get(get_resource_endpoint, params=query_param)
    print(get_resource_response.json())
    assert get_resource_response.status_code == 200, "Status code doesn't match"
    get_resource_response.status_code = requests.codes.ok

    # to validate the response body
    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}

        }
    }

    validate(instance=get_resource_response.json()[0], schema=schema)
    assert get_resource_response.json()[0]['id'] == query_param['id']


"""    b. Modify a specific resource data
        i. verify the response code
        ii. Verify the response body"""


def test_modify_resource_data(request_url):
    resource_endpoint = request_url + '/5'
    payload = {
        "userId": 1,
        "id": 5,
        "title": "nesciunt quas odio new",
        "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus "
                "esse voluptatibus quis\nest aut tenetur dolor neque"
    }
    modified_response = requests.put(resource_endpoint, data=payload)
    assert modified_response.status_code == 200
    assert modified_response.json()['title'] == "nesciunt quas odio new"


"""    c. Delete a specific resource 
        i. verify the response code
        ii. Verify the response body """


def test_delete_resource(request_url):
    resource_endpoint = request_url + '/2'

    delete_response = requests.delete(resource_endpoint)
    print("Resource successfully deleted", delete_response.json())
    assert delete_response.status_code == 200


""" d. Create your own resource 
        i. verify the response code
        ii. Verify the response body """


@pytest.mark.smoke
def test_create_resource(request_url):
    endpoint = request_url
    payload = {
        "userId": 11,
        "id": 101,
        "title": "nesciunt quas odio new",
        "body": "repudiandae veniam quaerat sunt sed new"
    }
    create_response = requests.post(endpoint, json=payload)
    print(create_response.json())
    assert create_response.status_code == 201
    assert create_response.json()['id'] == payload['id'], 'Assertion Error'
