class SelectionSort:
    """
    Selection Sort:
    In each round, find the SMALLEST (or LARGEST) remaining item
    and swap it into its correct position.

    Unlike Bubble Sort (which swaps neighbors many times),
    Selection Sort finds the best candidate first, then swaps ONCE per round.

    Time Complexity:
        Best case   : O(n^2)   -- no early exit, always scans fully
        Average case: O(n^2)
        Worst case  : O(n^2)
    (Selection Sort has NO best-case improvement, unlike Bubble Sort's early-stop version.
     It always does the same number of comparisons, no matter the input.)

    Space Complexity: O(1)
        -- sorts using swaps only, no extra list needed (data.copy() is just
           to protect the original list, not part of the algorithm's own space use)

    Can sort:
        - Integers        : [5, 3, 8, 1]
        - Floats          : [5.5, 3.2, 8.1]
        - Strings         : ["mango", "apple"]
        - Booleans        : [True, False, True]
        - Lists/Tuples    : [[3,"c"], [1,"a"]]  (compares element by element)
        - Dictionaries    : only by picking a key, e.g. data[j]["age"]
        - Custom objects  : only if __lt__ / __gt__ is defined in that class

    Cannot sort directly:
        - Sets            : no order, convert to list first
        - Mixed types     : e.g. [5, "apple"] -> TypeError
    """

    def __init__(self):
        pass

    def SortAscending(self, data):
        data = data.copy()          # work on a copy, so the original list stays unchanged
        n = len(data)

        for i in range(n-1):
            # Assume the current position i holds the smallest value for now
            minimum_index = i

            # Look through the REST of the list (i+1 to end) for anything smaller
            for j in range(i+1, n):
                if data[j] < data[minimum_index]:
                    minimum_index = j        # found a new smallest, remember its position

            # After checking all remaining items, swap the smallest found into position i
            data[i], data[minimum_index] = data[minimum_index], data[i]

        return data

    def SortDescending(self, data):
        data = data.copy()          # work on a copy, so the original list stays unchanged
        n = len(data)

        for i in range(n-1):
            # Assume the current position i holds the largest value for now
            maximum_index = i

            # Look through the REST of the list (i+1 to end) for anything larger
            for j in range(i+1, n):
                if data[j] > data[maximum_index]:
                    maximum_index = j        # found a new largest, remember its position

            # After checking all remaining items, swap the largest found into position i
            data[i], data[maximum_index] = data[maximum_index], data[i]

        return data


X = SelectionSort()
Y = SelectionSort()
L = [5, 6, 2, 1, 3, 6, 9]

AscSorted = X.SortAscending(L)
DescSorted = Y.SortDescending(L)
print(AscSorted)     # [1, 2, 3, 5, 6, 6, 9]
print(DescSorted)    # [9, 6, 6, 5, 3, 2, 1]