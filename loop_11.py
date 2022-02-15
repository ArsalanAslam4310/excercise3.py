prev_number=0
current_number=0
next_number=prev_number+current_number
sum = 0
while next_number <= 10:
    prev_number=current_number
    current_number=next_number
    next_number= prev_number+current_number

    if next_number%2==0:
        sum = sum +next_number
print(sum)
