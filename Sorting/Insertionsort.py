# Insertion Sort
#
# Insertion sort builds the sorted list one element at a time. On each pass,
# it takes the current element and inserts it into the correct position in the
# already-sorted portion on its left.
#
# The values must be comparable with > and <. This means insertion sort can
# sort integers, floats, strings, booleans, and lists or tuples containing
# comparable values.
#
# Dictionaries and sets are not normally sorted directly. A dictionary can be
# sorted by its keys, values, or items, and a set can be converted to a list
# before sorting.
#
# Time complexity:
# - Best case: O(n), when the data is already sorted
# - Average case: O(n^2)
# - Worst case: O(n^2), when the data is in reverse order
#
# Space complexity:
# - O(1) auxiliary space for the insertion sort operations
# - This implementation copies the input first, so the copied list uses O(n)
#   additional space and the original data remains unchanged.

class InsertionSort:

    def __init__(self):
        pass

    def SortAscending(self,data):
        # Work on a copy so the original list stays unchanged.
        data = data.copy()
        n = len(data)

        # The first item is already sorted by itself.
        for i in range(1, n):
            # Store the value that must be inserted into the sorted portion.
            current = data[i]
            j = i - 1

            # Shift larger values one position to the right to make room.
            while j >= 0 and data[j] > current:
                data[j + 1] = data[j]
                j -= 1

            # Insert the current value in its correct ascending position.
            data[j + 1] = current
        return data

    def SortDescending(self, data):
        # Work on a copy so the original list stays unchanged.
        data = data.copy()
        n = len(data)

        # The first item is already sorted by itself.
        for i in range(1, n):
            # Store the value that must be inserted into the sorted portion.
            current = data[i]
            j = i - 1

            # Shift smaller values one position to the right to make room.
            while j >= 0 and data[j] < current:
                data[j + 1] = data[j]
                j -= 1

            # Insert the current value in its correct descending position.
            data[j + 1] = current
        return data


X = [5, 6, 2, 1, 3, 6, 9]

sorter = InsertionSort()

AscSorted = sorter.SortAscending(X)
DescSorted = sorter.SortDescending(X)

print("Ascending:", AscSorted)     # [1, 2, 3, 5, 6, 6, 9]
print("Descending:", DescSorted)    # [9, 6, 6, 5, 3, 2, 1]