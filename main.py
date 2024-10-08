def ChangeCounter(amount, day):
    max_day = 2
    fee = 5000
    change = 0

    #change must be inputed lowest first

    if day > 2:
        print("max day of parking is 2 days")
    else:
        change = amount - (fee * day)

        print(change)
        possible_list = []
            
        possible, change = break_up(change)
        
        possible_list.append(possible)

        print(possible_list)

def break_up(change):
    possible = []
    temp = 0
    possible_change = [100000,50000,20000,10000,5000]
    while change > 0:
        for i in possible_change:
            if i <= change:
                temp += i
                change -= i
                possible.append(i)
                #print(i)
                #print(change)
                #print(possible)
                break
    
    return possible, change

ChangeCounter(50000,2)