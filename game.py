import pygame
from body import Body
from constants import WINDOW_SIZE

class Game: # Gravity System
    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.clock = clock
        self.set_up()

    def set_up(self):
        self.bodies = [
            Body(200, x=WINDOW_SIZE[0]/2, y=WINDOW_SIZE[1]/2, rigid=True),
        ]

        self.bodies.extend([Body(50) for i in range(0,10)])

    def render(self):
        for body in self.bodies:
            dt = self.clock.get_time()
            other_bodies = self.bodies.copy()
            other_bodies.remove(body)
            body.update_state(dt=dt, others=other_bodies)
            pygame.draw.circle(
                surface=self.screen, 
                color='black', 
                center=body.get_position(), 
                radius=body.m*0.1, 
            )