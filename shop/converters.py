import datetime

class FourDigitYearConverter:
    regex = r'\d{4}'

    def to_python(selfself, value):
        if 2010 <= int(value) <= datetime.datetime.now():
            return int(value)
        else:
            return None

    def to_url(self, value):
        return '{%04d}'.format(value)