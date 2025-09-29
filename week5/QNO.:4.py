def infix_to_postfix(expr):
    prec = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    assoc = {'^': 'R'}
    stack, out = [], []
    for c in expr:
        if c.isalnum(): out.append(c)
        elif c == '(': stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(': out.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and (
                prec[c] < prec[stack[-1]] or
                (prec[c] == prec[stack[-1]] and assoc.get(c) != 'R')
            ): out.append(stack.pop())
            stack.append(c)
    while stack: out.append(stack.pop())
    return ''.join(out)
