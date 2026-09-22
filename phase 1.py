def check(expression):
    stack = []

    for ch in expression:
        if ch == '(' or ch == '[' or ch == '{':
            stack.append(ch)

        elif ch == ')' or ch == ']' or ch == '}':
            if len(stack) == 0:
                return False

            top = stack.pop()

            if ch == ')' and top != '(':
                return False
            if ch == ']' and top != '[':
                return False
            if ch == '}' and top != '{':
                return False

    return len(stack) == 0


expression = input("Enter an expression: ")

if check(expression):
    print("Balanced Parentheses")
else:
    print("Not Balanced Parentheses")