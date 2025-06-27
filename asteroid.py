from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, width=2)
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        spilt_angle =  random.uniform(20, 50)
        small_asteroid_one = pygame.math.Vector2.rotate(self.velocity, spilt_angle)
        small_asteroid_two = pygame.math.Vector2.rotate(self.velocity, -spilt_angle)
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity= small_asteroid_one * 1.2
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = small_asteroid_two * 1.2


    def update(self, dt):
        self.position += self.velocity * dt
        pass
    