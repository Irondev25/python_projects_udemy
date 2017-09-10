print("Welcome to card validator")

card_number = str(input("Enter your card number: "))

split_card_number = []

#splitting the number
for i in card_number:
    split_card_number.append(int(i))


odd = []
even = []


#separating the number
for i in split_card_number:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)


sum_odd = 0
sum_even = 0

#summation of odd numbers
for i in odd:
    sum_odd += i


#summation of even number as per luhn algorithm
for i in range(len(even)):
    even[i] *= 2


for i in even:
    if len(str(i)) == 2:
        i = str(i)
        sum_even = int(i[0]) + int(i[1])
    else:
        sum_even += i


total = sum_odd + sum_even

if total%10 == 0:
    print("Card is valid")
else:
    print("Card is invalid")