from manim import *
from numpy import polymul
import sympy as sp
from sympy.abc import x


class SomeText(Scene):
    def construct(self):
        poly = sp.poly(3*x**3 - 2*x + 4)
        poly_str = MathTex(f"P(x) = {sp.latex(poly.expr)}")
        poly_with_dot = MathTex(
            f"P(x) = {sp.latex(poly.expr, mul_symbol='dot')}", substrings_to_isolate="x"
        )
        self.play(FadeIn(poly_str))
        self.wait()
        self.play(TransformMatchingTex(poly_str, poly_with_dot))
        self.wait()
        self.play(poly_with_dot.animate.set_color_by_tex('x', BLUE))
