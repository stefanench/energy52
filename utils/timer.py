import time

class Timer:

    def measure(

        self,

        func,

        *args

    ):

        start = time.perf_counter()

        result = func(*args)

        end = time.perf_counter()

        print(

            f"{end-start:.4f}s"

        )

        return result
