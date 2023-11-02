# Receipt Processor

A webservice that fulfils the API documented below. Built using Flask. Does not include persistent storage
so data does not survive the application stopping.

## API Specification
### Endpoint: Process Receipts

* Path: `/receipts/process/`
* Method: `POST`
* Payload: Receipt JSON
* Response: JSON containing an id for the receipt

#### Example of valid Receipt JSON

```json
{
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
```
### Endpoint: Get Points

* Path: `/receipts/{id}/points`
* Method: `GET`
* Response: A JSON object containing the number of points awarded.

## Rules that define amount of points awarded to a single receipt:

* One point for every alphanumeric character in the retailer name.
* 50 points if the total is a round dollar amount with no cents.
* 25 points if the total is a multiple of `0.25`.
* 5 points for every two items on the receipt.
* If the trimmed length of the item description is a multiple of 3, multiply the price by `0.2` and round up to the nearest integer. The result is the number of points earned.
* 6 points if the day in the purchase date is odd.
* 10 points if the time of purchase is after 2:00pm and before 4:00pm.

## How to Run Receipt Processor

Clone the repository and navigate to folder containing code.

Afterwards, build the Docker image from the Dockerfile:
```
docker build -t receipt-processor
```

Now run a new docker container named receipt-processor
```
docker run --name receipt-processor -d -p 5000:5000 receipt-processor
```

After a few seconds, our app should be running in localhost at port 5000

We can use curl, postman, or any other tool to interact with the api.
