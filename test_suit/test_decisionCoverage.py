from isTriangle import Triangle
import unittest

class TestDecisionCoverage(unittest.TestCase):

    def test_decisionCoverage(self):

        # Test case 1: Scalene triangle
        triangle_result = Triangle.classify(20, 21, 23)
        self.assertEqual(triangle_result, Triangle.Type.SCALENE)

        # Test case 2: Isosceles triangle - normative cases a=b
        triangle_result = Triangle.classify(7, 7, 5)
        self.assertEqual(triangle_result, Triangle.Type.ISOSCELES)
        
        # Test case 3: Isosceles triangle b=c
        triangle_result = Triangle.classify(8, 10, 10)
        self.assertEqual(triangle_result, Triangle.Type.ISOSCELES)
        
        # Test case 4: Isosceles triangle a=c
        triangle_result = Triangle.classify(15, 12, 15)
        self.assertEqual(triangle_result, Triangle.Type.ISOSCELES)

        # Test case 5: Equilateral triangle - normative cases a=b=c
        triangle_result = Triangle.classify(6, 6, 6)
        self.assertEqual(triangle_result, Triangle.Type.EQUILATERAL)

        # Test case 6: Invalid triangle - exceptional cases (all sides 0)
        triangle_result = Triangle.classify(0, 0, 0)
        self.assertEqual(triangle_result, Triangle.Type.INVALID)

        # Test case 7: Invalid triangle (2 sides zero)
        triangle_result = Triangle.classify(0, 0, 6)
        self.assertEqual(triangle_result, Triangle.Type.INVALID)

        # Test case 8: Invalid triangle (one side is zero)
        triangle_result = Triangle.classify(6, 6, 0)
        self.assertEqual(triangle_result, Triangle.Type.INVALID)

        # Test case 9: Invalid triangle - exceptional cases (a + b <= c)
        triangle_result = Triangle.classify(5, 5, 10)
        self.assertEqual(triangle_result, Triangle.Type.INVALID)
        
        # Test case 10: Invalid triangle (a + c <= b)
        triangle_result = Triangle.classify(3, 10, 2)
        self.assertEqual(triangle_result, Triangle.Type.INVALID)

        # Test case 11: Invalid triangle (b + c <= a)
        triangle_result = Triangle.classify(6, 2, 1)
        self.assertEqual(triangle_result, Triangle.Type.INVALID)
        
        
        
if __name__ == '__main__':
    unittest.main()