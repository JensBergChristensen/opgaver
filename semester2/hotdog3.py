"""
Vi kan nu købe brød og beregne subtotal. Vi har derfor indført en total, der
sættes til 0, før vi regner det hele sammen.
"""

class Bread():
   def __init__(self, cheap):
      self.cheap = cheap
      self.price = 5
      self.cheapPrice = 2
   def getPrice(self):
      return self.cheapPrice if self.cheap else self.price

class Sausage():
   def __init__(self, cheap):
      self.cheap = cheap
      self.price = 10
      self.cheapPrice = 9
   def getPrice(self):
      return self.cheapPrice if self.cheap else self.price

class TotalOrder():
   def __init__(self):
      self.__liBread = []
      self.__liSausage = []
      self.__liHotdog = []
   def hotdog(self):
      newSausage = Sausage(True)
      newBread = Bread(True)
      newHotdog = Sausage.getPrice(newSausage) + Bread.getPrice(newBread)
      self.__liHotdog.append(newHotdog)
   def sausage(self):
      newSausage = Sausage(False)
      self.__liSausage.append(newSausage)
   def expensiveBread(self):
      newBread = Bread(False)
      self.__liBread.append(newBread)
   def cheapBread(self):
      newBread = Bread(True)
      self.__liBread.append(newBread)
   def showSubTotal(self):
      self.__total = 0
      for bread in self.__liBread:
         self.__total = self.__total + bread.getPrice()
      for sausage in self.__liSausage:
         self.__total = self.__total + sausage.getPrice()
      for hotdog in self.__liHotdog:
         self.__total = self.__total + hotdog
      print("Subtotal: " + str(self.__total))
   def pay(self):
      pass

# Hovedprogram:

def showMenuCard():
   print("MENU-KORT:\n")
   print("1) Hotdog")
   print("2) Pølse")
   print("3) Dyrt brød")
   print("4) Billigt brød")
   print("5) Se subtotal og fortsæt")
   print("6) Afslut køb og vis total")

if __name__ == "__main__":
   order = TotalOrder()
   runMenu = True
   while runMenu:
      showMenuCard()
      n = input("\nHvad skulle det være? ")
      if n == "1":
         order.hotdog()
      elif n == "2":
         order.sausage()
      elif n == "3":
         order.expensiveBread()
      elif n == "4":
         order.cheapBread()
      elif n == "5":
         order.showSubTotal()
      elif n == "6":
         order.pay()
         runMenu = False
      print()
