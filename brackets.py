def is_correct_bracket_seq(expression):
    left_stack = []
    for i in expression:
        if i == '(' or i == '[' or i == '{':
            left_stack.append(i)
        elif i == ")":
            if len(left_stack) == 0 or left_stack[-1] != '(':
                return False
            else:
                left_stack.pop()
        elif i == ']':
            if len(left_stack) == 0 or left_stack[-1] != '[':
                return False
            else:
                left_stack.pop()
        elif i == '}':
            if len(left_stack) == 0 or left_stack[-1] != '{':
                return False
            else:
                left_stack.pop()
    if len(left_stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    cmd = input()
    print(is_correct_bracket_seq(cmd))
