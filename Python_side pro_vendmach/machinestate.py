class MachineState:

  def __init__(self):
    self.valid_coins = ['1', '5', '10', '50']
    self.coins = []
    self.invalid_coins = []
    self.products = {}
    self.selected_product = None
    self.balance = 0
    self.reset = False
  
  def accept(self, coin):
    if (coin in self.valid_coins):
      self.coins.append(int(coin))
      self.balance += int(coin)
      return "COIN ACCEPTED"
    else:
      self.invalid_coins.append(coin)
      return "INVALID COIN"

  def display(self):
    #total_coins = sum(self.coins)
    message = self.build_message(self.balance)
    self.selected_product = None

    return message

  def build_message(self, total_coins):
    if self.selected_product:
        return self.display_with_selected_product(total_coins)
    elif (self.reset == True):
        return self.refund()
    else:
        return self.display_without_selected_product(total_coins)

  def display_without_selected_product(self, total):
    if (total > 0.0):
      #self.balance = total
      return ""

    return "INSERT COIN"

  def display_with_selected_product(self, total):
    if (total == self.products[self.selected_product]):
        self.balance = total - self.products[self.selected_product]
        return "THANK YOU"
    else:
        self.balance = total - self.products[self.selected_product]
        return "PRICE %s" % self.format_amount(self.products[self.selected_product])

  def format_amount(self, amount):
    return "%s" % "{0}".format(amount)

  def check_return_slot(self):
    return self.invalid_coins

  def clear_return_slot(self):
    self.invalid_coins = []
    self.coins = []
    self.balance = 0
    self.reset = False

  def select_product(self, product):
    self.selected_product = product

  def refund(self):
    if (self.balance == 0):
        self.clear_return_slot()
        return "NO COIN RETURN"
    else:
        tmp = str(self.balance)
        self.clear_return_slot()
        return ("RETURN " + tmp)
