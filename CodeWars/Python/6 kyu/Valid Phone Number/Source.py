import re

def validPhoneNumber(phoneNumber):
    return True if re.findall('\(\d\d\d\) \d\d\d-\d\d\d\d', phoneNumber) and not any([x.isalpha() for x in phoneNumber]) else False