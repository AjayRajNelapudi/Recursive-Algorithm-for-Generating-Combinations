class Combinations:
	def __init__(self, n , r):
		self.arr = [1] * int(r)
		self.init_value = 0
		self.i = -1
		self.recursion_count = 0
		self.count = 0

	def generate_combinations(self, n, r):
		self.i += 1

		if r == 0:
			yield self.arr
		else:
			if self.i != 0:
				self.init_value = self.arr[self.i-1]

			self.arr[self.i] = self.init_value + 1

			for x in range(self.arr[self.i], int(n) + 1):
				self.arr[self.i] = x
				yield from self.generate_combinations(n, r - 1)
		self.i -= 1



n = int(input('Enter n = '))
r = int(input('Enter r = '))
generator = Combinations(n, r)
generator = generator.generate_combinations(n, r)
try:
	while(True):
		data = next(generator)
		print(data)
except StopIteration as se:
	print('Done')