lis = [11, 45, 8, 11, 23, 45, 23, 45, 89]
x=lis.count(11)
y=lis.count(45)
z=lis.count(8)
a=lis.count(23)
b= lis.count(89)
lis[x]=11
lis[y]=45
lis[z]=8
lis[a]=23
lis[b]=89
f=x,y,z,a,b
print(f,lis)