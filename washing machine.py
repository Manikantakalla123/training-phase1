weight=int(input("enter the weight of clothes:"))
water=str(input("enter the level oof water "))
if weight>0 and weight<=2000 and water=="low":
    print("estimated time: 25 minutes")
elif weight>2000 and weight<=4000 and water=="medium":
    print("estimated time: 35 minutes")
elif weight>4000 and weight<=7000 and water=="high":
    print("estimated time: 45 minutes")
elif weight>7000:
    print("INVALID INPUT")
else:
    print("time estimated: 0 minutes")