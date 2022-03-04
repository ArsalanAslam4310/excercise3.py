def find_first_occurence(lis, target):
    '''
    find first occurence of sub array
    '''
    k = 0
    flag = True
    target_index = 0
    for i in range(len(lis)):
        if lis[i] == target[0]:
            k = i+1
            target_index = i
            for j in range(1, len(target)-1):
                if lis[k] == target[j]:
                    k += 1
                    continue
                else:
                    flag = False
                    break

    if flag:
        return target_index
    return -1


lis = [5, 6, 7, 8, 1, 2, 6, 7, 8]
target = [6, 7, 8]
search = find_first_occurence(lis, target)
print(search)
