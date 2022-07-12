#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
def is_weekend(data):
    return data == 6 or data == 7

day = int(input())
if is_weekend(day) == 1:
    print('Да')
else:
    print('Нет')