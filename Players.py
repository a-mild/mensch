from random import choice
from itertools import cycle
from sortedcontainers import SortedDict
from  collections import OrderedDict

players = {1: 'a', 2: 'b', 3: 'c'}

sd = SortedDict(players)

print(sd)
sd.index('a')
sdc = cycle(sd.viewvalues())

print(next(sdc))
sd.pop(2)
print(next(sdc))

print(next(sdc))


# class Players(OrderedDict):
# 	def __iter__(self):
# 		return iter(self.values())

# 	def __next__(self):
# 		return


# 	def choose_starting_player(self):
# 		self.players = list(self.values())
# 		starting_player = choice(list(self.values()))
# 		self.i = list(self.items())
# 		print(self.i)
# 		return starting_player




# p = Players(players)

# starting_player = p.choose_starting_player()

# print(starting_player)

# for player in p:
# 	print(player)


