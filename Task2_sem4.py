# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

user_num = int(input("Введите число: "))
start_num = 2
my_list = []
N = user_num
while start_num <= user_num:
    if user_num % start_num == 0:
        my_list.append(start_num)
        user_num //= start_num
        start_num = 2
    else:
        start_num += 1
print(f"Простые множители числа {N} следующие: {my_list}")