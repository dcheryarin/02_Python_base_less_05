my_f = open('exercise4.txt')
for i, num_str in enumerate(my_f):
    with open("exercise4_out.txt", "a") as file:
        if (i) == 0:
            new_line = num_str.replace('One', 'один')
            file.write(new_line)
        elif (i) == 1:
            new_line = num_str.replace('Two', 'два')
            file.write(new_line)
        elif (i) == 2:
            new_line = num_str.replace('Three', 'три')
            file.write(new_line)
        elif (i) == 3:
            new_line = num_str.replace('Four', 'четыре')
            file.write(new_line)
#        print(new_line, end='')
my_f.close()
