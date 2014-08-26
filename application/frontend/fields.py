from wtforms import SelectField
import requests
import csv


class CountriesField(SelectField):
    """
    Loads a list of countries from a URL, and populates a select
    box with the values.

    If the URL points to a CSV file:
    The CSV must contain the country's name, and the country's ISO code.
    TODO The implementation can be changed to allow the user to specify
    the column indexes of said fields in the CSV, but for now it's
    hard-coded for the below CSV.

    The 'top_countries' can contain a list of ISO codes which should be
    excluded from the 'choices', but populated into an 'top_choices'
    instead.
    """

    def __init__(self, label='', validators=None, countries_url=None,
            top_countries=[], **kwargs):
        super(CountriesField, self).__init__(label, validators, **kwargs)
        countries = []
        internal_top_countries = []
        #tuples = self._from_csv_url(countries_url)
        tuples = self._from_csv_file(countries_url)
        # prepend a blank value
        tuples.insert(0, ('',''))
        for tup in tuples:
            if tup[0] in top_countries:
                internal_top_countries.append(tup)
            countries.append(tup)

        # add 'Other'
        internal_top_countries.append(('other', 'Other'))

        self.choices = countries
        self.top_choices = internal_top_countries

    def _from_csv_file(self, csv_file=None):
        if not csv_file:
            csv_file = 'data/countries.csv'
        with open(csv_file, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            return self._tuples_from_csv_reader(reader)

    def _from_csv_url(self, csv_url=None):
        if not csv_url:
            # TODO find an up-to-date hosted countries CSV.
            #+ The one below sadly doesn't have UK.
            csv_url = 'https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/271614/20140108-FCO_Country_Names_v1.csv'

        r = requests.get(csv_url)
        data = r.text
        reader = csv.reader(data.splitlines(), delimiter=',')
        return self._tuples_from_csv_reader(reader)

    def _tuples_from_csv_reader(self, reader):
        tuples = []
        for row in reader:
            tuples.append((row[5], row[0]))
        return tuples

    def iter_top_choices(self):
        for value, label in self.top_choices:
            yield (value, label, self.coerce(value) == self.data)
