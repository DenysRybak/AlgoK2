import unittest
def maximumConsecutiveNumbers(arr, N):

    v = []
    count = 0

    for i in range(N):
        if (arr[i] == 0):
            count += 1
        else:
            v.append(arr[i])

    v.sort()

    v = set(v)
    v = list(v)

    MAXN = 110000


    pref = [0 for i in range(MAXN + 1)]

    for i in range(len(v)):
        pref[v[i]] += 1

    for i in range(1, MAXN + 1, 1):
        pref[i] += pref[i - 1]

    mx = 0

    for i in range(1, MAXN + 1, 1):
        l = i
        r = MAXN
        local_max = 0
        while (l <= r):
            mid = (l + r) // 2

            if (pref[mid] - pref[i - 1] + count >= (mid - i + 1)):
                l = mid + 1
                local_max = max(local_max, mid - i + 1)

            else:
                r = mid - 1
        mx = max(mx, local_max)
    return mx


if __name__ == '__main__':
    N = 13
    arr = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 0, 0]
    print(maximumConsecutiveNumbers(arr, N))



class TestMaximumConsecutiveNumbers(unittest.TestCase):

    def test_example_case(self):
        N = 9
        arr = [0, 10, 15, 50, 0, 14, 9, 12, 40]
        self.assertEqual(maximumConsecutiveNumbers(arr, N), 7)

    def test_zero_count(self):
        N = 7
        arr = [1, 1, 1, 2, 1, 1, 3]
        self.assertEqual(maximumConsecutiveNumbers(arr, N), 3)

    def test_all_zeros(self):
        N = 5
        arr = [0, 0, 0, 0, 0]
        self.assertEqual(maximumConsecutiveNumbers(arr, N), 5)

if __name__ == '__main__':
    unittest.main()
