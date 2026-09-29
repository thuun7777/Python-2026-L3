l=[1,4,5,-1,10]
def extract_even(ls):
    n=len(ls)
    i=0
    while (i<len(ls)):
        if (ls[i]%2 ==1):
            del(ls[i])
            n-=1
        else:
            i+=1
        #print(ls[i])
        
    return ls

#print(l)
extract_even(l)
print(l)