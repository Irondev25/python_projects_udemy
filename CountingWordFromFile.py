filepath = input("Enter your file path(i.e c:/desktop/example.txt):")
file = open(filepath, 'r')

data = file.read()
print(data)
list = data.split(' ')
print('their are ' + str(len(list)) + ' words.')
print(list)
