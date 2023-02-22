n=10
k=5
m=int(input())
if m==0 or k>5:
    print("INVALID INPUT")
if m<=k:
    print("NUMBER OF CANDIES SOLD:",m)
    print("NUMBER OF CANDIES AVILABLE:",n-m)

