new_list = [el for el in range(10, 20)]
sum = 0
with open("exercise5.txt", "a") as file:
    for element in new_list:
        sum += element
        file.write(str(element))
        file.write(' ')

print('Сумма числе в файле равна:', sum)
