import  pygame
from constants import LINE_WIDTH,PLAYER_TURN_SPEED,PLAYER_MOVMENT_SPEED,SHOOT_COLLDOWN
from circleshape import CircleShape

from shot import Shot
class Player (CircleShape):
    def __init__(self,x:float,y:float,radius:float)->None:
        super().__init__(x,y,radius)
        self.rotation=0
        self.last_shot_time =0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen,"white",self.triangle(),LINE_WIDTH)		

    def rotate(self,dt:float):
        self.rotation+=PLAYER_TURN_SPEED * dt
    def move(self,dt:float):
        self.position +=pygame.math.Vector2((0,1)).rotate(self.rotation) *dt * PLAYER_MOVMENT_SPEED

    def shot(self):
        current_time = pygame.time.get_ticks()
        print(current_time  )
        if current_time - self.last_shot_time > SHOOT_COLLDOWN *1000:
            bullet = Shot(self.position.x,self.position.y,pygame.math.Vector2((0,1)).rotate(self.rotation))
            self.last_shot_time= pygame.time.get_ticks()
    
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_z]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shot()
        