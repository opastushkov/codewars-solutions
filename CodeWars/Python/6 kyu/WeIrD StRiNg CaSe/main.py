def to_weird_case(s):
    ls = []
    
    for x in s.split():
        text = ''
        for i in range(len(x)):
            text += x[i].lower() if i % 2 else x[i].upper() 
        ls.append(text)
        
    return ' '.join(ls)