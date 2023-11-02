from flask import Flask, request
from processor.receipt import Receipt
from datetime import date, time

app = Flask(__name__)

point_total = 0
receipts = []

# Endpoint to process receipt. Accepts JSON from request and returns new 
# receipt id
@app.route('/receipts/process', methods=['POST'])
def process():
    request_data = request.get_json(force=True)

    receipt_object = {}

    # Unpack request data into dictionary. If any field is missing,
    # return error code. Also return error code if any field contains
    # a value of unexpected type.
    try:
        if 'retailer' in request_data:
            receipt_object['retailer'] = request_data['retailer']
        else:
            return 400

        if 'purchaseDate' in request_data:
            receipt_object['purchase_date'] = date.fromisoformat(
                request_data['purchaseDate'])
        else:
            return 400

        if 'purchaseTime' in request_data:
            receipt_object['purchase_time'] = time.fromisoformat(
                request_data['purchaseTime'])
        else:
            return 400

        if 'items' in request_data:
            receipt_object['items'] = []

            for i, item in enumerate(request_data['items']):
                receipt_object['items'].append({
                    'short_description': item['shortDescription'],
                    'price': float(item['price'])
                })
        else:
            return 400

        if 'total' in request_data:
            receipt_object['total'] = float(request_data['total'])
        else:
            return 400
    except:
        return 400

    new_receipt = Receipt(receipt_object)
    receipts.append(new_receipt)

    return {"id": new_receipt.id}

# Endpoint takes in a receipt id and returns the amount of points
# the receipt accumulated.
@app.route('/receipts/<id>/points')
def get_points(id):
    receipt = None

    for i, r in enumerate(receipts):
        if r.id == id:
            receipt = r
            break

    if not receipt:
        return 'Unable to find receipt', 404

    return {"points": receipt.points}


if __name__ == '__main__':
    app.run()
