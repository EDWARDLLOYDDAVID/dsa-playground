# Bubble Sort Algorithm
# Bubble Sort is a simple comparison-based sorting technique.
# It repeatedly compares adjacent elements and swaps them if they are in the wrong order.
# Smaller values move toward the front for ascending order,
# and larger values move toward the front for descending order.
#
# Possible data types that can be sorted with Bubble Sort:
# 1. Integer: [5, 2, 9, 1]
# 2. Float: [5.5, 2.1, 9.0]
# 3. String: ["banana", "apple", "mango"]
# 4. Boolean: [True, False, True]  # Python treats False as 0 and True as 1
# 5. List of comparable values: [[2, 1], [1, 3], [0, 2]]
# 6. Tuple of comparable values: [(3, 2), (1, 5), (2, 1)]
# 7. Dictionary: sort by keys, values, or items separately
#    Example: sorted(my_dict.items())
# 8. Set: sort after converting to a list, e.g., sorted(my_set)
#
# Important note:
# - Bubble Sort works on any data that can be compared using >, <, and ==.
# - Dictionary and set are not directly sorted as a sequence in the same way as a list.
#   They are usually converted to a list first.
#
# Time Complexity:
# - Best case: O(n) when the array is already sorted
# - Average case: O(n^2)
# - Worst case: O(n^2)
#
# Space Complexity:
# - O(1) auxiliary space for the sorting logic itself
# - The copy inside each method creates O(n) extra memory for the returned list

class BubbleSort:
    def __init__(self, data):
        # Store the original data
        self.data = data

    def sortAscending(self):
        # Create a copy so the original list is not changed
        data = self.data.copy()
        n = len(data)

        # Outer loop runs n-1 times
        for i in range(n-1):
            isSorted = False

            # Inner loop compares adjacent pairs
            for j in range(n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    isSorted = True

            # If no swap happened, the list is already sorted
            if not isSorted:
                break
        return data

    def sortDescending(self):
        # Create a copy so the original list is not modified
        data = self.data.copy()
        n = len(data)

        # Repeat the sorting pass
        for i in range(n-1):
            isSorted = False

            # Compare adjacent elements for descending order
            for j in range(n-i-1):
                if data[j] < data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    isSorted = True

            # Stop early if the list is already sorted
            if not isSorted:
                break
        return data

# Example data
X = [5.5, 11.3, 2.1, 7.8, 3.6, 9.0]
bubble_sort = BubbleSort(X)
Asc_sorted_data = bubble_sort.sortAscending()
Desc_sorted_data = bubble_sort.sortDescending()

print("Ascending:", Asc_sorted_data)
print("Descending:", Desc_sorted_data)
print("Original:", X)

# Additional examples that can be sorted:
# integers = [9, 4, 7, 2, 1]
# floats = [3.5, 8.1, 2.2, 1.9]
# strings = ["banana", "apple", "cherry"]
# booleans = [True, False, True]
# tuple_data = (9, 4, 2, 1)
# set_data = {5, 2, 9, 1}
# dictionary_data = {"b": 2, "a": 1, "c": 3}
# sorted_dictionary = sorted(dictionary_data.items())
# print(sorted_dictionary)