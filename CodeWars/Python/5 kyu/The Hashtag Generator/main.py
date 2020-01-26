import re
def generate_hashtag(s):
    return '#' + ''.join([x.capitalize() for x in re.findall("[A-Za-z]+", s)]) if len(s) <= 140 and s else False