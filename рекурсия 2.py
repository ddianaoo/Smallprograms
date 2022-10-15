def b(s):
    if len(s)==0:
        return s
    if s[0]=='(':
        return s[0] + b(s[1:]) + ')'
    return s[0] + b(s[1:]) + s[0]
j = input()
print(b(j))

