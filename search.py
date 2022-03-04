def search_from_list(lis,targets):
    

    for i in range(len(lis)):
        if lis[i]==targets:
            return i
        for j in range(0,len(targets)-1):
            if targets[j]==lis[i]:
                return i
                
      

lis=[5,6,7,88,1,2,10,55,44]
target=[1,2,10]
search=search_from_list(lis,target)
print(search)