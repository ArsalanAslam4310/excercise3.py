def minimum_number(list_of_number):
    min = list_of_number[0]
    for number in list_of_number:
       if min > number:
        min = number
    return min


def bubble_sort(list_of_number):
    search_index=0
    temp=0
    min=0
    
    for index in range(len(list_of_number)):
        min = minimum_number(list_of_number[index:])
        search_index = list_of_number.index(min)
        temp=list_of_number[index]
        list_of_number[index]=min
        list_of_number[search_index]=temp
        return list_of_number

list_of_number=[6,1225,212,21,545,2]
sorted=bubble_sort(list_of_number)
print(sorted)