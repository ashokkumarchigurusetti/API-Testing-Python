import requests

def test_create_user():
    payload = {
        "name": "Ashok",
        "job": "QA Engineer"
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=payload
    )

    assert response.status_code == 201