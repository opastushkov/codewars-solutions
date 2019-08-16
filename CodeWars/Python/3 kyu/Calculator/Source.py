class Calculator(object):
  def evaluate(self, s):
    expression = [float(x) if x not in '*/+-' else x for x in s.split()]

    pr = {'*': 1,
          '/': 1,
          '-': 0,
          '+': 0,
          }

    postfix_notation = []
    stack = []

    for x in expression:
        if str(x) not in '*/+-':
            postfix_notation.append(x)
        else:
            if not stack or pr[stack[-1]] < pr[x]:
                stack.append(x)
            else:
                while stack and pr[stack[-1]] >= pr[x]:
                    postfix_notation.append(stack.pop(-1))
                stack.append(x)

    while stack:
        postfix_notation.append(stack.pop(-1))

    for x in postfix_notation:
        if x == '+': stack.append(stack.pop(-1) + stack.pop(-1))
        elif x == '-': stack.append(stack.pop(-2) - stack.pop(-1))
        elif x == '*': stack.append(stack.pop(-1) * stack.pop(-1))
        elif x == '/': stack.append(stack.pop(-2) / stack.pop(-1))
        else: stack.append(x)

    return stack[0]

              
        