#Part 3
colors = ["red", "blue", "green", "yellow"]

#blue
if 'blue' in colors:
    print("There is blue")
else:
    print("There is no blue")
#purple
if 'purple' in colors:
    print("There is purple")
else:
    print("There is no purple")

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user = int(input("Type a number: "))
if user in number_list:
    print(f'{user} is in the list')
else:
    print('Your number is not in the list')
