import random

def generate_id(prefix):
    number = random.randint(1000, 9999)
    return f"{prefix}{number}"

def is_valid_name(text):
    if text is None:
        return False
    return len(text.strip()) > 0

def is_positive_number(value):
    try:
        number = float(value)
        return number > 0
    except ValueError:
        return False

def is_valid_seat_count(value, available_seats):
    try:
        seats = int(value)
    except ValueError:
        return False

    if seats <= 0:
        return False

    if seats > available_seats:
        return False

    return True