from datetime import datetime

def add_current_time(f):
    def wrapped(*args, **kwargs):
        return f(datetime.utcnow(), *args, **kwargs)
    return wrapped

@add_current_time
def test(time, a, b):
    print('Я получил аргументы', a, b, 'at', time)

print(test(1,2))
