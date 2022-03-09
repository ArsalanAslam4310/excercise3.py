def capital(word):
    x=[]
    for char in word:
        if char.isupper():
            x.append(char)
    return x

print(capital("AdgvghXgsvghGGF"))