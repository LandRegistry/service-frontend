# coding=utf-8
title_no_charge = {
    "title_number": "TEST_AB1234567",
    "class_of_title":"Absolute",
    "tenure":"Leasehold",
    "edition_date":"10-31-2005",

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
        "fields" : {"proprietors":[{"name" : {"title" : "Mr", "full_name" : "Bob Test", "decoration" : ""}, "addresses" : [{"full_address": "8 Miller Way, Plymouth, Devon, PL6 8UQ", "house_no" : "8", "street_name" : "Miller Way", "town" : "Plymouth", "postal_county" : "Devon", "region_name" : "", "country" : "", "postcode":""}]},
                                   {"name" : {"title" : "Mrs", "full_name" : "Betty Tanker", "decoration" : ""}, "addresses" : [{"full_address": "8 Miller Way, Plymouth, Devon, PL6 8UQ", "house_no" : "8", "street_name" : "Miller Way", "town" : "Plymouth", "postal_county" : "Devon", "region_name" : "", "country" : "", "postcode":""}]}]},
        "deeds" : [],
        "notes" : []
    },

    "property_description" : {
        "template" : "The Freehold land shown edged with red on the plan of the above Title filed at the Registry and being *AD*",
        "full_text" : "The Freehold land shown edged with red on the plan of the above Title filed at the Registry and being 8 Miller Way, Plymouth, Devon, PL6 8UQ",
        "fields" : {"addresses" : [{"full_address": "8 Miller Way, Plymouth, Devon, PL6 8UQ", "house_no" : "8", "street_name" : "Miller Way", "town" : "Plymouth", "postal_county" : "Devon", "region_name" : "", "country" : "", "postcode":""}]},
        "deeds" : [],
        "notes" : []
    },

    "restrictive_covenants" : [{

                                   "template" : "By an Order of the Upper Tribunal (Lands Chamber) dated *DA* made pursuant to Section 84 of the Law of Property Act 1925 the restrictive covenants contained in the *DT**DE* dated *DD* referred to above were released. *N<¬NOTE: Copy Order filed>N*.",
                                   "full_text" : "By an Order of the Upper Tribunal (Lands Chamber) dated 14/06/2013 made pursuant to Section 84 of the Law of Property Act 1925 the restrictive covenants contained in the Conveyance dated 01.06.1996 referred to above were released. NOTE: Copy Order filed",
                                   "fields" : {"date" : ["14/06/2013"], "extent" : [""]},
                                   "deeds" : [{"type" : "Conveyance", "date" : "01.06.1996", "parties" : [{"title" : "Mr", "full_name" : "Michael Jones", "decoration" : ""},{"title" : "Mr", "full_name" : "Jeff Smith", "decoration" : ""}]}],
                                   "notes" : [{"text" : "Copy Order filed", "documents_referred" : "I"}]
                               }],

    "restrictions" : [{
                          "template" : "RESTRICTION: No disposition by the proprietor of the registered estate or in exercise of the power of sale or leasing in any registered charge (except an exempt disposal as defined by section 81(8) of the Housing Act 1988) is to be registered without the consent of - (a) in relation to a disposal of land in England by a private registered provider of social housing, the Regulator of Social Housing, (b) in relation to any other disposal of land in England, the Secretary of State, and (c) in relation to a disposal of land in Wales, the Welsh Ministers, to that disposition under *M<>M*.",
                          "full_text" : "RESTRICTION: No disposition by the proprietor of the registered estate or in exercise of the power of sale or leasing in any registered charge (except an exempt disposal as defined by section 81(8) of the Housing Act 1988) is to be registered without the consent of - (a) in relation to a disposal of land in England by a private registered provider of social housing, the Regulator of Social Housing, (b) in relation to any other disposal of land in England, the Secretary of State, and (c) in relation to a disposal of land in Wales, the Welsh Ministers, to that disposition under section 133 of that Act.",
                          "fields" : {"miscellaneous" : ["section 133 of that Act"]},
                          "deeds" : [],
                          "notes" : []
                      }],

    "bankruptcy" : [{
                        "template" : "BANKRUPTCY NOTICE entered under section 86(2) of the Land Registration Act 2002 in respect of a pending action, as the title of the proprietor of the registered estate appears to be affected by a petition in bankruptcy against *NM* presented in the *M<>M* Court (Court Reference Number *M<>M*) (Land Charges Reference Number PA*M<>M*).",
                        "full_text" : "BANKRUPTCY NOTICE entered under section 86(2) of the Land Registration Act 2002 in respect of a pending action, as the title of the proprietor of the registered estate appears to be affected by a petition in bankruptcy against James Lock presented in the Gloucester County Court (Court Reference Number 124578) (Land Charges Reference Number PA102).",
                        "fields" : {"name" : ["James Lock"], "miscellaneous" : ["Gloucester County",  "124578",  "102"]},
                        "deeds" : [],
                        "notes" : []
                    }],

    "easements" : [{
                       "template" : "The land *E<>E* is subject to the rights granted by a *DT**DE* dated *DD* made between *DP*. The said Deed also contains restrictive covenants by the grantor. *N<^NOTE: Copy in Certificate. Copy filed>N*.",
                       "full_text" : "The land tinted pink is subject to the rights granted by a Deed dated 03.03.1976 made between Mr Michael Jones and Mr Jeff Smith. The said Deed also contains restrictive covenants by the grantor. NOTE: Copy filed.",
                       "fields" : {"extent" : ["tinted pink", ""]},
                       "deeds" : [{"type" : "Deed", "date" : "03.03.1976", "parties" : [{"title" : "Mr", "full_name" : "Michael Jones", "decoration" : ""},{"title" : "Mr", "full_name" : "Jeff Smith", "decoration" : ""}]}],
                       "notes" : [{"text" : "Copy filed", "documents_referred" : "I"}]
                   }],

    "provisions" : [{
                        "template" : "A *DT**DE* dated *DD* made between *DP* contains the following provision:-*VT*",
                        "full_text" : "A Transfer of the land in this title dated 01.06.1996 made between Mr Michael Jones and Mr Jeff Smith contains the following provision:-The land has the benefit of a right of way along the passageway to the rear of the property, and also a right of way on foot only on to the open ground on the north west boundary of the land in this title",
                        "fields" : {"extent" : ["of the land in this title"], "verbatim_text" : ["The land has the benefit of a right of way along the passageway to the rear of the property, and also a right of way on foot only on to the open ground on the north west boundary of the land in this title"]},
                        "deeds" : [{"type" : "Transfer", "date" : "01.06.1996", "parties" : [{"title" : "Mr", "full_name" : "Michael Jones", "decoration" : ""},{"title" : "Mr", "full_name" : "Jeff Smith", "decoration" : ""}]}],
                        "notes" : []
                    }],

    "price_paid" : {
        "template" : "The price stated to have been paid on *DA* was *AM*.",
        "full_text" : "The price stated to have been paid on 15/11/2005 was 100,000.",
        "fields" : {"date" : ["15/11/2005"], "amount" : ["100,000"]},
        "deeds" : [],
        "notes" : []
    },

    "h_schedule" : {
        "template" : "Short particulars of the lease(s) (or under-lease(s)) under which the land is held: Date: *DD* Term: *TM* *OR*<RENT:>*OR* Parties *DP* *NN* ",
        "full_text" : "Short particulars of the lease(s) (or under-lease(s)) under which the land is held: Date: 22nd September 1998 Term: 999 years Parties: Mr Michael Jones and Mr Jeff Smith. Note: The lease also comprises other land.",
        "fields" : {},
        "deeds" : [{"type" : "Transfer", "date" : "01.06.1996", "term" : "999 years", "parties" : [{"title" : "Mr", "full_name" : "Michael Jones", "decoration" : ""},{"title" : "Mr", "full_name" : "Jeff Smith", "decoration" : ""}]}],
        "notes" : [{"text" : "The lease also comprises other land", "documents_referred" : ""}]
    },
    "other" : [],
    "charges" : []

}

title_no_easement = {
    "title_number": "TEST_AB1234567",
    "class_of_title":"Absolute",
    "tenure":"Leasehold",
    "edition_date":"10-31-2005",

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
        "fields" : {"proprietors":[{"name" : {"title" : "Mr", "full_name" : "Bob Test", "decoration" : ""}, "addresses" : [{"full_address": "8 Miller Way, Plymouth, Devon, PL6 8UQ", "house_no" : "8", "street_name" : "Miller Way", "town" : "Plymouth", "postal_county" : "Devon", "region_name" : "", "country" : "", "postcode":""}]},
                                   {"name" : {"title" : "Mrs", "full_name" : "Betty Tanker", "decoration" : ""}, "addresses" : [{"full_address": "8 Miller Way, Plymouth, Devon, PL6 8UQ", "house_no" : "8", "street_name" : "Miller Way", "town" : "Plymouth", "postal_county" : "Devon", "region_name" : "", "country" : "", "postcode":""}]}]},
        "deeds" : [],
        "notes" : []
    },

    "property_description" : {
        "template" : "The Freehold land shown edged with red on the plan of the above Title filed at the Registry and being *AD*",
        "full_text" : "The Freehold land shown edged with red on the plan of the above Title filed at the Registry and being 8 Miller Way, Plymouth, Devon, PL6 8UQ",
        "fields" : {"addresses" : [{"full_address": "8 Miller Way, Plymouth, Devon, PL6 8UQ", "house_no" : "8", "street_name" : "Miller Way", "town" : "Plymouth", "postal_county" : "Devon", "region_name" : "", "country" : "", "postcode":""}]},
        "deeds" : [],
        "notes" : []
    },

    "restrictive_covenants" : [{

                                   "template" : "By an Order of the Upper Tribunal (Lands Chamber) dated *DA* made pursuant to Section 84 of the Law of Property Act 1925 the restrictive covenants contained in the *DT**DE* dated *DD* referred to above were released. *N<¬NOTE: Copy Order filed>N*.",
                                   "full_text" : "By an Order of the Upper Tribunal (Lands Chamber) dated 14/06/2013 made pursuant to Section 84 of the Law of Property Act 1925 the restrictive covenants contained in the Conveyance dated 01.06.1996 referred to above were released. NOTE: Copy Order filed",
                                   "fields" : {"date" : ["14/06/2013"], "extent" : [""]},
                                   "deeds" : [{"type" : "Conveyance", "date" : "01.06.1996", "parties" : [{"title" : "Mr", "full_name" : "Michael Jones", "decoration" : ""},{"title" : "Mr", "full_name" : "Jeff Smith", "decoration" : ""}]}],
                                   "notes" : [{"text" : "Copy Order filed", "documents_referred" : "I"}]
                               }],

    "restrictions" : [{
                          "template" : "RESTRICTION: No disposition by the proprietor of the registered estate or in exercise of the power of sale or leasing in any registered charge (except an exempt disposal as defined by section 81(8) of the Housing Act 1988) is to be registered without the consent of - (a) in relation to a disposal of land in England by a private registered provider of social housing, the Regulator of Social Housing, (b) in relation to any other disposal of land in England, the Secretary of State, and (c) in relation to a disposal of land in Wales, the Welsh Ministers, to that disposition under *M<>M*.",
                          "full_text" : "RESTRICTION: No disposition by the proprietor of the registered estate or in exercise of the power of sale or leasing in any registered charge (except an exempt disposal as defined by section 81(8) of the Housing Act 1988) is to be registered without the consent of - (a) in relation to a disposal of land in England by a private registered provider of social housing, the Regulator of Social Housing, (b) in relation to any other disposal of land in England, the Secretary of State, and (c) in relation to a disposal of land in Wales, the Welsh Ministers, to that disposition under section 133 of that Act.",
                          "fields" : {"miscellaneous" : ["section 133 of that Act"]},
                          "deeds" : [],
                          "notes" : []
                      }],

    "bankruptcy" : [{
                        "template" : "BANKRUPTCY NOTICE entered under section 86(2) of the Land Registration Act 2002 in respect of a pending action, as the title of the proprietor of the registered estate appears to be affected by a petition in bankruptcy against *NM* presented in the *M<>M* Court (Court Reference Number *M<>M*) (Land Charges Reference Number PA*M<>M*).",
                        "full_text" : "BANKRUPTCY NOTICE entered under section 86(2) of the Land Registration Act 2002 in respect of a pending action, as the title of the proprietor of the registered estate appears to be affected by a petition in bankruptcy against James Lock presented in the Gloucester County Court (Court Reference Number 124578) (Land Charges Reference Number PA102).",
                        "fields" : {"name" : ["James Lock"], "miscellaneous" : ["Gloucester County",  "124578",  "102"]},
                        "deeds" : [],
                        "notes" : []
                    }],

    "easements" : [],

    "provisions" : [{
                        "template" : "A *DT**DE* dated *DD* made between *DP* contains the following provision:-*VT*",
                        "full_text" : "A Transfer of the land in this title dated 01.06.1996 made between Mr Michael Jones and Mr Jeff Smith contains the following provision:-The land has the benefit of a right of way along the passageway to the rear of the property, and also a right of way on foot only on to the open ground on the north west boundary of the land in this title",
                        "fields" : {"extent" : ["of the land in this title"], "verbatim_text" : ["The land has the benefit of a right of way along the passageway to the rear of the property, and also a right of way on foot only on to the open ground on the north west boundary of the land in this title"]},
                        "deeds" : [{"type" : "Transfer", "date" : "01.06.1996", "parties" : [{"title" : "Mr", "full_name" : "Michael Jones", "decoration" : ""},{"title" : "Mr", "full_name" : "Jeff Smith", "decoration" : ""}]}],
                        "notes" : []
                    }],

    "price_paid" : {
        "template" : "The price stated to have been paid on *DA* was *AM*.",
        "full_text" : "The price stated to have been paid on 15/11/2005 was £100,000.",
        "fields" : {"date" : ["15/11/2005"], "amount" : ["£100,000"]},
        "deeds" : [],
        "notes" : []
    },

    "h_schedule" : {
        "template" : "Short particulars of the lease(s) (or under-lease(s)) under which the land is held: Date: *DD* Term: *TM* *OR*<RENT:>*OR* Parties *DP* *NN* ",
        "full_text" : "Short particulars of the lease(s) (or under-lease(s)) under which the land is held: Date: 22nd September 1998 Term: 999 years Parties: Mr Michael Jones and Mr Jeff Smith. Note: The lease also comprises other land.",
        "fields" : {},
        "deeds" : [{"type" : "Transfer", "date" : "01.06.1996", "term" : "999 years", "parties" : [{"title" : "Mr", "full_name" : "Michael Jones", "decoration" : ""},{"title" : "Mr", "full_name" : "Jeff Smith", "decoration" : ""}]}],
        "notes" : [{"text" : "The lease also comprises other land", "documents_referred" : ""}]
    },
    "other" : [],
    "charges" : []


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
import json
response_without_charge = json.dumps(title_no_charge)
response_without_easement = json.dumps(title_no_easement, encoding='utf-8')

response_relationship_one_client = json.dumps(conveyancer_one_client)
response_relationship_two_clients = json.dumps(conveyancer_two_clients)

response_intoduction_token_details = json.dumps(introductions_response)
