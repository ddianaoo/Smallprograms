def my_decorator(f):
    print('decorating', f)
    return f

@my_decorator
def my_function(a, b):
    return a + b
print(my_function(1, 2))
