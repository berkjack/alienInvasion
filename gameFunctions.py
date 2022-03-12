import sys

import pygame

from bullet import Bullet




def check_events(ship, screen, bullets, ai_settings):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				
				ship.moving_right = True
			
			if event.key == pygame.K_LEFT:
				
				ship.moving_left = True
			
			if event.key == pygame.K_UP:
				
				ship.moving_up = True
			
			if event.key == pygame.K_DOWN:
				
				ship.moving_down = True

		elif event.type == pygame.KEYUP:

			if event.key == pygame.K_RIGHT:
				
				ship.moving_right = False

			if event.key == pygame.K_LEFT:

				ship.moving_left = False

			if event.key == pygame.K_UP:

				ship.moving_up = False

			if event.key == pygame.K_DOWN:

				ship.moving_down = False

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_x or event.key == pygame.K_SPACE:
				
				
				if len(bullets) < ai_settings.bullets_allowed:
					
					new_bullet = Bullet(screen, ship)
					bullets.append(new_bullet)
					new_bullet.fire = True
					
				



def update_screen(ai_settings, screen, ship, bullets):

	screen.fill(ai_settings.bg_color)
	ship.blit_me()
	for bullet in bullets:
		bullet.blit_bullet()
	pygame.display.flip()



def bullet_control(bullets, screen):

	for bullet in bullets:

		if bullet.rect.left > screen.get_rect().right:

			bullets.remove(bullet)
			del bullet