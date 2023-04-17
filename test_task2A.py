import pytest
import requests

BaseURL = 'https://jsonplaceholder.typicode.com'


@pytest.mark.smoke
def test_posts():
    request_url = BaseURL + '/posts/'
    find_no_of_resources(request_url)
    get_resource_data(request_url, 4)
    payload = {
        "userId": 1,
        "id": 5,
        "title": "nesciunt quas odio new",
        "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimusum"
    }
    modify_resource(request_url, payload)
    delete_resource(request_url, payload['id'])
    new_payload = {
        "userId": 11,
        "id": 101,
        "title": "nesciunt quas odio new",
        "body": "repudiandae veniam quaerat sunt sed new"
    }
    create_resource(request_url, new_payload)


def test_comments():
    request_url = BaseURL + '/comments/'
    find_no_of_resources(request_url)
    get_resource_data(request_url, 5)

    payload = {
        "postId": 1,
        "id": 5,
        "name": "vero eaque aliquid doloribus et culpa",
        "email": "Hayden@althea.bizz",
        "body": "harum non quasi et rationetempore iure ex vo"
    }
    modify_resource(request_url, payload)
    delete_resource(request_url, payload['id'])
    new_payload = {
        "postId": 2,
        "id": 101,
        "name": "Tester 1",
        "email": "tester@epam.com",
        "body": "A sample test"
    }
    create_resource(request_url, new_payload)


def test_albums():
    request_url = BaseURL + '/albums/'
    find_no_of_resources(request_url)
    get_resource_data(request_url, 6)
    payload = {
        "userId": 1,
        "id": 6,
        "title": "natus impedit quibusdam illo"
    }
    modify_resource(request_url, payload)
    delete_resource(request_url, payload['id'])
    new_payload = {
        "userId": 10,
        "id": 101,
        "title": "Testing"
    }
    create_resource(request_url, new_payload)


def test_photos():
    request_url = BaseURL + '/photos/'
    find_no_of_resources(request_url)
    get_resource_data(request_url, 7)
    payload = {
        "albumId": 1,
        "id": 8,
        "title": "aut porro officiis laborum",
        "url": "https://via.placeholder.com/600/",
        "thumbnailUrl": "https://via.placeholder.com/150/"
    }
    modify_resource(request_url, payload)
    delete_resource(request_url, payload['id'])
    new_payload = {
        "albumId": 101,
        "id": 5001,
        "title": "Testing",
        "url": "https://via.placeholder.com/test/",
        "thumbnailUrl": "https://via.placeholder.com/testing/"
    }
    create_resource(request_url, new_payload)


def test_todos():
    request_url = BaseURL + '/todos/'
    find_no_of_resources(request_url)
    get_resource_data(request_url, 8)
    payload = {
        "userId": 1,
        "id": 2,
        "title": "quis ut nam facilis",
        "completed": False
    }
    modify_resource(request_url, payload)
    delete_resource(request_url, payload['id'])
    new_payload = {
        "userId": 11,
        "id": 201,
        "title": "Testing title",
        "completed": True
    }
    create_resource(request_url, new_payload)


def test_users():
    request_url = BaseURL + '/users/'
    find_no_of_resources(request_url)
    get_resource_data(request_url, 9)
    payload = {
        "id": 10,
        "name": "Clementina DuBuque",
        "username": "Moriah.Stanton",
        "email": "Padberg@karina.biz",
        "address": {
            "street": "Kattie Turnpike",
            "suite": "Suite 198",
            "city": "Lebsackbury",
            "zipcode": "31428-2261",
            "geo": {
                "lat": "-38.2386",
                "lng": "57.2232"
            }
        },
        "phone": "024-648-3804",
        "website": "ambrose.net",
        "company": {
            "name": "Hoeger LLC",
            "catchPhrase": "Centralized empowering task-force",
            "bs": "target end-to-end models"
        }
    }
    modify_resource(request_url, payload)
    delete_resource(request_url, payload['id'])
    new_payload = {
        "id": 11,
        "name": "Test Engineer1 DuBuque",
        "username": "test.engineer",
        "email": "testeng@epam.com",
        "address": {
            "street": "Kattie Turnpike",
            "suite": "Suite 198",
            "city": "Lebsackbury",
            "zipcode": "31428-2261",
            "geo": {
                "lat": "-38.2386",
                "lng": "57.2232"
            }
        }
    }
    create_resource(request_url, new_payload)


# Helper functions

def find_no_of_resources(request_url):
    posts_response = requests.get(request_url)
    print(posts_response.url)
    print('No.of resources present in the DB is', len(posts_response.json()))


def get_resource_data(request_url, ID):
    query_param = {
        "id": ID
    }
    get_resource_response = requests.get(request_url, params=query_param)
    print('Fetching response data', get_resource_response.json())
    verify_response_data(get_resource_response, query_param)


# def verify_response(response, query_param):
#     assert response.status_code == 200, "Status code doesn't match"
#     response.status_code = requests.codes.ok
#     assert response.json()[0]['id'] == query_param['id']


def modify_resource(request_url, payload):
    response = requests.put(request_url + str(payload['id']), json=payload)
    print(response.url)
    print('Existing resource is modified and the response is', response.json())
    assert response.status_code == 200
    verify_response_data(response, payload)


def verify_response_data(response, payload):
    for key_response in response.json():
        for key_request in payload:
            if key_response == key_request:
                print("value of ", key_response, " is matching in both the response received and request json payload")
                assert response.json()[key_response] == payload[key_request], "Assertion error"


def delete_resource(request_url, parameter):
    response = requests.delete(request_url + str(parameter))
    print("Successfully deleted the given resource from DB")
    assert response.status_code == 200


def create_resource(request_url, payload):
    response = requests.post(request_url, json=payload)
    print('New resource created', response.json())
    assert response.status_code == 201
    verify_response_data(response, payload)

    # assert response.json()['id'] == payload['id'], 'Assertion Error - The ID is not matching'
    # assert response.json()['body'] == payload['body'], 'Assertion Error'
