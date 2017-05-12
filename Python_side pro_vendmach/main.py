import sys
import numpy as np
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

ms.accept(10)
ga._label = 'a'
gb._label = 'b'
gc._label = 'c'
gd._label = 'd'
ms.products = {ga._name : ga._price, gb._name : gb._price, gc._name : gc._price, gd._name : gd._price,}
plist = [ga, gb, gc, gd]

def pannel(mes):
    print("current balance: {0}".format(ms.balance))
    for i in plist:
        print("{0}. {1} - balance {2}, price {3}".format(i._label, i._name, i._balance, i._price))
    print(mes)
    print("please insert coin(1,5,10,50), enter REFUNDS to return coins, or enter labels to choose product:")


while True:
    pannel("")

    inputC = input()
    if (inputC == "REFUNDS"):
	    pannel(ms.refund())
    else:
        pannel(ms.accept(int(inputC)))
	

	

