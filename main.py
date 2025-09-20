from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot
import pygame



def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)    

    Asteroid.containers = (updatable, drawable, asteroids)
    
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (updatable, drawable, shots)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for item in updatable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)
        
        for item in asteroids:
            for shot in shots:
                if item.collision(shot):
                    item.split()
                    shot.kill()
            
            if item.collision(player):
                print("Game over!")
                exit()
            

        
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
        

        

if __name__ == "__main__":
    main()
