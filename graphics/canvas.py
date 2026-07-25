from tkinter import Canvas

from settings import WIDTH, HEIGHT

from graphics.palette import *

class GraphCanvas:

    def __init__(

        self,

        root

    ):

        self.canvas = Canvas(

            root,

            width=WIDTH,

            height=HEIGHT,

            bg=BACKGROUND

        )

        self.canvas.pack()

    def draw(

        self,

        values,

        active

    ):

        self.canvas.delete("all")

        width = WIDTH / len(values)

        maximum = max(values)

        for i, value in enumerate(values):

            x = i * width

            y = HEIGHT - (

                value / maximum

            ) * HEIGHT

            color = (

                ACTIVE

                if i in active

                else BAR

            )

            self.canvas.create_rectangle(

                x,

                y,

                x + width - 2,

                HEIGHT,

                fill=color,

                outline=""

            )
