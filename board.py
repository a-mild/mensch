from math import cos, sin, pi
import yaml
import pygame as pg
from sprites.field import Field






def rotate(point, origin, angle):
	"""Rotate a point (px, py) around an origin (ox, oy) by an angle.
	Rounds to an integer.
	Used to create the field sprites more easily."""
	ox, oy = origin
	px, py = point

	qx = ox + cos(angle)*(px-ox) - sin(angle)*(py-oy)
	qy = oy + sin(angle)*(px-ox) + cos(angle)*(py-oy)
	return round(qx), round(qy)

class Board(object):
	with open('config/fields.yaml') as f:
		relative_field_points = yaml.load(f)

	def __init__(self):
		from sprites.meeple import Meeple

		fieldsize = self.boardsize // 27
		counter_boardfields = 0
		counter_homefields = 40
		for i in range(4):
			for fieldtype in Board.relative_field_points:
				for rel_point in Board.relative_field_points[fieldtype]:
					point = [self.boardsize//18*coord for coord in rel_point]
					point = rotate(point, self.boardorigin, i*pi/2)
					if fieldtype == 'out':
						if self.players[i]:
							color = self.players[i].color
							field = Field(point, fieldsize, -1, color)
							self.allfields.add(field)
							meeple = Meeple(self.players[i], field)
							self.players[i].meeples.add(meeple)
							self.allmeeples.add(meeple)
						else:
							self.allfields.add(Field(point, fieldsize))
					elif fieldtype == 'home':
						if self.players[i]:
							color = self.players[i].color
						self.homefields.add(Field(point, fieldsize, counter_homefields, color))
						counter_homefields += 1
					else:
						self.boardfields.add(Field(point, fieldsize, counter_boardfields))
						counter_boardfields += 1


class HUD(object):
	def __init__(self):
		from sprites.die import Die
		#draw the die
		self.die = Die()
		self.die_group.add(self.die)


class GUI(Board, HUD):
	def __init__(self):
		Board.__init__(self)
		HUD.__init__(self)

