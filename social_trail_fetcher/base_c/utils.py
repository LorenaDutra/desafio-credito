import datetime
import json
import string
import random


def char_generator(size=10, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def char_digits_generator(size=50, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def name_generator():
    return char_generator()

def address_generator():
    return char_digits_generator()

def company_generator():
    return char_generator()

def value_generator():
    return random.randrange(999)

def status_generator():
    return char_generator()

def contract_generator():
    return random.randrange(999)

def date_generator():
    """Generate a random datetime between `start` and `end`"""
    start = datetime.datetime.strptime(
        '1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
    end = datetime.datetime.strptime('1/1/2018 4:50 AM', '%m/%d/%Y %I:%M %p')
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

def datetime_serializer(obj):
    if isinstance(obj, datetime.datetime):
        return obj.__str__()

def person_trail_serializer(person_trail):
    person_dict = person_trail.to_son().to_dict()
    return json.loads(json.dumps(person_dict, default=datetime_serializer))
