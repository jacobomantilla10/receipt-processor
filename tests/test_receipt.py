from datetime import date, time
from processor.receipt import Receipt
import pytest

@pytest.fixture
def receipt():
    receipt_body = {
        "retailer": "Target",
        "purchase_date": date.fromisoformat("2022-01-01"),
        "purchase_time": time.fromisoformat("13:01"),
        "items": ([
            {
            "short_description": "Mountain Dew 12PK",
            "price": 6.49
            },{
            "short_description": "Emils Cheese Pizza",
            "price": 12.25
            },{
            "short_description": "Knorr Creamy Chicken",
            "price": 1.26
            },{
            "short_description": "Doritos Nacho Cheese",
            "price": 3.35
            },{
            "short_description": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": 12.00
            }
        ]),
        "total": 35.35
    }

    receipt = Receipt(receipt_body)
    yield receipt

def test_calculate_points(receipt):
    assert receipt.points == 28

def test_calculate_retailer_points_alphanum(receipt):
    assert receipt.calculate_retailer_points('Target') == 6

def test_cualculate_retailer_points_no_alphanum(receipt):
    assert receipt.calculate_retailer_points('&#$#&*^#%#') == 0

def test_calculate_total_round_points_odd_total(receipt):
    assert receipt.calculate_total_round_points(35.35) == 0

def test_calculate_total_round_points_even_total(receipt):
    assert receipt.calculate_total_round_points(35.00) == 50

def test_calculate_total_multiple_points_total_not_multiple(receipt):
    assert receipt.calculate_total_multiple_points(35.35) == 0

def test_calculate_total_multiple_points_total_is_multiple(receipt):
    assert receipt.calculate_total_multiple_points(35.25) == 25

def test_calculate_item_total_points(receipt):
    items = [
            {
            "short_description": "Mountain Dew 12PK",
            "price": 6.49
            },{
            "short_description": "Emils Cheese Pizza",
            "price": 12.25
            },{
            "short_description": "Knorr Creamy Chicken",
            "price": 1.26
            },{
            "short_description": "Doritos Nacho Cheese",
            "price": 3.35
            },{
            "short_description": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": 12.00
            }
        ]
    
    assert receipt.calculate_item_total_points(items) == 10

def test_calculate_item_total_points_no_items(receipt):
    items = []

    assert receipt.calculate_item_total_points(items) == 0

def test_calculate_item_value_points(receipt):
    items = [
            {
            "short_description": "Mountain Dew 12PK",
            "price": 6.49
            },{
            "short_description": "Emils Cheese Pizza",
            "price": 12.25
            },{
            "short_description": "Knorr Creamy Chicken",
            "price": 1.26
            },{
            "short_description": "Doritos Nacho Cheese",
            "price": 3.35
            },{
            "short_description": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": 12.00
            }
        ]
    
    assert receipt.calculate_item_value_points(items) == 6

def test_calculate_item_value_points_no_items(receipt):
    items = []

    assert receipt.calculate_item_value_points(items) == 0

def test_calculate_day_points_odd_day(receipt):
    receipt_date = date.fromisoformat('2022-01-01')

    assert receipt.calculate_day_points(receipt_date) == 6

def test_calculate_day_points_even_day(receipt):
    receipt_date = date.fromisoformat('2022-02-02')

    assert receipt.calculate_day_points(receipt_date) == 0

def test_calculate_time_points_time_in_range(receipt):
    receipt_time = time.fromisoformat('14:01')

    assert receipt.calculate_time_points(receipt_time) == 10

def test_calculate_time_points_time_not_in_range(receipt):
    receipt_time = time.fromisoformat('13:01')

    assert receipt.calculate_time_points(receipt_time) == 0
