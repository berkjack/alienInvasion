import pygame

from settings import Settings

from ship import Ship

import gameFunctions as gf

from bullet import Bullet





def run_game():
	
	pygame.init()
	ai_settings = Settings()
	

	screen = pygame.display.set_mode((ai_settings.width, ai_settings.height))
	
	pygame.display.set_caption("for my lovely Sevval!")
	
	ship = Ship(screen)
	bullet = Bullet(screen, ship)
	clock = pygame.time.Clock()
	bullets = []
	

	while True:
		clock.tick(ai_settings.fps)
		
		gf.check_events(ship, screen, bullets, ai_settings) # Event checking loop from gameFunctions.
		ship.update_moving()
		for bullet in bullets:
			bullet.update_bullet_mv()
		gf.bullet_control(bullets, screen)
		gf.update_screen(ai_settings, screen, ship, bullets) # Screen updating code from gameFunctions.


run_game()

