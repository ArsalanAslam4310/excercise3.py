from codecs import namereplace_errors


def twice(lis):
    new_li=[]

    for value in lis:
        value=lis
        new_li+=lis+lis
    return new_li

lis=[4,9]
print(twice(lis))