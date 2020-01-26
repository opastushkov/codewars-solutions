def to_postfix(infix):
    priority = {'*': 1,
                '/': 1,
                '^': 1,
                '+': 0,
                '-': 0,
                '(': 0
                }
    res = ''
    stack = []
    for x in infix:

        if x.isdigit():
            res += x
        elif x == '(':
            stack.append(x)
        elif x in '*/^+-':
            if not stack or stack[-1] == '(':
                stack.append(x)
            elif priority[x] > priority[stack[-1]]:
                stack.append(x)
            elif priority[x] <= priority[stack[-1]]:
                while stack and stack[-1] != '(':
                        res += stack.pop(-1)
                        if stack and priority[stack[-1]] < priority[x]: break
                stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop(-1)
            if stack and stack[-1] == '(': stack.pop(-1)
    while stack:
        res += stack.pop(-1)

    return res
