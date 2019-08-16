def solution(s, marks):
    ls = s.split('\n')
    res = []
    for x in ls:
        check = True
        line = ''
        for s in x:
            if s in marks:
                check = False
            if check: line = line + s
        print(line)
        res.append(line.rstrip())
    return '\n'.join(res)