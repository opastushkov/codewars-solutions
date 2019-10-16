import re
def order(s):
  return ' '.join(sorted(s.split(), key=lambda x: re.findall("\d", x)))