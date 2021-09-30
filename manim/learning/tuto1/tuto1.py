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
        mathtext.add_updater(lambda x: x.move_to(rectangle))
        # animations
        self.play(FadeIn(rectangle))
        self.play(Write(mathtext))
        self.play(rectangle.animate.shift(4*DOWN+2*RIGHT))
        self.wait()
        # remove updater
        mathtext.clear_updaters()
        self.play(rectangle.animate.shift(4*UP + 2*LEFT))


class Circumference(Scene):
    def construct(self):
        # def a variable
        r = ValueTracker(2)
        # always_redraw act like an updater
        circle = always_redraw(
            lambda: Circle(color=BLUE, radius=r.get_value())
        )
        line = always_redraw(
            lambda: Line(color=BLUE).set_length(
                2*PI*r.get_value()).next_to(circle, DOWN)
        )
        # animations
        self.play(FadeIn(circle))
        self.wait()
        self.play(ReplacementTransform(circle.copy(), line))
        self.wait()
        self.play(r.animate.set_value(1))
