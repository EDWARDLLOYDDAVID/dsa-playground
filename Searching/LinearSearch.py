class LinearSearch:
    """
    Linear Search:
    Check each element ONE BY ONE, from the start of the list,
    until the target is found or the list ends.

    No assumption is needed about the data being sorted.
    This is the simplest possible search method.

    Time Complexity:
        Best case   : O(1)     -- target is the very first element checked
        Average case: O(n)     -- target is somewhere in the middle, roughly n/2 checks
        Worst case  : O(n)     -- target is the last element, or not present at all
                                   (every single element must be checked)

    Space Complexity: O(1)
        -- only uses a loop variable (i) and the target to compare,
           no extra list or data structure is created

    Can search:
        - Integers        : [45, 23, 67, 12, 89]
        - Floats          : [4.5, 2.3, 6.7]
        - Strings         : ["apple", "mango", "banana"]
        - Booleans        : [True, False, True]
        - Lists/Tuples    : compares whole item, e.g. [1,2] == [1,2]
        - Dictionaries    : only by comparing a specific key's value
        - Custom objects  : works only if __eq__ is defined, otherwise
                             compares by memory identity, not by field values

    Cannot search meaningfully:
        - Sets            : no fixed order, but 'in' keyword can still check membership
        - Mixed types where == naturally returns False for every pair
          (e.g. searching for a string target inside a list of ints will just never match)

    Note: Unlike Binary Search, the list does NOT need to be sorted.
          This is Linear Search's main advantage, but it's slower on large,
          already-sorted data compared to Binary Search.
    """

    def __init__(self):
        pass

    def search(self, data, target):
        # Go through each index one at a time, from left to right
        for i in range(len(data)):
            if data[i] == target:      # found a match
                return i                # return the position immediately, stop searching
        return -1                       # loop finished without finding it -> not present


X = [45, 23, 67, 12, 89]
Y = 12

search_instance = LinearSearch()
Result = search_instance.search(X, Y)

# If Result is 0 or more, the target was found at that index.
# If Result is -1, the target does not exist in the list.
print(f"Found at index: {Result}" if Result >= 0 else "Element Not Found")