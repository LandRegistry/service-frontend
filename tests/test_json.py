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
      "extent": {
          "crs": {
              "properties": {
                  "name": "urn:ogc:def:crs:EPSG:27700"
              },
              "type": "name"
          },
          "geometry": {
              "coordinates": [
                  [
                      [
                          [
                              530857.01,
                              181500
                          ],
                          [
                              530857,
                              181500
                          ],
                          [
                              530857,
                              181500
                          ],
                          [
                              530857,
                              181500
                          ],
                          [
                              530857.01,
                              181500
                          ]
                      ]
                  ]
              ],
              "type": "MultiPolygon"
          },
          "properties": {},
          "type": "Feature"
      },
      "charges": [
          {
              "charge_date": "2014-08-11",
              "chargee_address": "a warehouse",
              "chargee_name": "compone",
              "chargee_registration_number": "12345"
          },
          {
              "charge_date": "2014-08-12",
              "chargee_address": "a barn",
              "chargee_name": "comptwo",
              "chargee_registration_number": "56666"
          }
      ],
      "easements": [
          {
              "easement_description": "easement one",
              "easement_geometry": {
                  "crs": {
                      "properties": {
                          "name": "urn:ogc:def:crs:EPSG:27700"
                      },
                      "type": "name"
                  },
                  "geometry": {
                      "coordinates": [
                          [
                              [
                                  [
                                      530857.01,
                                      181500
                                  ],
                                  [
                                      530857,
                                      181500
                                  ],
                                  [
                                      530857,
                                      181500
                                  ],
                                  [
                                      530857,
                                      181500
                                  ],
                                  [
                                      530857.01,
                                      181500
                                  ]
                              ]
                          ]
                      ],
                      "type": "MultiPolygon"
                  },
                  "properties": {},
                  "type": "Feature"
              }
          },
          {
              "easement_description": "easement two",
              "easement_geometry": {
                  "crs": {
                      "properties": {
                          "name": "urn:ogc:def:crs:EPSG:27700"
                      },
                      "type": "name"
                  },
                  "geometry": {
                      "coordinates": [
                          [
                              [
                                  [
                                      530857.01,
                                      181500
                                  ],
                                  [
                                      530857,
                                      181500
                                  ],
                                  [
                                      530857,
                                      181500
                                  ],
                                  [
                                      530857,
                                      181500
                                  ],
                                  [
                                      530857.01,
                                      181500
                                  ]
                              ]
                          ]
                      ],
                      "type": "MultiPolygon"
                  },
                  "properties": {},
                  "type": "Feature"
              }
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
      "title_number": "TEST198",
      "extent": {
          "crs": {
              "properties": {
                  "name": "urn:ogc:def:crs:EPSG:27700"
              },
              "type": "name"
          },
          "geometry": {
              "coordinates": [
                  [
                      [
                          [
                              530857.01,
                              181500
                          ],
                          [
                              530857,
                              181500
                          ],
                          [
                              530857,
                              181500
                          ],
                          [
                              530857,
                              181500
                          ],
                          [
                              530857.01,
                              181500
                          ]
                      ]
                  ]
              ],
              "type": "MultiPolygon"
          },
          "properties": {},
          "type": "Feature"
      },
  }

title_no_easement = {
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
      "extent": {
          "crs": {
              "properties": {
                  "name": "urn:ogc:def:crs:EPSG:27700"
              },
              "type": "name"
          },
          "geometry": {
              "coordinates": [
                  [
                      [
                          [
                              530857.01,
                              181500
                          ],
                          [
                              530857,
                              181500
                          ],
                          [
                              530857,
                              181500
                          ],
                          [
                              530857,
                              181500
                          ],
                          [
                              530857.01,
                              181500
                          ]
                      ]
                  ]
              ],
              "type": "MultiPolygon"
          },
          "properties": {},
          "type": "Feature"
      },
  }

response_json = json.dumps(title)
response_without_charge = json.dumps(title_no_charge)
response_without_easement =  json.dumps(title_no_easement)
