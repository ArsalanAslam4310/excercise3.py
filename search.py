def search_from_list(lis,targets):
    for i in range(len(lis)):
        if lis[i]==targets:
            return i
        
    
    

list_of_numbers=[5,4,7,8,1,2,10,55,44]
target=[4,7,8]
search=search_from_list(list_of_numbers,target)
print(search)