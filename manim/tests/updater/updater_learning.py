from manim import *

class AddUpdater1(Scene):
    def construct(self):
        dot = Dot()
        text = Text("Label")
        text.next_to(dot, RIGHT)
        self.add(dot, text)

        def update_text(obj):
            """"""
            obj.next_to(dot, RIGHT)

        text.add_updater(update_text)

        self.add(text)
        self.play(dot.animate.shift(2*UP))
        self.wait()

class AddUpdater2(Scene):
    def construct(self):
        dot1 = Dot()
        dot2 = Dot(RIGHT)
        line = Line(dot1.get_center(), dot2.get_center())
        self.add(dot1, dot2, line)
        def update_line(obj):
            obj.become(Line(dot1.get_center(), dot2.get_center()))
        line.add_updater(update_line)
        self.add(line)
        self.play(dot1.animate.shift(2*UP))
        self.wait()

class AddUpdater3(Scene):
    def construct(self):
        pt1 = Point()
        pt2 = Point()
        arrow = Arrow(pt1, pt2, buff=0)
        self.add(arrow)
        # lambda sert à définir une fonction courte
        # on peut faire aussi 
        # def update_arrow(obj):
        #   obj.become(Arrow(pt1, pt2, buff=0))
        arrow.add_updater(lambda obj : obj.become(Arrow(pt1, pt2, buff=0)))
        self.add(arrow)
        self.play(pt2.animate.shift(2*RIGHT))