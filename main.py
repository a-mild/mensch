"""
wenn feld schon besetzt von eigenem meeple nicht draufgehen lassen
"""
import sys
from random import choice
from itertools import cycle
from collections import OrderedDict
from sortedcontainers import SortedDict
import yaml

import pygame as pg
from pygame.locals import *
from board import GUI
from player import Player
from inputhandler import InputHandler
from myspritegroups import AllSpritesGroup, NumberedGroup


import globalvars as g

with open('config/players.yaml') as cfg:
	player_default_config = yaml.load(cfg)

SCREENSIZE = (48*18, 36*18)
BG_COLOR = (158, 184, 108)



class App(GUI, InputHandler):

	def __init__(self):
		self.running = True
		pg.init()
		self.screen = pg.display.set_mode(SCREENSIZE)
		pg.display.set_caption("Mensch ärgere dich nicht! :)")
		self.boardsize = self.screen.get_height()
		self.boardorigin = (self.boardsize//2, self.boardsize//2)

		self.background = pg.Surface(self.screen.get_size()).convert()
		self.background.fill(BG_COLOR)
		self.screen.blit(self.background, (0, 0))

		# Init spritegroups
		self.allfields = NumberedGroup()
		self.boardfields = NumberedGroup()
		self.allmeeples = NumberedGroup()
		self.die_group = pg.sprite.GroupSingle()
		self.allsprites = AllSpritesGroup()


	def pregame_menu(self):
		"""Set up the participating players and choose a random starting player
		"""
		self.players = SortedDict({_id: Player(_id, **config)
						for _id, config in player_default_config.items()})
		self.players_cycle = cycle(self.players.viewvalues())
		# set random starting player and synchronize the cycle
		self.active_player = choice(self.players.values())
		while next(self.players_cycle) != self.active_player:
			continue


	def on_execute(self):
		GUI.__init__(self)
		self.allfields.add(self.boardfields)
		self.allsprites.add(self.allmeeples, self.die)
		while self.running:
			if len(self.players) <= 1:
				self.running = False
			if self.active_player.meeples_out == 4:
				self.active_player.number_throws = 3
			else:
				self.active_player.number_throws = 1
			print(self.active_player.name, "am Zug!")
			while self.active_player.number_throws > 0:
				for event in pg.event.get():
					self.on_event(event)
				self.on_loop()
				self.render()
			self.active_player = next(self.players_cycle)


	def on_loop(self):
		self.active_player.meeples.update(1)

	def render(self):
		self.background.fill(BG_COLOR)
		self.screen.blit(self.background, (0, 0))
		self.allfields.draw(self.screen)
		self.allmeeples.draw(self.screen)
		self.die_group.draw(self.screen)
		pg.display.flip()


theApp = App()
theApp.pregame_menu()
theApp.on_execute()
