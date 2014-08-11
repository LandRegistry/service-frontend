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
      "title_number": "TEST198",
      "charges": [
          {
              "charge_date": "2014-08-11",
              "chargee_address": "a house",
              "chargee_name": "trp ltd",
              "chargee_registration_number": "12345"
          }
    ]
  }

title_no_charge = {
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
response_without_charge = json.dumps(title_no_charge)
