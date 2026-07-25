import random

def generate(size):

    values = list(

        range(

            10,

            size * 10,

            10

        )

    )

    random.shuffle(values)

    return values
