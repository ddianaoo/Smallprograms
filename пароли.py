import random
digits= "0123456789"
lowercase_letters="abcdefghijklmnopqrstuvwxyz"
uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation="'!#$%&*+-=?@^_."
punc2="il1Lo0O"
chars = ''
count=input("Количество паролей для генерации: - ")
lenght=int(input("Длина одного пароля: - "))
digit=input("Включать ли цифры 0123456789? Да, Нет: - ")
Alpha=input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Да, Нет: - ")
alpha=input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Да, Нет: - ")
symbol=input("Включать ли символы !#$%&*+-=?@^_? Да, Нет: - ")
errsymbol=input("Исключать ли неоднозначные символы il1Lo0O? Да, Нет: - ")
punc="il1Lo0O"

right= int(count)
while right!=0:

    while len(chars)!=lenght:
        if digit.lower()=="да":
            chars+=random.choice(digits)
            if len(chars)==lenght:
                print(chars)
                break
        if Alpha.lower()=="да":
            chars += random.choice(uppercase_letters)
            if len(chars)==lenght:
                print(chars)
                break
        if alpha.lower()=="да":
            chars += random.choice(lowercase_letters)
            if len(chars)==lenght:
                print(chars)
                break
        if symbol.lower()=="да":
            chars += random.choice(punctuation)
            if len(chars)==lenght:
                print(chars)
                break
        if punc.lower()=="нет":
            chars += random.choice(punc2)
            if len(chars)==lenght:
                print(chars)
                break
        if len(chars)<lenght:
            continue
    chars = ""
    right-=1
    if right!=0:
        continue
