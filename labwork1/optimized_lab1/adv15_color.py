color=['blanc','noir','xanh','red','violet','burgundy','banana yellow']

cl=input('enter ur color: ')
if cl in color:
    print(f'yes its index is: {color.index(cl)}')
else:
    print('not in mine')