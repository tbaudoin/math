from typing_extensions import runtime
from manim import *
import numpy as np


class MyPoint():
    def __init__(self, coordinate=[0, 0, 0], name='A', label_pos=DOWN):
        self.coordinate = np.array(coordinate)
        self.name = name
        self.label_pos = label_pos

    def __repr__(self):
        return f"MyPoint({self.coordinate},{self.name},{self.label_pos})"


class Translation(Scene):
    def construct(self):
        points = [
            MyPoint([0, 0, 0], 'A'),
            MyPoint([2, 3, 0], 'B', UP),
            MyPoint([4, 1.5, 0], 'C'),
            MyPoint([2, 2, 0], 'D'),
        ]
        vector_origin = points[0].coordinate
        vector_extrema = np.array([-5, -3, 0])

        images = [MyPoint(p.coordinate + vector_extrema, p.name + "'")
                  for p in points]

        my_vec = Arrow([2,3,0],points[1].coordinate)
        my_vec.add_updater(lambda x: x.move_to(points[1].coordinate))

        dots = [Dot(
            p.coordinate,
            radius=DEFAULT_SMALL_DOT_RADIUS,
            name=p.name,
            color=BLUE,
        )
            for p in points]
        labels = [Text(p.name, font_size=24).next_to(
            p.coordinate, p.label_pos) for p in points]
        polygon = Polygon(*[p.coordinate for p in points])
        self.play(*[FadeIn(d) for d in dots+labels], FadeIn(polygon))
        self.wait()
        self.play(Create(Arrow(vector_origin, vector_extrema, buff=0)))
        self.wait()
        self.add(polygon.copy())
        self.play(Create(my_vec))
        self.play(polygon.animate.shift(UP))

