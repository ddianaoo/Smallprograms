import random
name = input( 'Как вас зовут? ' )
print(f' {name}, добро пожаловать в числовую угадайку!')
n = input('Введи правую границу: ' )
num = random.randint(1,int(n))
counter = 0

def is_valid(user_num):
    if 0 < int(user_num) < int(n)+1:
        return True
    else:
        return False

while True:
    user_num = input(f'Введи предпологаемое число от 1 до {int(n)}: ' )
    if is_valid(user_num):
        user_num  = int(user_num) 
        if num != user_num:
            counter += 1
            if user_num < num:
                print(f' {name}, твоё число {user_num} слишком мало, попытайся еще раз!')
                continue
            elif user_num > num:
                print(f' {name}, твоё число {user_num} слишком велико, попытайся еще раз!')
                continue
        else:
            print(f' Молодец, {name}, ты угадала число, количество твоих попыток - {counter+1}')
            break
    else:
        print(f'А может быть все-таки введешь целое число от 1 до {int(n)}?')
print('Спасибо, что сыграла в числовую угадайку. Еще увидимся...')        
