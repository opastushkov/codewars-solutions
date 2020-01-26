import re

def domain_name(url):
    return re.findall("[\/\.](.+)\.", url)[0].lstrip("/")