from app.app import app

import pytest
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        with app.test_client() as client:
            #The client will raise warning message in flask 1.1, it won't show after flask 2
            yield client

@pytest.fixture
def data(client):
    #post a data for update and delete
    test_data = json.dumps({           
        'name': 'eat breakfast'
    })
    res = client.post('/task', data=test_data)
    data = json.loads(res.data)
    yield data

def test_database_configured():
    assert app.config['SQLALCHEMY_DATABASE_URI']

def test_get_method(client):
    res = client.get('/task')
    assert res.status_code == 200

def test_post_method(client):
    #test no data case
    res = client.post('/task')
    assert res.status_code == 400

def test_put_method(client, data):
    test_data = json.dumps({           
        'name': 'eat lunch',
        'status': 1,
    })
    res = client.put(f'/task/{data["result"]["id"]}', data=test_data)
    res_status = json.loads(res.data)['status']
    res = client.delete(f'/task/{data["result"]["id"]}')
    assert res.status_code == 200
    #check data updated or not
    assert res_status == 1

def test_delete_method(client, data):
    res = client.delete(f'/task/{data["result"]["id"]}')
    assert res.status_code == 200

    #check data really deleted
    res = client.get('/task')
    task_list = json.loads(res.data)['result']
    is_exist = False
    for task in task_list:
        if task['id'] == data["result"]["id"]:
            is_exist = True
    assert is_exist == False
