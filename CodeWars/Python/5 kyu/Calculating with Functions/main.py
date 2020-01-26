def zero(op_arg=None): 
    if op_arg:
        op, arg = op_arg
        if op == '+': return 0 + arg
        elif op == '-': return 0 - arg
        elif op == '*': return 0 * arg
        elif op == '/': return 0 // arg
    else: return 0
    
def one(op_arg=None): 
    if op_arg:
        op, arg = op_arg
        if op == '+': return 1 + arg
        elif op == '-': return 1 - arg
        elif op == '*': return 1 * arg
        elif op == '/': return 1 // arg
    else: return 1
    
def two(op_arg=None): 
    if op_arg:
        op, arg = op_arg
        if op == '+': return 2 + arg
        elif op == '-': return 2 - arg
        elif op == '*': return 2 * arg
        elif op == '/': return 2 // arg
    else: return 2
    
def three(op_arg=None):
    if op_arg:
        op, arg = op_arg
        if op == '+': return 3 + arg
        elif op == '-': return 3 - arg
        elif op == '*': return 3 * arg
        elif op == '/': return 3 // arg
    else: return 3
    
def four(op_arg=None): 
    if op_arg:
        op, arg = op_arg
        if op == '+': return 4 + arg
        elif op == '-': return 4 - arg
        elif op == '*': return 4 * arg
        elif op == '/': return 4 // arg
    else: return 4
    
def five(op_arg=None):
    if op_arg:
        op, arg = op_arg
        if op == '+': return 5 + arg
        elif op == '-': return 5 - arg
        elif op == '*': return 5 * arg
        elif op == '/': return 5 // arg
    else: return 5
    
def six(op_arg=None): 
    if op_arg:
        op, arg = op_arg
        if op == '+': return 6 + arg
        elif op == '-': return 6 - arg
        elif op == '*': return 6 * arg
        elif op == '/': return 6 // arg
    else: return 6
    
def seven(op_arg=None): 
    if op_arg:
        op, arg = op_arg
        if op == '+': return 7 + arg
        elif op == '-': return 7 - arg
        elif op == '*': return 7 * arg
        elif op == '/': return 7 // arg
    else: return 7

def eight(op_arg=None): 
    if op_arg:
        op, arg = op_arg
        if op == '+': return 8 + arg
        elif op == '-': return 8 - arg
        elif op == '*': return 8 * arg
        elif op == '/': return 8 // arg
    else: return 8
    
def nine(op_arg=None): 
    if op_arg:
        op, arg = op_arg
        if op == '+': return 9 + arg
        elif op == '-': return 9 - arg
        elif op == '*': return 9 * arg
        elif op == '/': return 9 // arg
    else: return 9

def plus(arg): return ('+', arg) 
def minus(arg): return ('-', arg)
def times(arg): return ('*', arg)
def divided_by(arg): return ('/', arg)