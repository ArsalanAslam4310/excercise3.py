lis=[21,5,4,7,9,1,42]
lis1=[4,1,9]

lis1[:] = [item for item in lis1 if item in lis.values()]

        
print(lis1)
