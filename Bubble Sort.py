
num = str(input('Enter the number to be sorted: '))

list_digits = list(int(x) for x in num)
num_size = len(str(num))

for a in range(num_size-1):
    swap = 0
    for i in range(num_size - 1):

        if list_digits[i] > list_digits[i + 1]:
            list_digits[i], list_digits[i + 1] = list_digits[i + 1], list_digits[i]
            swap += 1

    if swap == 0:
        break

print('Sorted list: ' + str(list_digits))
print('No. of iterations: ' + str(a))
