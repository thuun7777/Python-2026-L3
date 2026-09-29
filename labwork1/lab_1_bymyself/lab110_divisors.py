import math
def getDivisors(x):
    ls=[]
    sqr=int(math.sqrt(x))
    for i in range (1,sqr+1):
        if (x%i==0):
            ls.append(i)
            ls.append(x//i)

    if (sqr==math.sqrt(x)):
        ls.remove(sqr)
    ls.sort()
    return ls

n=int(input("Enter a number: "))

print(f"List of divisors of {n}: {getDivisors(n)}")