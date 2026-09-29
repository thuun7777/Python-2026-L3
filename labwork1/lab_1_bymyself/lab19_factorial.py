def factorial1(x):
    if (x<=1):
        return 1
    res=1
    for i in range(2,x+1):
        res*=i
    return res

def factorial2(x):
    if (x<=1):
        return 1
    else: return factorial2(x-1)*x


n=int(input("Enter a number: "))
print(factorial2(n))
