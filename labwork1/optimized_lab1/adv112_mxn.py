mcols=int(input("how many columns? "))
nrows=int(input("how many rows? "))
print("*  " * mcols)
for i in range (0,nrows-2):
    print(''.join(["*  ", "   " * (mcols-2), "*"]))
print("*  " * mcols)