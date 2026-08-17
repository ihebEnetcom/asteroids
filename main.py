import sys
import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,PLAYER_RADIUS
from logger import log_state,log_event
from player import Player   
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable =  pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    dt=0.0

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers= (updatable)
    Shot.containers = (updatable,drawable,bullets)

    player=Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2,radius=PLAYER_RADIUS)
    astroid_field = AsteroidField()
    while  True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill("black")


        for updatable_item in updatable:
            updatable_item.update(dt)
        for drawable_item in drawable:
            drawable_item.draw(screen)
        for astroid in asteroids:
            if astroid.collides_with(player):
                log_event("player_hit")
                print('game over')
                sys.exit()
            for bullet in bullets:
                if astroid.collides_with(bullet):
                    bullet.kill()
                    astroid_field.split(astroid)
        
            
        



        pygame.display.flip()
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
