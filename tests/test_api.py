from processor.api import app
import pytest

@pytest.fixture
def client():
    client = app.test_client()
    yield client

def test_get_points(client):
    res = client.get('/receipts/abcd/points')
    assert res.status_code == 404

def test_process_valid(client):
    receipt_body = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
    }

    res = client.post('/receipts/process', json=receipt_body)

    assert res.status_code == 200

def test_process_no_retailer(client):
    receipt_body = {
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
    }

    res = client.post('/receipts/process', json=receipt_body)

    assert res.status_code == 400

def test_process_no_purchase_date(client):
    receipt_body = {
        "retailer": "Target",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
    }

    res = client.post('/receipts/process', json=receipt_body)

    assert res.status_code == 400

def test_process_no_purchase_time(client):
    receipt_body = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
    }

    res = client.post('/receipts/process', json=receipt_body)

    assert res.status_code == 400

def test_process_no_items(client):
    receipt_body = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "total": "35.35"
    }

    res = client.post('/receipts/process', json=receipt_body)

    assert res.status_code == 400

def test_process_no_total(client):
    receipt_body = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ]
    }

    res = client.post('/receipts/process', json=receipt_body)

    assert res.status_code == 400

def test_process_invalid_date(client):
    receipt_body = {
        "retailer": "Target",
        "purchaseDate": "2022-13-13",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
    }

    res = client.post('/receipts/process', json=receipt_body)

    assert res.status_code == 400

def test_process_invalid_date_format(client):
    receipt_body = {
        "retailer": "Target",
        "purchaseDate": "13/13/2023",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
    }

    res = client.post('/receipts/process', json=receipt_body)

    assert res.status_code == 400

def test_process_invalid_date_type(client):
    receipt_body = {
        "retailer": "Target",
        "purchaseDate": "abcde",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
    }

    res = client.post('/receipts/process', json=receipt_body)

    assert res.status_code == 400

def test_process_invalid_time(client):
    receipt_body = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "25:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
    }

    res = client.post('/receipts/process', json=receipt_body)

    assert res.status_code == 400

def test_process_invalid_time_format(client):
    receipt_body = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "abcde",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
    }

    res = client.post('/receipts/process', json=receipt_body)

    assert res.status_code == 400

def test_process_invalid_item_price(client):
    receipt_body = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "abcdeeee"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
    }

    res = client.post('/receipts/process', json=receipt_body)

    assert res.status_code == 400

def test_process_integer_item_price(client):
    receipt_body = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "5"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12"
            }
        ],
        "total": "35.35"
    }

    res = client.post('/receipts/process', json=receipt_body)

    assert res.status_code == 200

def test_process_invalid_total(client):
    receipt_body = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "invalid total"
    }

    res = client.post('/receipts/process', json=receipt_body)

    assert res.status_code == 400 

def test_process_no_request_body(client):
    receipt_body = {}

    res = client.post('/receipts/process', json=receipt_body)

    assert res.status_code == 400

def test_get_points_valid_id(client):
    receipt_body = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
    }
    post_res = client.post('/receipts/process', json=receipt_body)
    receipt_id = post_res.get_json()['id']
    url = f'/receipts/{receipt_id}/points'

    res = client.get(url)
    assert res.status_code == 200
    assert res.get_json() == {'points' : 28}

def test_get_points_bad_id(client):
    res = client.get('/receipts/abcde/points')

    assert res.status_code == 404

