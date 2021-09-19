from manim import *
from numpy import sin, cos, deg2rad

class PointWithTrace(Scene):
    def construct(self):
        RADIUS = 2
        self.ALPHA = deg2rad(30)
        circ = Circle(radius=RADIUS)
        dot = Dot()
        dot.move_to([RADIUS*cos(self.ALPHA),RADIUS*sin(self.ALPHA),0])
        
        def go_around_circle(mob,dt):
            self.ALPHA += 5
            dot.move_to([RADIUS*cos(self.ALPHA),RADIUS*sin(self.ALPHA),0])
        
        dot.add_updater(go_around_circle)
        self.add(circ)
        self.add(dot)
        self.wait(10)