import math
a={'x':1, 'y':2}
b={'x':3, 'y':4}
def getDistance(a,b):
    x=a['x']-b['x']
    x*=x
    y=b['y']-a['y']
    y*=y

    res=x+y
    res=math.sqrt(res)

    return res


print(f"{getDistance(a,b):.4f}")
