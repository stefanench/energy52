from tkinter import Tk

from data.generator import generate

from graphics.canvas import GraphCanvas
from graphics.animator import Animator

from algorithms.bubble_sort import sort

from settings import BAR_COUNT

root = Tk()

root.title(

    "Sorting Visualizer"

)

values = generate(

    BAR_COUNT

)

canvas = GraphCanvas(

    root

)

Animator().play(

    root,

    canvas,

    sort(values)

)

root.mainloop()
