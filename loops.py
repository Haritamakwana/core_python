for x in range(1,10):
    print(x)

no=int(input("enter no. :"))
rev=0
while no>0:
    rem=no%10
    no=no//10
    rev=rev*10+rem
print("rev is:",rev)
