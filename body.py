import random
from dataclasses import dataclass
from typing import List
from constants import WINDOW_SIZE
import math

G = 0.001

@dataclass
class StateVector:
    x: float
    y: float
    vx: float
    vy: float

class Body:
    def __init__(self, m, x=None, y=None, rigid=False) -> None:
        self.m = m
        self.rigid = rigid
        vx = (random.random() * 2 - 1) * 0.01
        vy = (random.random() * 2 - 1) * 0.01
        self.state = StateVector(
            x=x or random.randint(0, WINDOW_SIZE[0]), 
            y=y or random.randint(0, WINDOW_SIZE[1]), 
            vx=vx, 
            vy=vy
        )

    def calculate_pull(self, other: 'Body'):
        theta = math.atan2((other.state.y - self.state.y), (other.state.x - self.state.x))
        r = math.sqrt((other.state.x - self.state.x)**2 + (other.state.y - self.state.y)**2)
        g = G*other.m/(r**2)
        return g * math.cos(theta), g * math.sin(theta)

    def update_state(self, dt, others: List['Body']):
        ## calculate pull
        ax = sum([self.calculate_pull(other=body)[0] for body in others])
        ay = sum([self.calculate_pull(other=body)[1] for body in others])
        
        # update velocities
        self.state.vx = self.state.vx + ax * dt
        self.state.vy = self.state.vy + ay * dt

        # update position
        if not self.rigid:
            self.state.x = self.state.x + self.state.vx * dt
            self.state.y = self.state.y + self.state.vy * dt

    def get_position(self):
        return (self.state.x, self.state.y)