import sys

import pygame as pg
from pygame.locals import *

ROLL_EVENT = USEREVENT

class InputHandler():
	def __init__(self):
		pass

	def on_leftbutton_down(self):
		player = self.active_player
		action = self.active_player.action
		clicked_sprite = self.allsprites.get_sprites_at(self.event.pos)
		if (action == 'roll') & (clicked_sprite in self.die_group):
			self.die.on_click()
		elif (action == 'move') & (clicked_sprite in player.meeples):
			self.grabbed_meeple = clicked_sprite
			self.grabbed_meeple.on_click()
		else:
			print("{} has to {} now!".format(player.name, action))

	def on_leftbutton_up(self):
		try:
			if self.grabbed_meeple:
				if self.grabbed_meeple.drop(self.boardfields):
					for meeple in self.active_player.meeples:
						meeple.allowed_field.empty()
						print(meeple.allowed_field)
					self.grabbed_meeple = []
					if self.die.number == 6:
						self.active_player.number_throws = 1
					# del self.grabbed_meeple
					# self.active_player = next(self.players_cycle)
		except AttributeError:
			pass


	def on_rightbutton_down(self):
		return

	def on_midbutton_down(self):
		return

	def on_event(self, event):
		self.event = event
		if event.type == QUIT:
			self.running = False
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				self.on_leftbutton_down()
			elif event.button == 2:
				self.on_midbutton_down()
			elif event.button == 3:
				self.on_rightbutton_down()
		elif event.type == MOUSEBUTTONUP:
			if event.button == 1:
				self.on_leftbutton_up()
			elif event.button == 2:
				self.on_midbutton_up()
			elif event.button == 3:
				self.on_rightbutton_up()

		elif event.type == ROLL_EVENT:
			if self.die.roll_speed < 2000:
				self.die.roll()
			else:
				self.die.stop_roll(self.active_player)
				if self.active_player.meeples_out == 4:
					if self.die.number == 6:
						self.active_player.action = "move"
						self.active_player.set_allowed_fields(
							self.boardfields, self.die.number)
					else:
						self.active_player.number_throws -= 1
						print("Noch {} Würfe über!".format(self.active_player.number_throws))
				else:
					self.active_player.action = "move"
					self.active_player.set_allowed_fields(
						self.boardfields, self.die.number)
