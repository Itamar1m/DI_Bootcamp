from random import randint, random
class Gene:
	def __init__(self):
		self.value = randint(0,1)
	def mutate(self):
		self.value = int(not bool(self.value))
	def __repr__(self):
		return f"{self.value}"
class Chromosome:
	def __init__(self):
		self.value = [Gene() for _ in range(10)]
	def mutate(self):
		for gene in self.value:
			if random() > 0.5:
				gene.mutate()
	def __repr__(self):
		return f"{self.value}"
class DNA:
	def __init__(self):
		self.value = [Chromosome() for _ in range(10)]
	def __repr__(self):
		return f"{self.value}"

        # Dunder
# Double Under
# Methods that start and end with 2 underscores
# Dunder methods are exactly like normal methods / function
# Except. They run automatically under certain circumstances...
# __repr__   show a string representation of the class
# it runs wheneve a variable is dumped in the terminal