import pygame


class Ship():

	def __init__(self, screen):
		self.screen = screen


		self.image = pygame.image.load("images/ship.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()


		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False 
		self.moving_down = False

		self.ms = 10


	def blit_me(self):

		self.screen.blit(self.image, self.rect) 

	def update_moving(self):

		if self.moving_right and self.rect.right < self.screen_rect.right:
			
			self.rect.centerx += self.ms

		if self.moving_left and self.rect.left > 0:

			self.rect.centerx -= self.ms

		if self.moving_up and self.rect.top > 0:

			self.rect.centery -= self.ms

		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:

			self.rect.centery += self.ms




