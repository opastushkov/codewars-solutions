import re
def validate_pin(pin):
    return bool(re.match("\d{4}\Z|\d{6}\Z", pin)) 