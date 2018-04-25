import pygame as pg

# import globalvars as g


class Player(object):
	def __init__(self, _id, name, color):
		from sprites.meeple import Meeple
		self._id = _id
		self.name = name
		self.color = color

		self.meeples = pg.sprite.Group()
		self._meeples_out = 4
		self.number_throws = 3
		self._action = 'roll'

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
			[1 for m in self.meeples if m.occupied_field.idx == 0])
		return self._meeples_out

	def set_allowed_fields(self, boardfields, number):
		for meeple in self.meeples:
			current_field = meeple.occupied_field.idx
			print(current_field)
			if current_field == 0:
				if number == 6:
					allowed_field_idx = self._id*10
				else:
					allowed_field_idx = None
			else:
				allowed_field_idx = current_field + number -1
			print(allowed_field_idx)
			if not allowed_field_idx is None:
				allowed_field = boardfields.get_sprite(allowed_field_idx)
				allowed_field.admissable = True
				meeple.allowed_field.add(allowed_field)
