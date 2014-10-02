# coding=utf-8
title={
    "title_number": "TEST198",

    "proprietors": [
        {
            "full_name": "Michael Jones"
        }
    ],

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

    "extent": {
        "type": "Feature",
        "crs": {
            "type":"name",
            "properties":{
                "name":"urn:ogc:def:crs:EPSG:27700"
            }
        },
        "geometry":{
            "type":"Polygon",
            "coordinates":[
                [[530857.01,181500.00],
                 [530857.00,181500.00],
                 [530857.00,181500.00],
                 [530857.00,181500.00],
                 [530857.01,181500.00]]
            ]
        },
        "properties":{
        }
    },

    "proprietorship" :   {
        "template" : "PROPRIETOR(S):  *RP*",
        "full_text": "PROPRIETOR(S): Michael Jones of 8 Miller Way, Plymouth, Devon, PL6 8UQ",
        "fields" : {"proprietors":[{"name" : {"title" : "Mr", "full_name" : "Bob Test", "decoration" : ""}, "address" : {"full_address": "8 Miller Way, Plymouth, Devon, PL6 8UQ", "house_no" : "8", "street_name" : "Miller Way", "town" : "Plymouth", "postal_county" : "Devon", "region_name" : "", "country" : "", "postcode":""}},
                                   {"name" : {"title" : "Mrs", "full_name" : "Betty Tanker", "decoration" : ""}, "address" : {"full_address": "8 Miller Way, Plymouth, Devon, PL6 8UQ", "house_no" : "8", "street_name" : "Miller Way", "town" : "Plymouth", "postal_county" : "Devon", "region_name" : "", "country" : "", "postcode":""}}]},
        "deeds" : [],
        "notes" : []
    },

    "property_description" : {
        "template" : "The Freehold land shown edged with red on the plan of the above Title filed at the Registry and being *AD*",
        "full_text" : "The Freehold land shown edged with red on the plan of the above Title filed at the Registry and being 8 Miller Way, Plymouth, Devon, PL6 8UQ",
        "fields" : {"tenure": "freehold", "address" : {"full_address": "8 Miller Way, Plymouth, Devon, PL6 8UQ", "house_no" : "8", "street_name" : "Miller Way", "town" : "Plymouth", "postal_county" : "Devon", "region_name" : "", "country" : "", "postcode":""}},
        "deeds" : [],
        "notes" : []
    },

    "restrictive_covenants" : [{

                                   "template" : "By an Order of the Upper Tribunal (Lands Chamber) dated *DA* made pursuant to Section 84 of the Law of Property Act 1925 the restrictive covenants contained in the *DT**DE* dated *DD* referred to above were released. *N<NOTE: Copy Order filed>N*.",
                                   "full_text" : "By an Order of the Upper Tribunal (Lands Chamber) dated 14/06/2013 made pursuant to Section 84 of the Law of Property Act 1925 the restrictive covenants contained in the Conveyance dated 01.06.1996 referred to above were released. NOTE: Copy Order filed",
                                   "fields" : {"date" : "14/06/2013", "extent" : [""]},
                                   "deeds" : [{"type" : "Conveyance", "date" : "01.06.1996", "parties" : [{"title" : "Mr", "full_name" : "Michael Jones", "decoration" : ""},{"title" : "Mr", "full_name" : "Jeff Smith", "decoration" : ""}]}],
                                   "notes" : [{"text" : "Copy Order filed", "documents_referred" : "I"}]
                               }],

    "bankruptcy" : [{
                        "template" : "BANKRUPTCY NOTICE entered under section 86(2) of the Land Registration Act 2002 in respect of a pending action, as the title of the proprietor of the registered estate appears to be affected by a petition in bankruptcy against *NM* presented in the *M<>M* Court (Court Reference Number *M<>M*) (Land Charges Reference Number PA*M<>M*).",
                        "full_text" : "BANKRUPTCY NOTICE entered under section 86(2) of the Land Registration Act 2002 in respect of a pending action, as the title of the proprietor of the registered estate appears to be affected by a petition in bankruptcy against James Lock presented in the Gloucester County Court (Court Reference Number 124578) (Land Charges Reference Number PA102).",
                        "fields" : {"name" : "James Lock", "miscellaneous" : ["Gloucester County",  "124578",  "102"]},
                        "deeds" : [],
                        "notes" : []
                    }],

    "easements" : [{
                       "template" : "The land *E<>E* is subject to the rights granted by a *DT**DE* dated *DD* made between *DP*. The said Deed also contains restrictive covenants by the grantor. *N<^NOTE: Copy in Certificate. Copy filed>N*.",
                       "full_text" : "easement one",
                       "fields" : {"extent" : ["tinted pink", ""]},
                       "deeds" : [{"type" : "Deed", "date" : "03.03.1976", "parties" : [{"title" : "Mr", "full_name" : "Michael Jones", "decoration" : ""},{"title" : "Mr", "full_name" : "Jeff Smith", "decoration" : ""}]}],
                       "notes" : [{"text" : "Copy filed", "documents_referred" : "I"}]
                   },
                   {
                       "template" : "The land *E<>E* is subject to the rights granted by a *DT**DE* dated *DD* made between *DP*. The said Deed also contains restrictive covenants by the grantor. *N<^NOTE: Copy in Certificate. Copy filed>N*.",
                       "full_text" : "easement two",
                       "fields" : {"extent" : ["tinted pink", ""]},
                       "deeds" : [{"type" : "Deed", "date" : "03.03.1976", "parties" : [{"title" : "Mr", "full_name" : "Michael Jones", "decoration" : ""},{"title" : "Mr", "full_name" : "Jeff Smith", "decoration" : ""}]}],
                       "notes" : [{"text" : "Copy filed", "documents_referred" : "I"}]
                   }],

    "provisions" : [{
                        "template" : "A *DT**DE* dated *DD* made between *DP* contains the following provision:-*VT*",
                        "full_text" : "A Transfer of the land in this title dated 01.06.1996 made between Mr Michael Jones and Mr Jeff Smith contains the following provision:-The land has the benefit of a right of way along the passageway to the rear of the property, and also a right of way on foot only on to the open ground on the north west boundary of the land in this title",
                        "fields" : {"extent" : ["of the land in this title"], "verbatim_text" : "The land has the benefit of a right of way along the passageway to the rear of the property, and also a right of way on foot only on to the open ground on the north west boundary of the land in this title"},
                        "deeds" : [{"type" : "Transfer", "date" : "01.06.1996", "parties" : [{"title" : "Mr", "full_name" : "Michael Jones", "decoration" : ""},{"title" : "Mr", "full_name" : "Jeff Smith", "decoration" : ""}]}],
                        "notes" : []
                    }],

    "price_paid" : {
        "template" : "The price stated to have been paid on *DA* was *AM*.",
        "full_text" : "The price stated to have been paid on 15/11/2005 was £100,000.",
        "fields" : {"date" : "15/11/2005", "amount" : "2,000,000"},
        "deeds" : [],
        "notes" : []
    }

}


import json
response_json = json.dumps(title)