import math

from tests._testing import TestCase
from geometric import circle


class TestCircleArea(TestCase):
    def test_circle_area_int(self):
        for r in [
            0, 1, 2, 35812, 10 ** 9 + 7, 10 ** 6 - 1,
        ]:
            self.assertIsClose(circle.area(r), math.pi * r ** 2)

    def test_circle_area_float(self):
        for r in [
            0, 0.1, 1.0, 1.2312, 123123.23, 10e10, 1.23e-8, 1 / 3,
        ]:
            self.assertIsClose(circle.area(r), math.pi * r ** 2)

    def test_circle_area_corner_cases(self):
        for r in [
            0, 0.0, 10 ** 18, 1e18, 1e-6, 1e-9, 1e-18,
        ]:
            self.assertIsClose(circle.area(r), math.pi * r ** 2)
    
    def test_circle_area_valid_arguments(self):
        class A: pass

        for r in [
            'asd', [], '', A, A(), 123 - 3j,
        ]:
            with self.assertRaises(TypeError):
                circle.area(r)

        for r in [
            -1, -2, -10 ** 9, -1.0, -2.0, -1e9, -1e-6,
        ]:
            with self.assertRaises(ValueError):
                circle.area(r)


class TestCirclePerimeter(TestCase):
    def test_circle_perimeter_int(self):
        for r in [
            0, 1, 2, 35812, 10 ** 9 + 7, 10 ** 6 - 1,
        ]:
            self.assertIsClose(circle.perimeter(r), 2 * math.pi * r)

    def test_circle_perimeter_float(self):
        for r in [
            0, 0.1, 1.0, 1.2312, 123123.23, 10e10, 1.23e-8, 1 / 3,
        ]:
            self.assertIsClose(circle.perimeter(r), 2 * math.pi * r)

    def test_circle_perimeter_corner_cases(self):
        for r in [
            0, 0.0, 10 ** 18, 1e18, 1e-6, 1e-9, 1e-18,
        ]:
            self.assertIsClose(circle.perimeter(r), 2 * math.pi * r)
    
    def test_circle_perimeter_valid_arguments(self):
        class A: pass

        for r in [
            'asd', [], '', A, A(), 123 - 3j,
        ]:
            with self.assertRaises(TypeError):
                circle.perimeter(r)

        for r in [
            -1, -2, -10 ** 9, -1.0, -2.0, -1e9, -1e-6,
        ]:
            with self.assertRaises(ValueError):
                circle.perimeter(r)

