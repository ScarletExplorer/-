numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
corect1 = numbers[:4]+numbers[5:]
sum_nubers = sum(corect1)
count_of_nubers = len(numbers)
number = sum_nubers/count_of_nubers
numbers [4] = number

print("Измененный список:",numbers)