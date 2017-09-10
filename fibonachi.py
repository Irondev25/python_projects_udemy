def fibonacci(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        b = a + b
        a = b - a


x = int(input("Enter the number of Fibonacci numbers you want to generate: "))

for i in fibonacci(x):
    print(i)
