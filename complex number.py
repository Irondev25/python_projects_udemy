import cmath
complex_number_1 = str(input("Enter 1st complex number(x+iy): "))
complex_number_2 = str(input("Enter 2nd complex number(x+iy): "))

list_1 = complex_number_1.split('+i')
list_2 = complex_number_2.split('+i')


def addition():
    sum_x = float(list_1[0]) + float(list_2[0])
    sum_y = float(list_1[1]) + float(list_2[1])
    print("%s + i%s" %(sum_x, sum_y))

def subtraction():
    sub_1 = float(list_1[0]) - float(list_2[0])
    sub_2 = float(list_1[1]) + float(list_2[1])
    print("%s + i%s" % (sub_1, sub_2))


def multiplication():
    list_1[1] = list_1[1] *



complex()
