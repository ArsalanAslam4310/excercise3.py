def edit(lis,exist,new_occurence):
    for i in range(len(lis)):
        if lis[i]==exist:
            lis[i]=new_occurence
            return lis

lis=[6,5,4,9,3,8,9]
print(edit(lis,8,56))
