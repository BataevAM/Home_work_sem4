#Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной 
# последовательности.

my_list = list(map(int, input("Задайте список. Введите числа через пробел:\n").split()))
new_list = []
[new_list.append(i) for i in my_list if i not in new_list]
print(f"Неповторяющиеся элементы списка -> {new_list}")