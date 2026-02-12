def isBalanced(s):
    st = []

    for c in s:

        # If opening bracket → push to stack
        if c == '(' or c == '{' or c == '[':
            st.append(c)

        # If closing bracket → check stack
        elif c == ')' or c == '}' or c == ']':
            if not st:
                return False

            top = st[-1]

            if ((c == ')' and top != '(') or
                (c == '}' and top != '{') or
                (c == ']' and top != '[')):
                return False

            st.pop()

    # If stack is empty → balanced
    return not st


print(isBalanced("{[()]}"))