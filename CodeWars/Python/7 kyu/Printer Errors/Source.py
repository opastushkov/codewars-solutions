import re
def printer_error(s):
    return "{}/{}".format(len(s) - len(re.findall('[a-m]', s)), len(s))