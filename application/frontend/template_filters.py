import dateutil


def dateformat(value, format = '%-d %B %Y'):
    new_date =dateutil.parser.parse(value, dayfirst=True)
    return new_date.strftime(format)

def datetimeformat(value, format = '%-d %B %Y at %H:%M:%S'):
    norm = dateutil.parser.parse(value)
    return norm.strftime(format)

def currency(value):
    """Format a comma separated  currency to 2 decimal places."""
    return "{:,.2f}".format(float(value))
