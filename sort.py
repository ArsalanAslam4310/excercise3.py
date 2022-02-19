def find_index(list_of_number,start,value):
    for i in range(start,len(list_of_number)):
        if list_of_number[i] == value:
            return i

def bubble_sort(list_of_numbers,order=True):

    for i in range(len(list_of_numbers)):
        min_index=find_index(list_of_numbers,i,min(list_of_numbers[i:])) #index of the minimum number in the list
        
        list_of_numbers[i],list_of_numbers[min_index]=list_of_numbers[min_index],list_of_numbers[i]

    if not order:
        list_of_numbers.reverse()

    return list_of_numbers   


list_of_number=[52,6562,5455,555,2202,52]
print(bubble_sort(list_of_number))
