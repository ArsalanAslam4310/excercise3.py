def search_from_list(lis,targets):
    
    for i in range(len(lis)):
        if lis[i]==targets:
            return i
        for j in range(1,len(targets)-1):
            if targets[j]==lis[i]:
                print(targets)
                return j
      

lis=[5,4,7,8,1,2,10,55,44]
target=[7,8,1]
search=search_from_list(lis,target)
print(search)
