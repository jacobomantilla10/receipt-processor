import uuid
import math
import re

class Receipt:
    # Initializes the receipt object from the JSON object
    def __init__(self, receipt_object):
        self.id = str(uuid.uuid1())
        self.points = self.calculate_points(receipt_object)

    def __str__(self):
        return f'Receipt id {self.id} contains {self.points} points'
    
    # Calculates and returns the total amount of points in receipt
    def calculate_points(self, receipt_object):
        retailer = receipt_object['retailer']
        purchase_date = receipt_object['purchase_date']
        purchase_time = receipt_object['purchase_time']
        items = receipt_object['items']
        total = receipt_object['total']

        # Calculate total receipt points
        total_points = 0

        retailer_alphanumeric = re.sub('[^0-9a-zA-Z]+', '', retailer)
        total_points += len(retailer_alphanumeric)

        if total % 1 == 0.0:
            total_points += 50

        if (total / 0.25) % 1 == 0.0:
            total_points += 25

        total_points += (len(items) // 2) * 5

        for i in range(len(items)):
            item = items[i]
            if len(item['short_description'].strip()) % 3 == 0:
                total_points += math.ceil(item['price'] * 0.2)
        
        if purchase_date.day % 2 != 0:
            total_points += 6

        if purchase_time.hour >= 14 and purchase_time.hour < 16:
            if purchase_time.minute != 0:
                total_points += 10

        return total_points