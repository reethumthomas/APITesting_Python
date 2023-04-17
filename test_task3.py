import requests

Base_URL = 'https://petstore.swagger.io/v2/pet'

""" Create a PET using the POST call from http://petstore.swagger.io/#/
once the pet is created write the test cases using REST assured for the below calls
https://petstore.swagger.io/v2/pet/12345
GET call
Validate the below from API response:
That the status code is equal to ‘200’
That the content type is ‘application/json’
That if the pet is a ‘dog’
That its name is ‘snoopie’
That its current status is ‘pending’ """


def test_create_pet():
    json_payload = {
        "id": 12345,
        "category": {
            "id": 1,
            "name": "dog"
        },
        "name": "snoopie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "pending"
    }

    response = requests.post(Base_URL, json=json_payload)
    print(response.status_code)
    print(response.json())


def test_validate_pet():
    endpoint = Base_URL + '/12345'
    response = requests.get(endpoint)
    print(response.headers['content-type'])

    validate_status_code(response)
    validate_header(response, 'content-type')
    validate_values(response)

    assert response.json()['category']['name'] == 'dog'
    assert response.json()['name'] == 'snoopie'
    assert response.json()['status'] == 'pending'


def validate_status_code(response):
    assert response.status_code == 200


def validate_header(response, header):
    assert response.headers.get(header) == 'application/json'


def validate_values(response):
    for key, value in response.json().items():
        if key == 'category':
            assert value['name'] == 'dog'
        elif key == 'name':
            assert value == 'snoopie'
        elif key == 'status':
            assert value == 'pending'

