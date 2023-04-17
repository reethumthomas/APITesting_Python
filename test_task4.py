import requests

""" https://jsonplaceholder.typicode.com/users
GET call
Validate the below from API response:
That the status code is equal to ‘200’
That there more than ‘3’ users in the list
That one of the users has a name of “Ervin Howell” """


def test_api_users():
    URL = 'https://jsonplaceholder.typicode.com/users'

    get_response = requests.get(URL)
    validate_response(get_response)


def validate_response(response):
    print(type(response.json()))

    assert response.status_code == 200
    response.raise_for_status()
    assert len(response.json()) > 3
    names = []
    given_name = 'Ervin Howell'
    for items in response.json():
        names.append(items['name'])
    if given_name in names:
        print("The given name", given_name, "is present in the response")
        assert True
    else:
        assert False, "The given name is NOT present in the response"


