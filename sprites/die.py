from random import randint
import numpy as np

import pygame as pg
from pygame.locals import *

ROLL_EVENT = USEREVENT

class Die(pg.sprite.Sprite):
	"""Sprite for the die"""
	size = pg.display.get_surface().get_height() // 36 * 8
	image = pg.Surface((size, size)).convert()
	image.fill((255, 255, 255))
	pg.draw.lines(image,
			(0, 0, 0),		# black
			True,			# connects last to first point
			[(0, 0), (size, 0), (size, size), (0, size)],
			size//20)			# line width
	ONE = 1 / 5 * np.array([
		(2.5, 2.5)])
	TWO = 1 / 5 * np.array([
		[1.0, 4.0],
		[4.0, 1.0]])
	THREE = 1 / 5 * np.array([
		[1.0, 4.0],
		[2.5, 2.5],
		[4.0, 1.0]])
	FOUR = 1 / 5 * np.array([
		[1.0, 1.0],
		[1.0, 4.0],
		[4.0, 1.0],
		[4.0, 4.0]])
	FIVE = 1 / 5 * np.array([
		[1.0, 1.0],
		[1.0, 4.0],
		[4.0, 1.0],
		[4.0, 4.0],
		[2.5, 2.5]])
	SIX = 1 / 5 * np.array([
		[1.0, 1.0],
		[1.0, 2.5],
		[1.0, 4.0],
		[4.0, 1.0],
		[4.0, 2.5],
		[4.0, 4.0]])
	NUMBERS = [ONE, TWO, THREE, FOUR, FIVE, SIX]


	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = Die.image.copy()
		self.rect = self.image.get_rect()
		f = pg.display.get_surface().get_height() // 36
		self.rect.topleft = (f * 38, f * 2)
		self._number = randint(1,6)
		self.draw_number()
		self.rolling = False
		self.roll_speed = 250		# how fast the die shows a new number [ms]

	@property
	def number(self):
		return self._number

	@number.setter
	def number(self, value):
		self._number = value
		self.draw_number()

	def start_roll(self):
		self.rolling = True
		pg.time.set_timer(ROLL_EVENT, self.roll_speed)

	def stop_roll(self, player):
		self.number = randint(1, 6)
		self.rolling = False
		self.roll_speed = 250
		pg.time.set_timer(ROLL_EVENT, 0)
		print('Es wurde eine {} gewürfelt!'.format(self.number))
		# if self.number == 6:
			# print("{} hat einen Extrawurf!".format(player.name))


	def roll(self):
		self.number = randint(1, 6)
		pg.time.set_timer(ROLL_EVENT, self.roll_speed)
		self.roll_speed = round(self.roll_speed**1.53)
		print(self.roll_speed)

	def on_click(self):
		if not self.rolling:
			print("Die is rolling now!")
			self.start_roll()
		else:
			print('Lass den Würfel rollen!')

	def update(self):
		pass

	def draw_number(self):
		self.image = Die.image.copy()
		for pip in Die.NUMBERS[self.number-1]:
			pg.draw.circle(
				self.image,
				(0, 0, 0),
				(self.size*pip).astype(int),
				self.size//10)					# radius
