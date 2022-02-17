list_of_number=[56,6562,5455,555,2202,52]


for index in range(len(list_of_number)):
    min_index=list_of_number.index(min)
    list_of_number[index],list_of_number[min-index]=list_of_number[index]
print(list_of_number)
