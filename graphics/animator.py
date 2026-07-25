from settings import DELAY

class Animator:

    def play(

        self,

        root,

        canvas,

        steps

    ):

        iterator = iter(steps)

        def update():

            try:

                values, a, b = next(iterator)

                canvas.draw(

                    values,

                    (a, b)

                )

                root.after(

                    DELAY,

                    update

                )

            except StopIteration:

                pass

        update()
