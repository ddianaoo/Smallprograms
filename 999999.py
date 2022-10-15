a = [1, 2, 3]
try:
    print(a[4])
except IndexError as e:
    print(e)
