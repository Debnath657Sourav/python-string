def isBalanced(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return "NO"
            stack.pop()
        else:
            # Invalid character (not a bracket)
            return "NO"

    return "YES" if not stack else "NO"
