
num = str(input('Enter the number to be sorted: '))

list_digits = list(int(x) for x in num)
num_size = len(str(num))
sorted_list = []
#3748920

for i in range(num_size):
    min_digit = min(list_digits)
    list_digits.remove(min_digit)
    sorted_list.append(min_digit)

print(sorted_list)
