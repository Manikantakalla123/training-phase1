#0,0,7,6,14,12,21..........n find 15th and 16th term program in python
a=7
b=6
i=j=temp=1
list=[]
n=int(input("enter n:"))
while (temp<=n):
    if temp%2!=0 :
        list.append(a*(i-1))
        i+=1
    else:
        list.append(b*(j-1))
    temp+=1
print("the () term is()".format(n,list(n-1)))

