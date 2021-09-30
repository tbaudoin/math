from manim import *


class WorkWithGraph(Scene):
    def construct(self):
        f = [
            (lambda x: 0.5*x, DR),
            (lambda x: -0.5*x + 3, UP),
        ]
        for func, pos in f:
            graphing_stuff = self.create_graph(func)
            graphing_stuff.to_edge(UL)
            self.play_graph(graphing_stuff, final_pos=pos)

    def play_graph(self, graphing_stuff, final_pos=DR):
        self.play(
            DrawBorderThenFill(graphing_stuff["axes"]),
            Write(graphing_stuff["axis_label"])
        )
        self.play(Create(graphing_stuff["graph"]))
        self.play(graphing_stuff.animate.to_edge(final_pos))

    def create_graph(self, func):
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=5,
            y_length=3,
        )
        # show the thicks labels
        axes.add_coordinates()
        # set the axis labels
        axis_label = axes.get_axis_labels(x_label="x", y_label="f(x)")
        # graph
        graph = axes.get_graph(func, x_range=[0, 5], color=RED)
        return VDict(
            {
                "axes": axes,
                "axis_label": axis_label,
                "graph": graph
            }
        )
