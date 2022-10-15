def a(n, c=0):
    if n < 10:
        return n, c
    c += 1
    return a(n%10+n//10, c)
print(*a(int(input())))
