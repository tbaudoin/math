from manim import *


class RectangleWithFraction(Scene):
    """ Moving rectangle with a fraction in his center."""
    def construct(self):
        # create a rectangle
        rectangle = Rectangle(
            color=WHITE,
            width=4.5,
            height=2,
        )
        # move the rectangle
        rectangle.shift(2*UP + 4*LEFT)
        # create a math text
        mathtext = MathTex(
            '\\frac{3}{2}'
        )
        # move the frac in the center of the rectangle
        mathtext.move_to(rectangle)
        # add an updater, if the rectangle move the fraction get stick in his
        # center
        mathtext.add_updater(lambda x : x.move_to(rectangle))
        # animation
        self.play(FadeIn(rectangle))
        self.play(Write(mathtext))
        self.play(rectangle.animate.shift(4*DOWN+2*RIGHT))
        self.wait()
        # remove updater
        mathtext.clear_updaters()
        self.play(rectangle.animate.shift(4*UP + 2*LEFT))
