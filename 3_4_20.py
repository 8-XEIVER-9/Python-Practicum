from itertools import product
opers = {'not': 'not', 'and': 'and', 'or': 'or', '^': '!=', '->': '<=', '~': '=='}
prior = {'not': 0, 'and': 1, 'or': 2, '^': 3, '->': 4, '~': 5, '(': 6}


def remake_exp(exp, vars):
    stack = []
    result = []
    exp = exp.replace('(', '( ').replace(')', ' )')

    for item in exp.split():
        if item in vars:
            result.append(item)
        elif item == '(':
            stack.append(item)
        elif item == ')':
            while stack[-1] != '(':
                result.append(opers[stack.pop()])
            stack.pop()
        elif item in opers:
            while stack and prior[item] >= prior[stack[-1]]:
                result.append(opers[stack.pop()])
            stack.append(item)
    while stack:
        result.append(opers[stack.pop()])
    return result


def evaluate(exp, vars):
    stack = []
    for item in exp:
        if item in vars:
            stack.append(vars[item])
        else:
            if item == 'not':
                stack.append(not stack.pop())
            else:
                var2, var1 = stack.pop(), stack.pop()
                stack.append(eval(f'{var1} {item} {var2}'))
    return int(stack.pop())


exp = input()
vars = sorted(set([item for item in exp if item.isupper()]))
remaked_exp = remake_exp(exp, vars)
table = product([0, 1], repeat=len(vars))
print(*vars, 'F')
for values in table:
    globals = {key: value for key, value in zip(vars, values)}
    print(*values, evaluate(remaked_exp, globals))
