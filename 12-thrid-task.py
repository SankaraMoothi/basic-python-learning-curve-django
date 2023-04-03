# convert weight to Pounds And Kg

# 1kg=2.204 pound ,1pound=453.59gram

weight=float(input("Enter the Weight: "))
unit=input("(K)g Or (L)lb: ")
if unit.upper()=="K":
    converted=weight/0.45
    print("Weight in Lbs: ",converted)
elif unit.upper()=="L":
    converted=weight*0.45
    print("Weight in Lbs: ",converted)
else:
    print("Choose Correct Unit..")