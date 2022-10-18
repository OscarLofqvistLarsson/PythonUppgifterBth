def pattern(n):
    if n == 1:
        return "*"
    if n == 2:
        return "**"
    return "<" + pattern(n - 2) +  ">"

print(pattern(4))