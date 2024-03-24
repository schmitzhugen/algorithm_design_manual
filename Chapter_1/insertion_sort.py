import unittest


# Insertion Sort

def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]


def insertion_sort(arr):
    # increment j up by one, and compare arr[j] to arr[j-1]
    # if arr[j] > arr[j-1], then j = j+1 [i.e. move up the array]
    # if arr[j] < arr[j-1], then swap arr[j] and arr[j-1], and j = j-1

    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            swap(arr, j, j - 1),
            j = j - 1
    return arr


# Creating two test cases for my insertion sort algorithm

class SortTest(unittest.TestCase):
    def test_sort_1(self):
        self.assertEqual(insertion_sort([6, 9, 1, 4, 10, 11, 13, 3]), [1, 3, 4, 6, 9, 10, 11, 13])

    def test_sort_2(self):
        self.assertEqual(insertion_sort([33, 2, 19, 4, 2]), [2, 2, 4, 19, 33])


if __name__ == '__main__':
    unittest.main()
