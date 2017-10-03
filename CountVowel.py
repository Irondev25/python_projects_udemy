string = input("Enter String: ")

ctr = 0
vowel = []

for letter in string:
    if letter == 'a' or letter == 'A':
        ctr += 1
        vowel.append(letter)
    elif letter == 'e' or letter == 'E':
        ctr += 1
        vowel.append(letter)
    elif letter == 'i' or letter == 'I':
        ctr += 1
        vowel.append(letter)
    elif letter == 'o' or letter == 'O':
        ctr += 1
        vowel.append(letter)
    elif letter == 'u' or letter == 'U':
        ctr += 1
        vowel.append(letter)

print("Their are " + str(ctr) + " vowel")
print(vowel)
