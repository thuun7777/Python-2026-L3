m=int(input("Enter m="))
n=int(input("Enter n="))

for i in range(1,n+1):
    if (i==1 or i==n):
        for j in range(1,m+1):
            print("*  ", end="")
        print("")
    else:
        print("*",end="")
        for j in range(2,m):
            print("   ", end="")
        print("  *")