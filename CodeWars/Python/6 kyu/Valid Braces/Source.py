def validBraces(s):
    bracers = {
                ')': '(',
                '}': '{',
                ']': '[',
    }
    stack = []
    for x in s:
        if x in '({[': stack.append(x)
        elif stack:
            temp = stack.pop(-1)
            if temp == bracers[x]: pass
            else: return False
        else: return False
    return True if not stack else False