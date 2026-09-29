colorlist=["purple","yellow","red","pink","bleu","verte","noir","blanc","maroon"]

color=input("What is your favorite color? ")
ch=0
for i in colorlist:
    if (color==i):
        print(f"Your color is at index {ch} in my list")
        break

    #print(f"{ch}. {i}")
    ch+=1
if (ch+1>len(colorlist)):
    print(f"Sorry, I could not find your color")
    