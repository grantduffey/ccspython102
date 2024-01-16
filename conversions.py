def ctof(C):
    return (float(C) * 9/5) + 32
    
def ftoc(F):
    return (float(F) - 32) * 5/9

C = input("Temp in C? ")
print("%.2f" % ctof(C))
F = input("Temp in F? ")
print("%.2f" % ftoc(F))
