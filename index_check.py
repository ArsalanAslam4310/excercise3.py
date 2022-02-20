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




def index_checks(list_of_numbers,value):
    for i in range(len(list_of_numbers)):
        sorting=bubble_sort(list_of_numbers[i:])
        if list_of_numbers[i]==value:
            return i

list_of_numbers=[5,25,5,4,8745,451,7]
print(index_checks(list_of_numbers,7))
