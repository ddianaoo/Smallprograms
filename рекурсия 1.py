def a(s):
    if len(s)==1:
        return s
    return s[0] + '*' + a(s[1:-1]) + '*' + s[-1]
w = input()
print(a(w))
