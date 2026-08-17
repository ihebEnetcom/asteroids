from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,(255, 255, 255, 255),self.position,self.radius,LINE_WIDTH)
    def update(self, dt):
        self.position+=self.velocity *dt
    def getKind(self)-> int:
        return int (self.radius / ASTEROID_MIN_RADIUS)
    
    