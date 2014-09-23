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

changes_two_pending_two_previous = {
    [
        {
            "status": "completed",
            "work_queue": "casework",
            "title_number": "TEST_SM7333269",
            "request_details_data": {
                "proprietor_full_name": "Denise Bates",
                "title": {
                    "previous_sha256": "cafebabe",
                    "proprietors": [
                        {
                            "full_name": "Ford Prefect"
                        },
                        {
                            "full_name": "Kerry Myers"
                        }
                    ],
                    "title_number": "TEST_SM7333269",
                    "extent": {
                        "geometry": {
                            "type": "MultiPolygon",
                            "coordinates": [
                                [
                                    [
                                        [
                                            530647,
                                            181419
                                        ],
                                        [
                                            530855,
                                            181500
                                        ],
                                        [
                                            530917,
                                            181351
                                        ],
                                        [
                                            530713,
                                            181266
                                        ],
                                        [
                                            530647,
                                            181419
                                        ]
                                    ]
                                ]
                            ]
                        },
                        "crs": {
                            "type": "name",
                            "properties": {
                                "name": "urn:ogc:def:crs:EPSG:27700"
                            }
                        },
                        "type": "Feature",
                        "properties": {}
                    },
                    "property": {
                        "address": {
                            "house_number": "376-8006",
                            "town": "RaurkelaCivilTownship",
                            "postcode": "L954ZD",
                            "road": "Enim.Road"
                        },
                        "class_of_title": "good",
                        "tenure": "freehold"
                    },
                    "payment": {
                        "titles": [
                            "TEST_SM7333269"
                        ],
                        "price_paid": "208648"
                    }
                },
                "partner_name": "Arthur Dent",
                "application_type": "change-name-marriage",
                "confirm": true,
                "proprietor_new_full_name": "Ford Prefect",
                "marriage_place": "Mars",
                "marriage_country": "GB",
                "title_number": "TEST_SM7333269",
                "marriage_certificate_number": "1234567890",
                "marriage_date": 1410303600
            },
            "submitted_by": "Denise Bates",
            "request_details": "{\"action\": \"change-name-marriage\", \"data\": \"{\\\"confirm\\\": true, \\\"partner_name\\\": \\\"Arthur Dent\\\", \\\"application_type\\\": \\\"change-name-marriage\\\", \\\"title\\\": {\\\"previous_sha256\\\": \\\"cafebabe\\\", \\\"proprietors\\\": [{\\\"full_name\\\": \\\"Ford Prefect\\\"}, {\\\"full_name\\\": \\\"Kerry Myers\\\"}], \\\"title_number\\\": \\\"TEST_SM7333269\\\", \\\"extent\\\": {\\\"geometry\\\": {\\\"type\\\": \\\"MultiPolygon\\\", \\\"coordinates\\\": [[[[530647, 181419], [530855, 181500], [530917, 181351], [530713, 181266], [530647, 181419]]]]}, \\\"crs\\\": {\\\"type\\\": \\\"name\\\", \\\"properties\\\": {\\\"name\\\": \\\"urn:ogc:def:crs:EPSG:27700\\\"}}, \\\"type\\\": \\\"Feature\\\", \\\"properties\\\": {}}, \\\"property\\\": {\\\"tenure\\\": \\\"freehold\\\", \\\"class_of_title\\\": \\\"good\\\", \\\"address\\\": {\\\"house_number\\\": \\\"376-8006\\\", \\\"town\\\": \\\"RaurkelaCivilTownship\\\", \\\"postcode\\\": \\\"L954ZD\\\", \\\"road\\\": \\\"Enim.Road\\\"}}, \\\"payment\\\": {\\\"titles\\\": [\\\"TEST_SM7333269\\\"], \\\"price_paid\\\": \\\"208648\\\"}}, \\\"proprietor_new_full_name\\\": \\\"Ford Prefect\\\", \\\"marriage_place\\\": \\\"Mars\\\", \\\"title_number\\\": \\\"TEST_SM7333269\\\", \\\"proprietor_full_name\\\": \\\"Denise Bates\\\", \\\"marriage_certificate_number\\\": \\\"1234567890\\\", \\\"marriage_country\\\": \\\"GB\\\", \\\"marriage_date\\\": 1410303600}\", \"context\": {\"session-id\": \"123456\", \"transaction-id\": \"ABCDEFG\"}}",
            "application_type": "change-name-marriage",
            "id": 1,
            "submitted_at": "19-09-2014 13:46:19 864948"
        },
        {
            "status": "completed",
            "work_queue": "casework",
            "title_number": "TEST_SM7333269",
            "request_details_data": {
                "proprietor_full_name": "Kerry Myers",
                "title": {
                    "previous_sha256": "cafebabe",
                    "proprietors": [
                        {
                            "full_name": "Denise Bates"
                        },
                        {
                            "full_name": "fdxgchvjbk"
                        }
                    ],
                    "title_number": "TEST_SM7333269",
                    "extent": {
                        "geometry": {
                            "type": "MultiPolygon",
                            "coordinates": [
                                [
                                    [
                                        [
                                            530647,
                                            181419
                                        ],
                                        [
                                            530855,
                                            181500
                                        ],
                                        [
                                            530917,
                                            181351
                                        ],
                                        [
                                            530713,
                                            181266
                                        ],
                                        [
                                            530647,
                                            181419
                                        ]
                                    ]
                                ]
                            ]
                        },
                        "crs": {
                            "type": "name",
                            "properties": {
                                "name": "urn:ogc:def:crs:EPSG:27700"
                            }
                        },
                        "type": "Feature",
                        "properties": {}
                    },
                    "property": {
                        "address": {
                            "house_number": "376-8006",
                            "town": "RaurkelaCivilTownship",
                            "postcode": "L954ZD",
                            "road": "Enim.Road"
                        },
                        "class_of_title": "good",
                        "tenure": "freehold"
                    },
                    "payment": {
                        "titles": [
                            "TEST_SM7333269"
                        ],
                        "price_paid": "208648"
                    }
                },
                "partner_name": "hcgvjbknl",
                "application_type": "change-name-marriage",
                "confirm": true,
                "proprietor_new_full_name": "fdxgchvjbk",
                "marriage_place": "fcghvjbk",
                "marriage_country": "GB",
                "title_number": "TEST_SM7333269",
                "marriage_certificate_number": "45678",
                "marriage_date": 1390176000
            },
            "submitted_by": "Kerry Myers",
            "request_details": "{\"action\": \"change-name-marriage\", \"data\": \"{\\\"confirm\\\": true, \\\"partner_name\\\": \\\"hcgvjbknl\\\", \\\"application_type\\\": \\\"change-name-marriage\\\", \\\"title\\\": {\\\"previous_sha256\\\": \\\"cafebabe\\\", \\\"proprietors\\\": [{\\\"full_name\\\": \\\"Denise Bates\\\"}, {\\\"full_name\\\": \\\"fdxgchvjbk\\\"}], \\\"title_number\\\": \\\"TEST_SM7333269\\\", \\\"extent\\\": {\\\"geometry\\\": {\\\"type\\\": \\\"MultiPolygon\\\", \\\"coordinates\\\": [[[[530647, 181419], [530855, 181500], [530917, 181351], [530713, 181266], [530647, 181419]]]]}, \\\"crs\\\": {\\\"type\\\": \\\"name\\\", \\\"properties\\\": {\\\"name\\\": \\\"urn:ogc:def:crs:EPSG:27700\\\"}}, \\\"type\\\": \\\"Feature\\\", \\\"properties\\\": {}}, \\\"property\\\": {\\\"tenure\\\": \\\"freehold\\\", \\\"class_of_title\\\": \\\"good\\\", \\\"address\\\": {\\\"house_number\\\": \\\"376-8006\\\", \\\"town\\\": \\\"RaurkelaCivilTownship\\\", \\\"postcode\\\": \\\"L954ZD\\\", \\\"road\\\": \\\"Enim.Road\\\"}}, \\\"payment\\\": {\\\"titles\\\": [\\\"TEST_SM7333269\\\"], \\\"price_paid\\\": \\\"208648\\\"}}, \\\"proprietor_new_full_name\\\": \\\"fdxgchvjbk\\\", \\\"marriage_place\\\": \\\"fcghvjbk\\\", \\\"title_number\\\": \\\"TEST_SM7333269\\\", \\\"proprietor_full_name\\\": \\\"Kerry Myers\\\", \\\"marriage_certificate_number\\\": \\\"45678\\\", \\\"marriage_country\\\": \\\"GB\\\", \\\"marriage_date\\\": 1390176000}\", \"context\": {\"session-id\": \"123456\", \"transaction-id\": \"ABCDEFG\"}}",
            "application_type": "change-name-marriage",
            "id": 2,
            "submitted_at": "19-09-2014 15:28:55 704923"
        },
        {
            "status": "queued",
            "work_queue": "casework",
            "title_number": "TEST_SM7333269",
            "request_details_data": {
                "proprietor_full_name": "Denise Bates",
                "title": {
                    "previous_sha256": "cafebabe",
                    "proprietors": [
                        {
                            "full_name": "Zaphod Beeblebrox"
                        },
                        {
                            "full_name": "Kerry Myers"
                        }
                    ],
                    "title_number": "TEST_SM7333269",
                    "extent": {
                        "geometry": {
                            "type": "MultiPolygon",
                            "coordinates": [
                                [
                                    [
                                        [
                                            530647,
                                            181419
                                        ],
                                        [
                                            530855,
                                            181500
                                        ],
                                        [
                                            530917,
                                            181351
                                        ],
                                        [
                                            530713,
                                            181266
                                        ],
                                        [
                                            530647,
                                            181419
                                        ]
                                    ]
                                ]
                            ]
                        },
                        "crs": {
                            "type": "name",
                            "properties": {
                                "name": "urn:ogc:def:crs:EPSG:27700"
                            }
                        },
                        "type": "Feature",
                        "properties": {}
                    },
                    "property": {
                        "address": {
                            "house_number": "376-8006",
                            "town": "RaurkelaCivilTownship",
                            "postcode": "L954ZD",
                            "road": "Enim.Road"
                        },
                        "class_of_title": "good",
                        "tenure": "freehold"
                    },
                    "payment": {
                        "titles": [
                            "TEST_SM7333269"
                        ],
                        "price_paid": "208648"
                    }
                },
                "partner_name": "Ford Prefect",
                "application_type": "change-name-marriage",
                "confirm": true,
                "proprietor_new_full_name": "Zaphod Beeblebrox",
                "marriage_place": "Birmingham",
                "marriage_country": "GB",
                "title_number": "TEST_SM7333269",
                "marriage_certificate_number": "1234567890",
                "marriage_date": 1408489200
            },
            "submitted_by": "Denise Bates",
            "request_details": "{\"action\": \"change-name-marriage\", \"data\": \"{\\\"confirm\\\": true, \\\"partner_name\\\": \\\"Ford Prefect\\\", \\\"application_type\\\": \\\"change-name-marriage\\\", \\\"title\\\": {\\\"previous_sha256\\\": \\\"cafebabe\\\", \\\"proprietors\\\": [{\\\"full_name\\\": \\\"Zaphod Beeblebrox\\\"}, {\\\"full_name\\\": \\\"Kerry Myers\\\"}], \\\"title_number\\\": \\\"TEST_SM7333269\\\", \\\"extent\\\": {\\\"geometry\\\": {\\\"type\\\": \\\"MultiPolygon\\\", \\\"coordinates\\\": [[[[530647, 181419], [530855, 181500], [530917, 181351], [530713, 181266], [530647, 181419]]]]}, \\\"crs\\\": {\\\"type\\\": \\\"name\\\", \\\"properties\\\": {\\\"name\\\": \\\"urn:ogc:def:crs:EPSG:27700\\\"}}, \\\"type\\\": \\\"Feature\\\", \\\"properties\\\": {}}, \\\"property\\\": {\\\"tenure\\\": \\\"freehold\\\", \\\"class_of_title\\\": \\\"good\\\", \\\"address\\\": {\\\"house_number\\\": \\\"376-8006\\\", \\\"town\\\": \\\"RaurkelaCivilTownship\\\", \\\"postcode\\\": \\\"L954ZD\\\", \\\"road\\\": \\\"Enim.Road\\\"}}, \\\"payment\\\": {\\\"titles\\\": [\\\"TEST_SM7333269\\\"], \\\"price_paid\\\": \\\"208648\\\"}}, \\\"proprietor_new_full_name\\\": \\\"Zaphod Beeblebrox\\\", \\\"marriage_place\\\": \\\"Birmingham\\\", \\\"title_number\\\": \\\"TEST_SM7333269\\\", \\\"proprietor_full_name\\\": \\\"Denise Bates\\\", \\\"marriage_certificate_number\\\": \\\"1234567890\\\", \\\"marriage_country\\\": \\\"GB\\\", \\\"marriage_date\\\": 1408489200}\", \"context\": {\"session-id\": \"123456\", \"transaction-id\": \"ABCDEFG\"}}",
            "application_type": "change-name-marriage",
            "id": 3,
            "submitted_at": "22-09-2014 14:14:17 835280"
        },
        {
            "status": "queued",
            "work_queue": "casework",
            "title_number": "TEST_SM7333269",
            "request_details_data": {
                "proprietor_full_name": "Kerry Myers",
                "title": {
                    "previous_sha256": "cafebabe",
                    "proprietors": [
                        {
                            "full_name": "Denise Bates"
                        },
                        {
                            "full_name": "Darth Vader"
                        }
                    ],
                    "title_number": "TEST_SM7333269",
                    "extent": {
                        "geometry": {
                            "type": "MultiPolygon",
                            "coordinates": [
                                [
                                    [
                                        [
                                            530647,
                                            181419
                                        ],
                                        [
                                            530855,
                                            181500
                                        ],
                                        [
                                            530917,
                                            181351
                                        ],
                                        [
                                            530713,
                                            181266
                                        ],
                                        [
                                            530647,
                                            181419
                                        ]
                                    ]
                                ]
                            ]
                        },
                        "crs": {
                            "type": "name",
                            "properties": {
                                "name": "urn:ogc:def:crs:EPSG:27700"
                            }
                        },
                        "type": "Feature",
                        "properties": {}
                    },
                    "property": {
                        "address": {
                            "house_number": "376-8006",
                            "town": "RaurkelaCivilTownship",
                            "postcode": "L954ZD",
                            "road": "Enim.Road"
                        },
                        "class_of_title": "good",
                        "tenure": "freehold"
                    },
                    "payment": {
                        "titles": [
                            "TEST_SM7333269"
                        ],
                        "price_paid": "208648"
                    }
                },
                "partner_name": "Chewbacca",
                "application_type": "change-name-marriage",
                "confirm": true,
                "proprietor_new_full_name": "Darth Vader",
                "marriage_place": "Tatooine",
                "marriage_country": "GB",
                "title_number": "TEST_SM7333269",
                "marriage_certificate_number": "1234567890",
                "marriage_date": 1390176000
            },
            "submitted_by": "Kerry Myers",
            "request_details": "{\"action\": \"change-name-marriage\", \"data\": \"{\\\"confirm\\\": true, \\\"partner_name\\\": \\\"Chewbacca\\\", \\\"application_type\\\": \\\"change-name-marriage\\\", \\\"title\\\": {\\\"previous_sha256\\\": \\\"cafebabe\\\", \\\"proprietors\\\": [{\\\"full_name\\\": \\\"Denise Bates\\\"}, {\\\"full_name\\\": \\\"Darth Vader\\\"}], \\\"title_number\\\": \\\"TEST_SM7333269\\\", \\\"extent\\\": {\\\"geometry\\\": {\\\"type\\\": \\\"MultiPolygon\\\", \\\"coordinates\\\": [[[[530647, 181419], [530855, 181500], [530917, 181351], [530713, 181266], [530647, 181419]]]]}, \\\"crs\\\": {\\\"type\\\": \\\"name\\\", \\\"properties\\\": {\\\"name\\\": \\\"urn:ogc:def:crs:EPSG:27700\\\"}}, \\\"type\\\": \\\"Feature\\\", \\\"properties\\\": {}}, \\\"property\\\": {\\\"tenure\\\": \\\"freehold\\\", \\\"class_of_title\\\": \\\"good\\\", \\\"address\\\": {\\\"house_number\\\": \\\"376-8006\\\", \\\"town\\\": \\\"RaurkelaCivilTownship\\\", \\\"postcode\\\": \\\"L954ZD\\\", \\\"road\\\": \\\"Enim.Road\\\"}}, \\\"payment\\\": {\\\"titles\\\": [\\\"TEST_SM7333269\\\"], \\\"price_paid\\\": \\\"208648\\\"}}, \\\"proprietor_new_full_name\\\": \\\"Darth Vader\\\", \\\"marriage_place\\\": \\\"Tatooine\\\", \\\"title_number\\\": \\\"TEST_SM7333269\\\", \\\"proprietor_full_name\\\": \\\"Kerry Myers\\\", \\\"marriage_certificate_number\\\": \\\"1234567890\\\", \\\"marriage_country\\\": \\\"GB\\\", \\\"marriage_date\\\": 1390176000}\", \"context\": {\"session-id\": \"123456\", \"transaction-id\": \"ABCDEFG\"}}",
            "application_type": "change-name-marriage",
            "id": 4,
            "submitted_at": "22-09-2014 14:22:33 031824"
        }
    ]
}

changes_one_pending = {
    [
        {
            "status": "queued",
            "work_queue": "casework",
            "title_number": "TEST_SD2215752",
            "request_details_data": {
                "proprietor_full_name": "Donna Trevino",
                "title": {
                    "previous_sha256": "cafebabe",
                    "proprietors": [
                        {
                            "full_name": "Winston Smith"
                        },
                        {
                            "full_name": "Hu Walker"
                        }
                    ],
                    "title_number": "TEST_SD2215752",
                    "extent": {
                        "geometry": {
                            "type": "MultiPolygon",
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
                            ]
                        },
                        "crs": {
                            "type": "name",
                            "properties": {
                                "name": "urn:ogc:def:crs:EPSG:27700"
                            }
                        },
                        "type": "Feature",
                        "properties": {}
                    },
                    "property": {
                        "address": {
                            "house_number": "P.O.Box697,7528",
                            "town": "Savannah",
                            "postcode": "AN162GK",
                            "road": "Vestibulum,Rd."
                        },
                        "class_of_title": "good",
                        "tenure": "leasehold"
                    },
                    "payment": {
                        "titles": [
                            "TEST_SD2215752"
                        ],
                        "price_paid": "728068"
                    }
                },
                "partner_name": "Julia Smith",
                "application_type": "change-name-marriage",
                "confirm": true,
                "proprietor_new_full_name": "Winston Smith",
                "marriage_place": "London",
                "marriage_country": "GB",
                "title_number": "TEST_SD2215752",
                "marriage_certificate_number": "1234567890",
                "marriage_date": 1390176000
            },
            "submitted_by": "Donna Trevino",
            "request_details": "{\"action\": \"change-name-marriage\", \"data\": \"{\\\"confirm\\\": true, \\\"partner_name\\\": \\\"Julia Smith\\\", \\\"application_type\\\": \\\"change-name-marriage\\\", \\\"title\\\": {\\\"previous_sha256\\\": \\\"cafebabe\\\", \\\"proprietors\\\": [{\\\"full_name\\\": \\\"Winston Smith\\\"}, {\\\"full_name\\\": \\\"Hu Walker\\\"}], \\\"title_number\\\": \\\"TEST_SD2215752\\\", \\\"extent\\\": {\\\"geometry\\\": {\\\"type\\\": \\\"MultiPolygon\\\", \\\"coordinates\\\": [[[[530857.01, 181500.0], [530857.0, 181500.0], [530857.0, 181500.0], [530857.0, 181500.0], [530857.01, 181500.0]]]]}, \\\"crs\\\": {\\\"type\\\": \\\"name\\\", \\\"properties\\\": {\\\"name\\\": \\\"urn:ogc:def:crs:EPSG:27700\\\"}}, \\\"type\\\": \\\"Feature\\\", \\\"properties\\\": {}}, \\\"property\\\": {\\\"tenure\\\": \\\"leasehold\\\", \\\"class_of_title\\\": \\\"good\\\", \\\"address\\\": {\\\"house_number\\\": \\\"P.O.Box697,7528\\\", \\\"town\\\": \\\"Savannah\\\", \\\"postcode\\\": \\\"AN162GK\\\", \\\"road\\\": \\\"Vestibulum,Rd.\\\"}}, \\\"payment\\\": {\\\"titles\\\": [\\\"TEST_SD2215752\\\"], \\\"price_paid\\\": \\\"728068\\\"}}, \\\"proprietor_new_full_name\\\": \\\"Winston Smith\\\", \\\"marriage_place\\\": \\\"London\\\", \\\"title_number\\\": \\\"TEST_SD2215752\\\", \\\"proprietor_full_name\\\": \\\"Donna Trevino\\\", \\\"marriage_certificate_number\\\": \\\"1234567890\\\", \\\"marriage_country\\\": \\\"GB\\\", \\\"marriage_date\\\": 1390176000}\", \"context\": {\"session-id\": \"123456\", \"transaction-id\": \"ABCDEFG\"}}",
            "application_type": "change-name-marriage",
            "id": 5,
            "submitted_at": "22-09-2014 14:35:31 112429"
        }
    ]
}

changes_one_complete = {
    [
        {
            "status": "completed",
            "work_queue": "casework",
            "title_number": "TEST_SD2215752",
            "request_details_data": {
                "proprietor_full_name": "Donna Trevino",
                "title": {
                    "previous_sha256": "cafebabe",
                    "proprietors": [
                        {
                            "full_name": "Winston Smith"
                        },
                        {
                            "full_name": "Hu Walker"
                        }
                    ],
                    "title_number": "TEST_SD2215752",
                    "extent": {
                        "geometry": {
                            "type": "MultiPolygon",
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
                            ]
                        },
                        "crs": {
                            "type": "name",
                            "properties": {
                                "name": "urn:ogc:def:crs:EPSG:27700"
                            }
                        },
                        "type": "Feature",
                        "properties": {}
                    },
                    "property": {
                        "address": {
                            "house_number": "P.O.Box697,7528",
                            "town": "Savannah",
                            "postcode": "AN162GK",
                            "road": "Vestibulum,Rd."
                        },
                        "class_of_title": "good",
                        "tenure": "leasehold"
                    },
                    "payment": {
                        "titles": [
                            "TEST_SD2215752"
                        ],
                        "price_paid": "728068"
                    }
                },
                "partner_name": "Julia Smith",
                "application_type": "change-name-marriage",
                "confirm": true,
                "proprietor_new_full_name": "Winston Smith",
                "marriage_place": "London",
                "marriage_country": "GB",
                "title_number": "TEST_SD2215752",
                "marriage_certificate_number": "1234567890",
                "marriage_date": 1390176000
            },
            "submitted_by": "Donna Trevino",
            "request_details": "{\"action\": \"change-name-marriage\", \"data\": \"{\\\"confirm\\\": true, \\\"partner_name\\\": \\\"Julia Smith\\\", \\\"application_type\\\": \\\"change-name-marriage\\\", \\\"title\\\": {\\\"previous_sha256\\\": \\\"cafebabe\\\", \\\"proprietors\\\": [{\\\"full_name\\\": \\\"Winston Smith\\\"}, {\\\"full_name\\\": \\\"Hu Walker\\\"}], \\\"title_number\\\": \\\"TEST_SD2215752\\\", \\\"extent\\\": {\\\"geometry\\\": {\\\"type\\\": \\\"MultiPolygon\\\", \\\"coordinates\\\": [[[[530857.01, 181500.0], [530857.0, 181500.0], [530857.0, 181500.0], [530857.0, 181500.0], [530857.01, 181500.0]]]]}, \\\"crs\\\": {\\\"type\\\": \\\"name\\\", \\\"properties\\\": {\\\"name\\\": \\\"urn:ogc:def:crs:EPSG:27700\\\"}}, \\\"type\\\": \\\"Feature\\\", \\\"properties\\\": {}}, \\\"property\\\": {\\\"tenure\\\": \\\"leasehold\\\", \\\"class_of_title\\\": \\\"good\\\", \\\"address\\\": {\\\"house_number\\\": \\\"P.O.Box697,7528\\\", \\\"town\\\": \\\"Savannah\\\", \\\"postcode\\\": \\\"AN162GK\\\", \\\"road\\\": \\\"Vestibulum,Rd.\\\"}}, \\\"payment\\\": {\\\"titles\\\": [\\\"TEST_SD2215752\\\"], \\\"price_paid\\\": \\\"728068\\\"}}, \\\"proprietor_new_full_name\\\": \\\"Winston Smith\\\", \\\"marriage_place\\\": \\\"London\\\", \\\"title_number\\\": \\\"TEST_SD2215752\\\", \\\"proprietor_full_name\\\": \\\"Donna Trevino\\\", \\\"marriage_certificate_number\\\": \\\"1234567890\\\", \\\"marriage_country\\\": \\\"GB\\\", \\\"marriage_date\\\": 1390176000}\", \"context\": {\"session-id\": \"123456\", \"transaction-id\": \"ABCDEFG\"}}",
            "application_type": "change-name-marriage",
            "id": 5,
            "submitted_at": "22-09-2014 14:35:31 112429"
        }
    ]
}

response_json = json.dumps(title)
response_without_charge = json.dumps(title_no_charge)
response_without_easement = json.dumps(title_no_easement)

response_relationship_one_client = json.dumps(conveyancer_one_client)
response_relationship_two_clients = json.dumps(conveyancer_two_clients)

changes_two_pending_and_previous = json.dumps(changes_two_pending_two_previous)
changes_one_complete = json.dumps(changes_one_complete)
changes_one_pending = json.dumps(changes_one_pending)