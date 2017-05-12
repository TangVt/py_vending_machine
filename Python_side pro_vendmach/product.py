class Product(object):

    def __init__(self):
        self._name = None
        self._price = None
        self._balance = None
		

    def get_price(self):
        return self._price

class GreenteaDrinkA(Product):
    def __init__(self):
        self._name = 'Greentea'
        self._price = 10
        self._balance = 10
        self._label = None
		
class GreenteaDrinkB(Product):
    def __init__(self):
        self._name = 'Greentea'
        self._price = 15
        self._balance = 10
        self._label = None
		
class GreenteaDrinkC(Product):
    def __init__(self):
        self._name = 'Greentea'
        self._price = 20
        self._balance = 10
        self._label = None
		
class GreenteaDrinkD(Product):
    def __init__(self):
        self._name = 'Greentea'
        self._price = 25
        self._balance = 10
        self._label = None

class RedTeaDrink(Product):
    def __init__(self):
        self._name = 'RedTea'
        self._price = 10
        self._balance = 10
        self._label = None

class RedbullDrink(Product):
    def __init__(self):
        self._name = 'Redbull'
        self._price = 20
        self._balance = 10
        self._label = None
		
class SoyDrink(Product):
    def __init__(self):
        self._name = 'Soy'
        self._price = 25
        self._balance = 10
        self._label = None

'''
class ProductFactory(object):
    @staticmethod
    def create_product(product_type):
        if product_type == 'GreenteaA':
            return GreenteaDrinkA()
		elif product_type == 'GreenteaB':
            return GreenteaDrinkB()
		elif product_type == 'GreenteaC':
            return GreenteaDrinkC()
		elif product_type == 'GreenteaD':
            return GreenteaDrinkD()
        elif product_type == 'RedTea':
            return RedTeaDrink()
        elif product_type == 'Redbull':
            return RedbullDrink()
		elif product_type == 'Soy':
            return SoyDrink()
'''