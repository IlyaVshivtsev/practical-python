# stock.py

class Stock:

	def __init__(self, name, shares, price):
		self.name = name
		self.shares = shares
		self.price = price

	@property	
	def cost(self):
		return self.shares * self.price
		
	def sell(self, diff):
		self.shares -= diff

	def __repr__(self):
		return f'Stock({self.name:s}, {self.shares:d}, {self.price:0.1f})'