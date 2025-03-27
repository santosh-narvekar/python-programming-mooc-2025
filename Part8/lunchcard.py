# Write your solution here:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = float(balance)

    def eat_lunch(self):
       if self.balance - 2.60 > 0:
          self.balance -= 2.60

    def eat_special(self):
      if self.balance - 4.60 > 0:
        self.balance -= 4.60

    def deposit_money(self,amount):
      if amount >= 0:
        self.balance += amount
      else:
        raise ValueError("You cannot deposit an amount of money less than zero")
      
    def __str__(self):
      return f"The balance is {round(self.balance,1)} euros"

peters_card = LunchCard(20)
graces_card = LunchCard(30)

peters_card.eat_special()
graces_card.eat_lunch()

print(f"Peter:",peters_card)
print(f"Grace:",graces_card)

peters_card.deposit_money(20)
graces_card.eat_special()

print(f"Peter:",peters_card)
print(f"Grace:",graces_card)

peters_card.eat_lunch()
peters_card.eat_lunch()

graces_card.deposit_money(50)

print(f"Peter:",peters_card)
print(f"Grace:",graces_card)
