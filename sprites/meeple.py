import pygame as pg
# from .loadstuff import load_image

pg.init()

class Meeple(pg.sprite.Sprite):
	"""Create a meeple of desired color at desired coordinates"""
	image = pg.image.load("C:/Users/Alex/Python/mensch/media/meeple.png")
	image = image.convert_alpha()
	size = pg.display.get_surface().get_height() // 27 * 2
	image = pg.transform.scale(image, (size, size))

	def __init__(self, player, field):
		pg.sprite.Sprite.__init__(self)
		self.player = player
		self.occupied_field = field
		self.allowed_field = pg.sprite.Group()

		self.image = Meeple.image
		self.change_color_of_image((0, 0, 0), self.player.color)
		self.rect = self.image.get_rect()
		self.rect.center = self.occupied_field.rect.center

		self.grabbed = False

	def update(self, number):
		if self.grabbed:
			self.rect.center = pg.mouse.get_pos()
		else:
			self.rect.center = self.occupied_field.rect.center

	def on_click(self):
		print("Meeple from {} was grabbed!".format(self.player.name))
		self.grabbed = True

	def drop(self, fieldgroup):
		""" Drop the meeple on a field. Move back to where it got grabbed if it's not dropped on a field"""
		field = fieldgroup.get_sprites_at(pg.mouse.get_pos())
		if field in self.allowed_field:
			print("Dropping meeple!")
			self.grabbed = False
			self.occupied_field = field
			self.occupied_field.admissable = False
			self.player.number_throws = 0
			self.player.action = "roll"
			return True
		else:
			self.grabbed = False
			print("Can't drop meeple here!")
			return False

	def change_color_of_image(self, from_color, to_color):
		w, h = self.image.get_size()
		for x in range(w):
			for y in range(h):
				if self.image.get_at((x, y)) == from_color:
					self.image.set_at((x, y), to_color)

