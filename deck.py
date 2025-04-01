# OOP (Object Oriented Programming) is different of functional programing. OOP focus on the same variable, changing that variable, is good when you dont need new variables, when all happens around
# the same object, in the case of this program, all happen around 4 pile of 'decks', Hand, Cemetery, Castle and Tavern, everything will be around then.

# Do I make 4 classes or make one class and modules that I will apply only to especific intances?

class Deck:
  def __init__(self,list_of_card):
    self.list_of_cards=list_of_cards

  def discard(self,list_to_discard):
    pass
