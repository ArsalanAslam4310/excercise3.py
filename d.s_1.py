list1=[1,2,3,4,5,6,7,8,9]
list2=[5,15,1,12,21,2,4,5]
list3=[]

odd=list1[1::2]
list3.extend(odd)
even=list2[::2]
list3.extend(even)
print(list3)