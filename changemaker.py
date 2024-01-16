import math
def value_of_change(change):
    total = change[0][0] + change[0][1]*5 + change[0][2]*10 + change[0][3]*20 + change[0][4]*50 + change[0][5]*100
    total += change[1][0]*.01 + change[1][1]*.05 + change[1][2]*.1 + change[1][3]*.25
    return total

# (singles, fives, tens, twentys, fifties, hundreds)
def bills(money):
    money = math.floor(money)
    singles = 0
    fives = 0
    tens = 0
    twentys = 0
    fifties = 0
    hundreds = 0
    
    if money >= 100:
        hundreds = math.floor(money / 100)
        money -= hundreds * 100
    
    if money >= 50:
        fifties = math.floor(money / 50)
        money -= fifties * 50
        
    if money >= 20:
        twentys = math.floor(money / 20)
        money -= twentys * 20
        
    if money >= 10:
        tens = math.floor(money / 10)
        money -= tens * 10
        
    if money >= 5:
        fives = math.floor(money / 5)
        money -= fives * 5
    
    if money >= 1:
        singles = math.floor(money / 1)
        money -= singles * 1
    
    return (singles, fives, tens, twentys, fifties, hundreds)

# (pennies, nickles, dimes, quarters)
def coins(money):
    money = money - int(money)
    money = round(money, 2)
    pennies = 0
    nickles = 0
    dimes = 0
    quarters = 0
    
    if money >= 0.25:
        quarters = math.floor(money / 0.25)
        money -= quarters * 0.25
    
    if money >= 0.10:
        dimes = math.floor(money / 0.10)
        money -= dimes * 0.10
        
    if money >= 0.05:
        nickles = math.floor(money / 0.05)
        money -= nickles * 0.05
        
    money = round(money, 2)
    if money >= 0.01:
        pennies = math.floor(money / 0.01)
        money -= pennies * 0.01
    
    return (pennies, nickles, dimes, quarters)

def make_change(total_charge, payment):
    money = payment - total_charge
    # print(round(money, 2))
    return(bills(money), coins(money))

total = float(input("Total payment: "))
payment = float(input("Money paid: "))
print(make_change(total, payment))
print(value_of_change(make_change(total, payment)))