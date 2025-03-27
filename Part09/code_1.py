# Write your solution here:
class Item:
  def __init__(self,name,weight):
    self.__name = name
    self.__weight = weight

  def name(self):
    return self.__name
  
  def weight(self):
    return self.__weight
  
  def __str__(self):
    return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
  def __init__(self,max_weight):
    self.__max_weight = max_weight
    self.__items = []

  def add_item(self,item):
    added_weight = 0

    for i in self.__items:
      added_weight += i.weight()
    
    if item.weight() + added_weight <= self.__max_weight:
      self.__items.append(item)
   
  def print_items(self):
    for item in self.__items:
      print(item)
 
  def weight(self):
    total_weight = 0

    for item in self.__items:
      total_weight += item.weight()

    return total_weight

  def __str__(self):
    total_weight = 0

    for item in self.__items:
      total_weight += item.weight()

    return f"{len(self.__items)} {"items" if len(self.__items) != 1  else "item"} ({total_weight} kg)"
  
  def heaviest_item(self):
    if len(self.__items) == 0:
      return None
    
    heaviest_item_in_suitcase = self.__items[0]
    heaviest_item_weight = self.__items[0].weight()

    for item in self.__items:
      if item.weight() > heaviest_item_weight:
        heaviest_item_in_suitcase = item
        heaviest_item_weight = item.weight()

    return heaviest_item_in_suitcase

class CargoHold:
  def __init__(self,max_weight):
    self.__max_weight = max_weight
    self.__suitcases = []

  def add_suitcase(self,suitcase):
    added_weight = 0
    
    for suit_case in self.__suitcases:
      added_weight += suit_case.weight()
    
    if added_weight + suitcase.weight() <= self.__max_weight:
      self.__suitcases.append(suitcase)

  def __str__(self):
    added_space = 0

    for suitcase in self.__suitcases:
      added_space += suitcase.weight()

    remaining_space = self.__max_weight - added_space
    
    return f"{len(self.__suitcases)} {"suitcases" if len(self.__suitcases) != 1 else "suitcase"}, space for {remaining_space} kg"

  def print_items(self):
    for suitcase in self.__suitcases:
      suitcase.print_items()
