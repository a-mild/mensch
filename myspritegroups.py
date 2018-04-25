from pygame import Rect
from pygame.sprite import AbstractGroup

class AllSpritesGroup(AbstractGroup):
	def __init__(self):
		AbstractGroup.__init__(self)

	def get_sprites_at(self, pos):
		colliderect = Rect(pos, (0, 0))
		colliding_idx = colliderect.collidelistall(self.sprites())
		print(colliding_idx)
		colliding_sprites = [self.sprites()[idx] for idx in colliding_idx]
		if not colliding_sprites:
			return None
		elif len(colliding_sprites) == 1:
			return colliding_sprites[-1]
		else:
			return colliding_sprites

class NumberedGroup(AbstractGroup):
	def __init__(self):
		AbstractGroup.__init__(self)
		self._spritelist = []


	def add_internal(self, sprite):
		AbstractGroup.add_internal(self, sprite)
		self._spritelist.append(sprite)

	def get_sprites_at(self, pos):
		colliderect = Rect(pos, (0, 0))
		colliding_idx = colliderect.collidelistall(self._spritelist)
		colliding_sprites = [self._spritelist[idx] for idx in colliding_idx]
		if not colliding_sprites:
			return None
		elif len(colliding_sprites) == 1:
			return colliding_sprites[-1]
		else:
			return colliding_sprites

	def get_idx_at(self, pos):
		colliderect = Rect(pos, (0, 0))
		return colliderect.collidelistall(self._spritelist)

	def get_sprite(self, idx):
		try:
			return self._spritelist[idx]
		except IndexError:
			return None

# class MeepleGroup(AbstractGroup):
# 	def __init__(self):
# 		AbstractGroup.__init__(self)

# 	def get_sprites_at(self, pos):
# 		colliderect = Rect(pos, (0, 0))
# 		colliding_idx = colliderect.collidelistall(list(self.spritedict))
# 		colliding_sprites = [self._spritelist[idx] for idx in colliding_idx]
# 		if not colliding_sprites:
# 			return None
# 		elif len(colliding_sprites) == 1:
# 			return colliding_sprites[-1]
# 		else:
# 			return colliding_sprites
