import pygame as pg
# from .loadstuff import load_image

pg.init()

class Meeple(pg.sprite.Sprite):
	"""Create a meeple of desired color at desired coordinates"""
	image = pg.image.load("C:/Users/Alex/Python/mensch/media/meeple.png")
	size = pg.display.get_surface().get_height() // 27 * 2
	image = pg.transform.scale(image, (size, size))
	if image.get_alpha() is None:
		image = image.convert()
	else:
		image = image.convert_alpha()

	def __init__(self, player, field):
		pg.sprite.Sprite.__init__(self)
		self.player = player
		self._occupied_field, self.startfield = field, field
		self.allowed_field = pg.sprite.Group()
		self.fields_moved = -6

		self.image = Meeple.image.copy()
		self.change_color_of_image((0, 0, 0, 255), self.player.color)
		self.image.convert()
		self.rect = self.image.get_rect()
		self.rect.center = self.occupied_field.rect.center

		self.grabbed = False

	@property
	def occupied_field(self):
		return self._occupied_field

	@occupied_field.setter
	def occupied_field(self, field):
		self._occupied_field.occupied_by = None
		if not field.occupied_by is None:
			field.occupied_by.send_home()
		field.occupied_by = self
		self._occupied_field = field

	def update(self):
		if self.grabbed:
			self.rect.center = pg.mouse.get_pos()
		else:
			self.rect.center = self.occupied_field.rect.center

	def on_click(self):
		print("Meeple from {} was grabbed!".format(self.player.name))
		self.grabbed = True

	def drop(self, allfields):
		""" Drop the meeple on a field. Move back to where it got grabbed if it's not dropped on a field"""
		field = allfields.get_sprites_at(pg.mouse.get_pos())
		if field in self.allowed_field:
			self.grabbed = False
			self.occupied_field = field
			for field in allfields:
				field.admissable = False
			self.player.number_throws = 0
			self.player.action = "roll"
			print("Dropping meeple!")
			return True
		else:
			self.grabbed = False
			print("Can't drop meeple here!")
			return False

	def send_home(self):
		print("Beating {}'s meeple!".format(self.player.name))
		self.occupied_field = self.startfield
		self.fields_moved = -6
		self.update()

	def change_color_of_image(self, from_color, to_color):
		w, h = self.image.get_size()
		for x in range(w):
			for y in range(h):
				if self.image.get_at((x, y)) == from_color:
					self.image.set_at((x, y), to_color)
