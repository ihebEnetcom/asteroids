import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS,SHOT_SPEED,LINE_WIDTH
class Shot (CircleShape):
    
    def __init__(self, x, y,direction:pygame.Vector2):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity =direction
        
    def draw(self, screen: pygame.Surface) -> None:
           pygame.draw.circle(screen,(255, 255, 255, 255),self.position,self.radius,LINE_WIDTH)
    def update(self, dt):
           self.position+=self.velocity *dt *SHOT_SPEED