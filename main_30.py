def profit_checker(food_price, discount_gofood, cashback_grabfood):
    #cashback is much more profitable when it's ratio to discount is 20%
    #cashback dont cut price, just return cash
    #Discount cut price by the percentage

    if cashback_grabfood - discount_gofood >= 20:
        #cashback is more profitable
        print("Choose: Grab Food")
        cashback_get = food_price * cashback_grabfood
        print("Harga yang harus di bayar:",food_price)
        print("Cashback:",cashback_get)
    else:
        #discount is more profitable
        price_to_pay = food_price - (food_price * discount_gofood / 100)
        print("Choose: Go Food")
        print("Price:",price_to_pay)


profit_checker(45000,20,30)
print()
profit_checker(60000,10,30)