import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class MutationAdequateTest(unittest.TestCase):
    
    def test1(self):
        # Test case 1: Scalene triangle
        triangle_result1 = Triangle.classify(20, 21, 23)
        self.assertEqual(triangle_result1, Triangle.Type.SCALENE)

    def test2(self):
        # Test case 2: Isosceles triangle - normative cases a=b
        triangle_result2 = Triangle.classify(7, 7, 5)
        self.assertEqual(triangle_result2, Triangle.Type.ISOSCELES)
    
    def test3(self):
        # Test case 3: Isosceles triangle b=c
        triangle_result3 = Triangle.classify(8, 10, 10)
        self.assertEqual(triangle_result3, Triangle.Type.ISOSCELES)
        
    def test4(self):
        # Test case 4: Isosceles triangle a=c
        triangle_result4 = Triangle.classify(15, 12, 15)
        self.assertEqual(triangle_result4, Triangle.Type.ISOSCELES)

    def test5(self):
        # Test case 5: Equilateral triangle - normative cases a=b=c
        triangle_result5 = Triangle.classify(6, 6, 6)
        self.assertEqual(triangle_result5, Triangle.Type.EQUILATERAL)

    def test6(self):
        # Test case 6: Invalid triangle - exceptional cases (all sides 0)
        triangle_result6 = Triangle.classify(0, 0, 0)
        self.assertEqual(triangle_result6, Triangle.Type.INVALID)

    def test7(self):
        # Test case 7: Invalid triangle (2 sides zero)
        triangle_result7 = Triangle.classify(0, 0, 6)
        self.assertEqual(triangle_result7, Triangle.Type.INVALID)

    def test8(self):
        # Test case 8: Invalid triangle (one side is zero)
        triangle_result8 = Triangle.classify(6, 6, 0)
        self.assertEqual(triangle_result8, Triangle.Type.INVALID)

    def test9(self):
        # Test case 9: Invalid triangle - exceptional cases (a + b <= c)
        triangle_result9 = Triangle.classify(5, 5, 10)
        self.assertEqual(triangle_result9, Triangle.Type.INVALID)

    def test10(self):       
        # Test case 10: Invalid triangle (a + c <= b)
        triangle_result10 = Triangle.classify(3, 10, 2)
        self.assertEqual(triangle_result10, Triangle.Type.INVALID)

    def test11(self):
        # Test case 11: Invalid triangle (b + c <= a)
        triangle_result11 = Triangle.classify(6, 2, 1)
        self.assertEqual(triangle_result11, Triangle.Type.INVALID)
        
    def test12(self):
        # Test case 12: a=0 shouldn't be accepted - Invalid triangle
        triangle_result11 = Triangle.classify(0, 2, 2)
        self.assertEqual(triangle_result11, Triangle.Type.INVALID)
        
    def test13(self):
        # Test case 13: b=0 shouldn't be accepted - Invalid triangle
        triangle_result11 = Triangle.classify(2, 0, 2)
        self.assertEqual(triangle_result11, Triangle.Type.INVALID)
        
    def test14(self):
        # Test case 14: a + b = c shouldnt be accepted - Invalid triangle
        triangle_result11 = Triangle.classify(5, 4, 9)
        self.assertEqual(triangle_result11, Triangle.Type.INVALID)
        
    def test15(self):
        # Test case 15: b + c = a shouldnt be accepted - Invalid triangle
        triangle_result11 = Triangle.classify(9, 5, 4)
        self.assertEqual(triangle_result11, Triangle.Type.INVALID)
    
    def test16(self):
        # Test case 16: a + c = b shouldnt be accepted - Invalid triangle
        triangle_result11 = Triangle.classify(5, 9, 4)
        self.assertEqual(triangle_result11, Triangle.Type.INVALID)
        

if __name__ == '__main__':
    unittest.main()


