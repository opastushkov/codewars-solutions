def calc(expr):

    if not expr: return 0
    
    stack = []
    ls = [float(x) if x not in '+-*/' else x for x in expr.split()]
    
    for x in ls:
        if x == '+': stack.append(stack.pop(-1) + stack.pop(-1))
        elif x == '-': stack.append(stack.pop(-2) - stack.pop(-1))
        elif x == '*': stack.append(stack.pop(-1) * stack.pop(-1))
        elif x == '/': stack.append(stack.pop(-2) / stack.pop(-1))
        else: stack.append(x)
        
    return stack[0]