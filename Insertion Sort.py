
num = input('Enter the number to be sorted: ')

num_size = len(str(num))
list_digits = list(int(x) for x in num)


def check(place, list_digits):
    if list_digits[place] > list_digits[place + 1]:
        list_digits[place], list_digits[place + 1] = list_digits[place + 1], list_digits[place]

        for i in range(place):
            if list_digits[place] < list_digits[place - 1]:
                list_digits[place], list_digits[place - 1] = list_digits[place - 1], list_digits[place]
                place -= 1
            else:
                break


for i in range(num_size - 1):
    check(i, list_digits)

print('The list sorted in ascending order is: ' + str(list_digits))
