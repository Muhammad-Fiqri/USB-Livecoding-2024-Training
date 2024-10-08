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
            
        possible, change = break_up(change,None)
        possible_list.append(possible)

        print(possible_list)
        print()

        for i in possible_list:
            for j in i:
                if j > 5000:
                    print(j)
                    possible, change = break_up(j,j)
                    print(possible)
                    print()
                    possible_list.append(possible)
                else:
                    break
        
        print(possible_list)


def break_up(change,ignore):
    if change == 5000:
        return 5000

    possible = []
    temp = 0
    possible_change = [100000,50000,20000,10000,5000]

    if ignore != None:
        possible_change.remove(ignore)

    while change > 5000:
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