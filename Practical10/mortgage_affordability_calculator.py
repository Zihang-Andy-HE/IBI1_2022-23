def mort_afford(value, salary):
    print('Can you afford the house?')
    if value <= 5*salary:
        print("Yes")
    else:
        print("No")
    
mort_afford(500, 110)
