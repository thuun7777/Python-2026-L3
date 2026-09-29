l=[1,4,5,-1,10]
def sol(l):
    ls = [x for x in l if x%2==0]
    return ls
print(sol(l))