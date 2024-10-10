from math import factorial
line = list(input().split())
op = "+-*/~#@!"
stack = []
for ch in line:
    if ch not in op:
        stack.append(int(ch))
    else:
        match ch:
            case "+":
                n1 = stack[-2]
                stack.pop(-2)
                n2 = stack[-1]
                stack.pop(-1)
                stack.append(n1 + n2)
            case "-":
                n1 = stack[-2]
                stack.pop(-2)
                n2 = stack[-1]
                stack.pop(-1)
                stack.append(n1 - n2)
            case "*":
                n1 = stack[-2]
                stack.pop(-2)
                n2 = stack[-1]
                stack.pop(-1)
                stack.append(n1 * n2)
            case "/":
                n1 = stack[-2]
                stack.pop(-2)
                n2 = stack[-1]
                stack.pop(-1)
                stack.append(n1 // n2)
            case "~":
                stack[-1] = (-1) * stack[-1]
            case "#":
                stack.append(stack[-1])
            case "!":
                stack[-1] = factorial(stack[-1])
            case "@":
                n3 = stack[-1]
                stack.pop(-1)
                n2 = stack[-1]
                stack.pop(-1)
                n1 = stack[-1]
                stack.pop(-1)
                stack += [n2, n3, n1]

print(*stack)