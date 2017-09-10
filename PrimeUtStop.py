y = 'y'
i = 1


def prime(x):
    ctr = 0
    for num in range(1, x+1):
        if x % num == 0:
            ctr += 1

    if ctr > 2:
        return False
    else:
        return True

while y == 'y' or y == 'Y':

    prime_or_not = prime(i)

    if prime_or_not == True:
        print(str(i) + " is prime.")
    else:
        print(str(i) + " is not prime")

    y = input("Do want to continue(y/n): ")

    i += 1




