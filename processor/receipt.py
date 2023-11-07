import math
import re

class Receipt:
    # Initializes the receipt object from the JSON object
    def __init__(self, receipt_object):
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

        total_points += self.calculate_retailer_points(retailer)
        total_points += self.calculate_total_round_points(total)
        total_points += self.calculate_total_multiple_points(total)
        total_points += self.calculate_item_total_points(items)
        total_points += self.calculate_item_value_points(items)
        total_points += self.calculate_day_points(purchase_date)
        total_points += self.calculate_time_points(purchase_time)

        return total_points
    
    def calculate_retailer_points(self, retailer):
        retailer_alphanumeric = re.sub('[^0-9a-zA-Z]', '', retailer)
        return len(retailer_alphanumeric)
    
    def calculate_total_round_points(self, total):
        if total % 1 == 0.0:
            return 50
        return 0
    
    def calculate_total_multiple_points(self, total):
        if (total / 0.25) % 1 == 0.0:
            return 25
        return 0
    
    def calculate_item_total_points(self, items):
        return (len(items) // 2) * 5
    
    def calculate_item_value_points(self, items):
        points = 0
        for i in range(len(items)):
            item = items[i]
            if len(item['short_description'].strip()) % 3 == 0:
                points += math.ceil(item['price'] * 0.2)
        return points
    
    def calculate_day_points(self, date):
        if date.day % 2 != 0:
            return 6
        return 0
    
    def calculate_time_points(self, time):
        if time.hour >= 14 and time.hour < 16:
            if time.minute != 0:
                return 10
        return 0
    

    
