def camel_case(s):
    return ''.join([x.capitalize() for x in s.split() if x])