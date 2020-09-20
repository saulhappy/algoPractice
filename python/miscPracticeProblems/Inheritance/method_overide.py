# -*- coding: utf-8 - *-

# Define a Clothing superclass with wear and sell instance methods.
# The wear method should return the string “I'm wearing this fashionable piece of clothing!”
# The sell method should return the string “Buy my piece of clothing!”

# Define a Socks subclass that inherits from the Clothing superclass.
# It should define a lose_one instance method that
# returns the string “Where did my other one go?”
# It should override the wear method to
# return the string “Take a look at my socks! They're gorgeous!”
# It should override the sell method to
# return the string “Buy my socks!”

class Clothing():
    def wear(self):
        return "I'm wearing this fashionable piece of clothing!"

    def sell(self):
        return "Buy my piece of clothing!"


class Socks(Clothing):
    def lose_one(self):
        return "Where did my other one go?"

    def wear(self):
        return "Take a look at my socks! They're gorgeous!"

    def sell(self):
        return "Buy my socks!"
