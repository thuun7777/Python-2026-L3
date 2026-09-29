# 28 = 1 2 4 7 14
import math

def check(n):
    x=n
    ch=1

    sqr=int(math.sqrt(x))
    if (sqr==math.sqrt(x)):
        ch-=sqr

    for i in range(2,sqr+1):
        if (x%i==0):
            ch+=i
            ch+=x//i
    return ch

n=int(input("Enter a number? "))

if (check(n)==n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is NOT a perfect number")

#print(check(n))
