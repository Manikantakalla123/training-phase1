num=int(input("enter any number:"))
i=s=sum=0
while(i<=num):
    if(i%2==0):
        s=s+i
    else:
        sum=sum+i
    i+=1
print("sum of even numbers",s)
print("sum of odd numbers",sum)
