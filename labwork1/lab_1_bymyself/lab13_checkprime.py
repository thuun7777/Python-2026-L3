import math
def check(x):
    sqr=int(math.sqrt(x))
    ch=1

    if (sqr==math.sqrt(x)):
        ch=0
        return ch 
  
    for i in range(2,sqr+1):
        if (x%i==0):
            ch=0
            return ch
    return ch


n=int(input("Enter a number? "))

if (check(n)==1):
    print(f"{n} is a prime number")
else:
    print(f"{n} is NOT a prime number")
