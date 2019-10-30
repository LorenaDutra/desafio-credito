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
