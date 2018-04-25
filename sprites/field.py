import pygame as pg
import yaml

BG_COLOR = (158, 184, 108)
BLACK = pg.Color('black')

class Field(pg.sprite.Sprite):
	def __init__(self, point, radius, idx, color=(255, 255, 255)):
		pg.sprite.Sprite.__init__(self)
		# self.fieldtype = fieldtype
		self.radius = radius
		self.color = color
		self._admissable = False
		self.idx = idx

		self.image = self.initial_field_drawing()
		self.rect = self.image.get_rect()
		self.rect.center = point

	@property
	def admissable(self):
		return self._admissable

	@admissable.setter
	def admissable(self, value):
		self._admissable = value
		print("change color")
		if self._admissable == True:
			self.change_fieldcolor(pg.Color('gray'))
		else:
			self.change_fieldcolor(pg.Color('white'))

	def update(self):
		
		return

	def initial_field_drawing(self):
		img = pg.Surface((2*self.radius, 2*self.radius)).convert()
		img.fill(BG_COLOR)
		pg.draw.circle(img, self.color, (self.radius, self.radius), self.radius, 0)
		pg.draw.circle(img, BLACK, (self.radius, self.radius), self.radius, 3)
		return img

	def change_fieldcolor(self, new_color):
		pg.draw.circle(self.image, new_color, (self.radius, self.radius), self.radius)



