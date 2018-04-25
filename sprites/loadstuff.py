import pygame as pg
# from pygame.locals import *

pg.init()

def load_image(path):
	"""Load an image as surface and convert it. 
	Return an image and rect object"""
	image = pg.image.load(path)
	if image.get_alpha() is None:
		image = image.convert()
	else:
		image = image.convert_alpha()
	image_rect = image.get_rect()
	return image, image_rect

def change_color_of_image(image, from_color, to_color):
	"""Change the color of an image object. Return the recolored image"""
	img_copy = image.copy()

	width, height = img_copy.get_size()
	for x in range(width):
		for y in range(height):
			if img_copy.get_at((x, y)) == from_color:
				img_copy.set_at((x, y), to_color)
	return img_copy