import unittest
from application import dateformat, datetimeformat, currency


class TemplateFiltersTestCase(unittest.TestCase):

    def test_dateformat(self):
        formatted = dateformat('14/01/2014')
        self.assertEquals(formatted, '14 January 2014')

        formatted = dateformat('01/01/2014')
        self.assertEquals(formatted, '1 January 2014')

        formatted = dateformat('02/01/2014')
        self.assertEquals(formatted, '2 January 2014')

        formatted = dateformat('2014-01-02')
        self.assertEquals(formatted, '2 January 2014')

        formatted = dateformat('2014/01/02')
        self.assertEquals(formatted, '2 January 2014')

        formatted = dateformat('14.01.02')
        self.assertEquals(formatted, '14 January 2002')


        formatted = dateformat('99.01.02')
        self.assertEquals(formatted, '2 January 1999')

        formatted = dateformat('02 January 2014')
        self.assertEquals(formatted, '2 January 2014')


    def test_datetimeformat(self):
        formatted = datetimeformat('14/01/2014 23:23:25.1231+01:01')
        self.assertEquals(formatted, '14 January 2014 at 23:23:25')

        formatted = datetimeformat('14/01/14 23:23:25.1231+01:01')
        self.assertEquals(formatted, '14 January 2014 at 23:23:25')

        formatted = datetimeformat('2013-01-02 08:23:25.1231+01:01')
        self.assertEquals(formatted, '2 January 2013 at 08:23:25')


    def test_currency(self):
        self.assertEquals(currency(80000), '80,000.00')




