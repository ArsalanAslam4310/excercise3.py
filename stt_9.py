def max_number(list_of_numbers):
    max=0
    for number in list_of_numbers:
        if max<number:
            max=number
    return max

list_of_numbers=[5,4,88,2,15]
x = max_number(list_of_numbers)
print(x)
            