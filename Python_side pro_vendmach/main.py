import sys
#import numpy as np
import product
import machinestate


ms = machinestate.MachineState()
pr = product.Product()
ga = product.GreenteaDrinkA()
gb = product.GreenteaDrinkB()
gc = product.GreenteaDrinkC()
gd = product.GreenteaDrinkD()
rt = product.RedTeaDrink()
rb = product.RedbullDrink()
sy = product.SoyDrink()

ms.accept('10')
ga._label = 'a'
gb._label = 'b'
gc._label = 'c'
gd._label = 'd'

plist = [ga, gb, gc, gd]
ldict = dict()


def pannel(im):

    print("\ncurrent balance: {0}".format(ms.balance))
    for i in plist:
        if ((ms.balance >= i._price) and (i._balance > 0)):
            i._aoruna = 'available'
        elif (0 >= i._balance):
            i._aoruna = 'sold out'
        else:
            i._aoruna = 'unavailable'
        
        ldict[i._label] = i
        
        print("{0}. {1} - balance {2}, price {3} - {4}".format(i._label, i._name, i._balance, i._price, i._aoruna))
        
    print(im)
    #print(im)
    print("please insert coin(1,5,10,50), enter REFUNDS to return coins, or enter labels to choose product:\n")




pannel(ms.display())
#print(ldict['a']._balance) 

for i in plist:
    ms.products.update({i._label : i._price})
    ldict.update({i._label : i})

while True:

    inputC = input()
    if (inputC == "REFUNDS"):
        ms.reset = True
        pannel(ms.display())
    elif (inputC in ldict):
        ms.selected_product = inputC
        if (ldict[inputC]._aoruna == 'available'):
            ldict[inputC]._balance -= 1
            pannel(ms.display())
        else:
            pannel("What you choose is {0}".format(ldict[inputC]._aoruna))
        
    else:
        pannel(ms.accept(inputC))
	

	

