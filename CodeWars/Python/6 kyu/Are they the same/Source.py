from collections import Counter

def comp(a1, a2):
    return Counter([x**2 for x in a1]) == Counter(a2) if a1 != None and a2 != None else False
    
	