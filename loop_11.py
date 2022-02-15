prev_number=0
current_number=0
next_number=prev_number+current_number

for i in range(10):
    prev_number=current_number
    current_number=next_number
    next_number= prev_number+current_number
    print(next_number)

    
