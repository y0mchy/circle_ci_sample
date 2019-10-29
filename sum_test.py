import unittest
from sum import add

class SumTest(unittest.TestCase):

    def test_sum(self):
        v1 = 3
        v2 = 5
        ans = 8
        print("v1,v2,ans = ",v1,v2,ans)
        self.assertEqual(add(v1,v2),ans)

    def test_sum2(self):
        v1 = 23
        v2 = 34
        ans = 57
        print("v1,v2,ans = ",v1,v2,ans)
        self.assertEqual(add(v1,v2),ans)

if __name__ == "__main__":
    unittest.main()

