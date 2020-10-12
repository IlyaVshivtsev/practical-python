# stock.py

class Stock:

	def __init__(self, name, shares, price):
		self.name = name
		self.shares = shares
		self.price = price

	@property	
	def cost(self):
		return self.shares * self.price
		
	@property
	def shares(self):
		return self._shares

	@shares.setter
	def shares(self, value):
		if not isinstance(int, value):
			raise TypeError('Expected integer')
		self._shares = value
	
	def sell(self, diff):
		self.shares -= diff

	def __repr__(self):
		return f'Stock({self.name:s}, {self.shares:d}, {self.price:0.1f})'