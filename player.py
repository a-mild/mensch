import pygame as pg

class Player(object):
	def __init__(self, _id, name, color):
		# from sprites.meeple import Meeple
		self._id = _id
		self.name = name
		self.color = color

		self.meeples = pg.sprite.Group()
		self.number_throws = 3
		self._meeples_out = 4
		self._meeples_home = 0
		self._action = 'roll'
		self._stuck = False

	@property
	def action(self):
		return self._action

	@action.setter
	def action(self, value):
		self._action = value
		if value == "move":
			print("Move your ass {}!".format(self.name))

	@property
	def meeples_out(self):
		self._meeples_out = len(
			[1 for m in self.meeples if m.occupied_field.idx == -1])
		return self._meeples_out

	@property
	def meeples_home(self):
		return len([1 for m in self.meeples if m.fields_moved > 39])

	# @meeples_home.setter
	# def meeples_home(self, value):
	# 	self._meeples_home = value
	# 	if self._meeples_home == 4:
	# 		print("Spieler {} hat gewonnen!".format(self.name))
	# 		del self

	@property
	def stuck(self):
		self._stuck = False
		if self.number_throws <= 1:
			self._stuck = True
			for meeple in self.meeples:
				print("meeple hat feld:", meeple.allowed_field)
				if meeple.allowed_field:
					self._stuck = False
					break
		print("stuck", self._stuck)
		return self._stuck

	def set_allowed_fields(self, boardfields, homefields, number):
		banned_fields = set([meeple.occupied_field for meeple in self.meeples])
		banned_fields.add(None)
		# print(banned_fields)
		for meeple in self.meeples:
			# current_field_idx = meeple.occupied_field.idx
			# print("current field:", current_field_idx)
			print(meeple.fields_moved)
			if meeple.fields_moved == -6:
				if number == 6:
					allowed_field = boardfields.get_sprite(self._id*10)
				else:
					allowed_field = None
			elif meeple.fields_moved < 40:
				a, b = divmod((meeple.fields_moved + number), 40)
				if a == 0:
					allowed_field = boardfields.get_sprite((self._id*10+b)%40)
				elif a > 0:
					if b < 4:
						allowed_field = homefields.get_sprite(self._id*4 + b)
						for i in range(b):
							idx = self._id*4 + i
							if not homefields.get_sprite(idx).occupied_by is None:
								allowed_field = None
								print("kann nicht über meeple springen", i)
								break
					else:
						allowed_field = None
			elif meeple.fields_moved >= 40:
				a, b = divmod(meeple.fields_moved - 40 + number, 4)
				if a == 0:
					current_idx = self._id*4 + (meeple.fields_moved - 40) % 3
					field_idx = current_idx + number
					allowed_field = homefields.get_sprite(field_idx)
					for idx in range(current_idx+1, field_idx+1):
						if not homefields.get_sprite(idx).occupied_by is None:
							allowed_field = None
							print("kann nicht über meeple springen", idx)
							break
				else:
					allowed_field = None
			if allowed_field:
				print("allowed field:", allowed_field.idx)
			if not allowed_field in banned_fields:
				allowed_field.admissable = True
				meeple.allowed_field.add(allowed_field)

