def sort(values):

    arr = values[:]

    for i in range(len(arr)):

        minimum = i

        for j in range(

            i+1,

            len(arr)

        ):

            yield arr, minimum, j

            if arr[j] < arr[minimum]:

                minimum = j

        arr[i], arr[minimum] = (

            arr[minimum],

            arr[i]

        )

        yield arr, i, minimum
