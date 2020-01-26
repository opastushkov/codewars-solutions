import re
def getCount(inputStr):
    return len(re.findall("[a,e,i,o,u]", inputStr)) 