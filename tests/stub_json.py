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
            "full_name": "Bob Test"
        },
        {
            "full_name": "Betty Tanker"
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
            "full_name": "Bob Test"
        },
        {
            "full_name": "Betty Tanker"
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
    }
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
            "full_name": "Bob Test"
        },
        {
            "full_name": "Betty Tanker"
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
    }
}

conveyancer_one_client = {
    "conveyancer_lrid": "214b78b1-20a0-4cdb-a0f3-111b5ba21d48",
    "title_number": "TEST1410429781566",
    "conveyancer_name": "Da Big Boss Company",
    "conveyancer_address": "123 High Street, Stoke, ST4 4AX",
    "clients": [
        {
            "lrid": "f55a02a0-057b-4a3f-9e34-ede5791a5874",
            "name": "Walter White",
            "address": "1 The house, The town, PL1 1AA",
            "DOB": "01-01-1960",
            "tel_no": "01752 123456",
            "email": "citizen@example.org"
        }
    ],
    "task": "sell"
}

conveyancer_two_clients = {
    "conveyancer_lrid": "214b78b1-20a0-4cdb-a0f3-111b5ba21d48",
    "title_number": "TEST1410429781566",
    "conveyancer_name": "Da Big Boss Company",
    "conveyancer_address": "123 High Street, Stoke, ST4 4AX",
    "clients": [
        {
            "lrid": "f55a02a0-057b-4a3f-9e34-ede5791a5874",
            "name": "Walter White",
            "address": "1 The house, The town, PL1 1AA",
            "DOB": "01-01-1960",
            "tel_no": "01752 123456",
            "email": "citizen@example.org"
        },
        {
            "lrid": "f55a02a0-057b-4a3f-9e34-ede5791a5874",
            "name": "Skyler White",
            "address": "1 The house, The town, PL1 1AA",
            "DOB": "04-06-1970",
            "tel_no": "01752 9999999",
            "email": "citizen2@example.org"
        }
    ],
    "task": "sell"
}

introductions_response = {
    "task": "sell",
    "conveyancer_address": "123 High Street, Stoke, ST4 4AX",
    "conveyancer_name": "Da Big Boss Company",
    "client_lrid": "f55a02a0-057b-4a3f-9e34-ede5791a5874",
    "title_number": "TEST1410429781566",
    "conveyancer_lrid": "214b78b1-20a0-4cdb-a0f3-111b5ba21d48"
}

response_json = json.dumps(title)
response_without_charge = json.dumps(title_no_charge)
response_without_easement = json.dumps(title_no_easement)

response_relationship_one_client = json.dumps(conveyancer_one_client)
response_relationship_two_clients = json.dumps(conveyancer_two_clients)

response_intoduction_token_details = json.dumps(introductions_response)