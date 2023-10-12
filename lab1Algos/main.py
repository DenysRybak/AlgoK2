import unittest


def isSubArray(num1, num2):
    if not num1:
        return True

    i = 0
    j = 0

    while i <len(num1) and j < len(num2):
        if num1[i] == num2[j]:
            i += 1;
        j += 1;

    return i == len(num1)


num1 = [5, 11, 2]
num2 = [5, 4, 11, 15, 7, 2]
print(isSubArray(num1, num2))




# class TestIsSubarray(unittest.TestCase):
#     def test_subarray_exists(self):
#         A = [1, 2, 3, 4, 5]
#         B = [3, 4, 5]
#         self.assertTrue(issubarray(A, B))
#
#     def test_subarray_not_exists(self):
#         A = [1, 2, 3, 4, 5]
#         B = [6, 7]
#         self.assertFalse(issubarray(A, B))
#
#     def test_subarray_empty_B(self):
#         A = [1, 2, 3, 4, 5]
#         B = []
#         self.assertTrue(issubarray(A, B))
