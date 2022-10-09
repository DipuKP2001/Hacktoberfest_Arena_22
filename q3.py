n=int(input("Enter the number: "))
count=0
print("The number of steps :",end=" ")
while(n>0):
    if n==1:
        break
    elif n%2==0:
        n=n/2
        count=count+1
    elif n%3==0:
        n=n/3
        count=count+1
    else:
        n=n-1
        count=count+1
print(count)
