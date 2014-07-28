import json

title = {
      "payment": {
          "price_paid": 2000000,
          "titles": [
              "TEST198"
          ]
      },
      "property": {
          "address": {
              "house_number": "Flat 11 Queensmere Court",
              "postcode": "SW13 9AT",
              "road": "Verdun Road",
              "town": "London"
          },
          "class_of_title": "absolute",
          "tenure": "leasehold"
      },
      "proprietors": [
          {
              "first_name": "Bob",
              "last_name": "Test"
          },
          {
              "first_name": "Betty",
              "last_name": "Tanker"
          }
      ],
      "title_number": "TEST198"
  }

response_json = json.dumps(title)