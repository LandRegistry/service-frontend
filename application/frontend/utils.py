import requests

from flask import current_app
from flask import abort

def get_or_log_error(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as e:
        current_app.logger.error("HTTP Error %s", e)
        abort(response.status_code)
    except requests.exceptions.ConnectionError as e:
        current_app.logger.error("Error %s", e)
        abort(500)


import requests

from flask import current_app
from flask import abort

def get_or_log_error(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as e:
        current_app.logger.error("HTTP Error %s", e)
        abort(response.status_code)
    except requests.exceptions.ConnectionError as e:
        current_app.logger.error("Error %s", e)
        abort(500)


class Address(object):

    def __init__(self, string_address):
        self.structured = None
        self.string = StringAddress(string_address)

class StructuredAddress(object):

    def __init__(self, house_no, street_name, town, postcode, postal_county, region_name, country):
        self.house_no = house_no
        self.street_name = street_name
        self.town = town
        self.postcode = postcode
        self.postal_county = postal_county
        self.region_name = region_name
        self.country = country

class StringAddress(object):

    def __init__(self, string_address):
        self.string_address = string_address

    def get_fields(self):
        fields = self.string_address.split(',')
        fields = [item.strip() for item in fields]
        return fields

    def get_string(self):
        return self.string_address


class AddressBuilder(object):

    def __init__(self, house_no, street_name, town, postcode, postal_county, region_name, country, full_address):
        self.house_no = house_no
        self.street_name = street_name
        self.town = town
        self.postcode = postcode
        self.postal_county = postal_county
        self.region_name = region_name
        self.country = country
        self.full_address = full_address
        self.minimal_viable_address_fields = ["house_no", "street_name", "town", "postcode"]


    def build(self):

        address = Address(self.full_address)

        have_minimum_required_data = True
        for field in self.minimal_viable_address_fields:
            if not self.__dict__[field] or self.__dict__[field].isspace() :
                have_minimum_required_data = False
                break
        if have_minimum_required_data and self.county_and_region_empty():
            have_minimum_required_data = False

        if have_minimum_required_data:
            address.structured = StructuredAddress(self.house_no, self.street_name, self.town, self.postcode, self.postal_county, self.region_name, self.country)

        return address

    def county_and_region_empty(self):
        county = self.postal_county.replace(" ","")
        region = self.region_name.replace(" ","")
        if not county and not region:
            return True
        return False


