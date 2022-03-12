import pygame



class Bullet():

	def __init__(self, screen, ship):

		self.fire = False

		self.screen = screen
		self.image = pygame.image.load("images/bullet.bmp")
		self.rect = self.image.get_rect()
		self.ship_rect = ship.rect

		self.rect.centery = self.ship_rect.centery
		self.rect.right = self.ship_rect.right

	def blit_bullet(self):

		
		self.screen.blit(self.image, self.rect)


	def update_bullet_mv(self):

		if self.fire:

			self.rect.centerx += 15

	
		
		
		