number = int(input("enter a number: "))
list = []


def primeCheck(x):
    ctr = 0
    for i in range(1,x+1):
        if x%i == 0:
            ctr+=1
    if ctr<=2:
        return False
    else:
        return True


def primeYielder():
    ctr = 0
    for i in range(2,number+1):
        if primeCheck(i) == False:
            yield i



g = primeYielder()


y = next(g)


while primeCheck(number):
    if number%y == 0:
        number = number / y
        list.append(y)
        print(y)
    else:
        y = next(g)


list.append(number)

print(list)








