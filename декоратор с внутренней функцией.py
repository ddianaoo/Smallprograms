def my_decorator(f):
    def wrapped(*args, **kwargs):
        print('До функции')
        response = f(*args, **kwargs)
        print('После функции')
        return response
    print('декорируем', f)
    return wrapped

@my_decorator
def my_function(a, b):
    print('В функции')
    return a + b
print(my_function(1,2))
