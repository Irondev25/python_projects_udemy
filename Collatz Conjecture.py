number = int(input("Enter a number(n > 1): "))

ctr = 0

while number != 1:
    if number % 2 == 0:
        number = number / 2
        print(number)
        ctr += 1
    else:
        number = (number * 3) + 1
        print(number)
        ctr += 1

print(ctr)

