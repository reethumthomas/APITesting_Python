import pytest
import requests

"""Use the documentation listed at https://dummy.restapiexample.com/ to perform the task below.
1. Get the list of all employees. 
    a. verify the count of employees. """

BASE_URL = 'https://dummy.restapiexample.com/'
count_of_default_employees = 24
request_body = {"employee_name": "Tester 1", "employee_salary": "250000", "employee_age": "26"}


def test_get_employees():
    api_endpoint = 'api/v1/employees'

    response = requests.get(BASE_URL + api_endpoint)
    print(response.url)
    print(response.json())
    assert len(response['data']) == count_of_default_employees


"""2. Create an employee
    a. verify that employee is created successfully.
    b. verify the count of employees is increased by +1 """


@pytest.fixture
def test_create_employee():
    api_endpoint = 'api/v1/create'

    response = requests.post(BASE_URL + api_endpoint, json=request_body)
    print(response.url)
    print(response.status_code)
    assert response.status_code == 200
    assert response['message'] == "Successfully! Record has been added."
    assert len(response.json()['data']) == count_of_default_employees + 1
    return response


""" 3. get the details of the employee created in step 2
    a. verify all the details given in step2 """


def test_validate_new_employee(test_create_employee):
    response = test_create_employee.json()
    # validate employee details
    # response = {
    #     "status": "success",
    #     "data": {
    #         "name": "Tester 1",
    #         "salary": "250000",
    #         "age": "26",
    #         "id": 4466
    #     },
    #     "message": "Successfully! Record has been added."
    # }

    validate_key_value(response, 'employee_name', 'Tester 1')
    validate_key_value(response, 'employee_salary', '250000')
    validate_key_value(response, 'employee_age', '26')


def validate_key_value(response, key, value):
    for k, v in response['data'].items():
        if k == key:
            assert v == value


"""4. update the details of the employee update the salary and age
    a. verify the update is successful.  """


def test_update_empolyee(test_create_employee):
    id = test_create_employee.json()['data']['id']
    # id = 444
    payload = {
        "employee_salary": "280000",
        "employee_age": "28"
    }
    endpoint = BASE_URL + 'public/api/v1/update/' + str(id)
    response = requests.put(endpoint, data=payload)
    print(response.json())


""" 6. delete the employee created in step 2.
    a. verify the delete is successful.
    b. verify the total list of employees is decreased by -1 """


def test_delete_employee(test_create_employee):
    id = test_create_employee.json()['data']['id']
    endpoint = BASE_URL + 'public/api/v1/delete/' + str(id)
    print(endpoint)
    response = requests.delete(endpoint)
    assert response.status_code == 200
    assert response.json()['message'] == 'Successfully! Record has been deleted'
    assert len(response.json()['data']) == count_of_default_employees
    assert response.encoding == 'utf-8'
    assert response.ok is True
