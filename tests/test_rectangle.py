import itertools

from tests._testing import TestCase
from geometric import rectangle


def AtleastOneInvalidComb(invalid, valid=None):
    if valid is None:
        valid = []

    yield from itertools.product(invalid, repeat=2)
    yield from itertools.product(valid, invalid)
    yield from itertools.product(invalid, valid)


class TestRectangleArea(TestCase):
    def test_rectangle_area_int(self):
        for a, b in itertools.product([
            0, 1, 2, 35812, 10 ** 9 + 7, 10 ** 6 - 1,
        ], repeat=2):
            self.assertIsClose(rectangle.area(a, b), a * b)

    def test_rectangle_area_float(self):
        for a, b in itertools.product([
            0, 0.1, 1.0, 1.2312, 123123.23, 10e10, 1.23e-8, 1 / 3,
        ], repeat=2):
            self.assertIsClose(rectangle.area(a, b), a * b)

    def test_rectangle_area_corner_cases(self):
        for a, b in itertools.product([
            0, 0.0, 10 ** 18, 1e18, 1e-6, 1e-9, 1e-18,
        ], repeat=2):
            self.assertIsClose(rectangle.area(a, b), a * b)
    
    def test_rectangle_area_valid_arguments(self):
        class A: pass

        for a, b in AtleastOneInvalidComb(
            ['asd', [], '', A, A(), 123 - 3j],
            [1, 1.0]
        ):
            with self.assertRaises(TypeError):
                rectangle.area(a, b)

        for a, b in AtleastOneInvalidComb(
            [-1, -2, -10 ** 9, -1.0, -2.0, -1e9, -1e-6],
            [1, 1.0],
        ):
            with self.assertRaises(ValueError):
                rectangle.area(a, b)


class TestRectanglePerimeter(TestCase):
    def test_rectangle_area_int(self):
        for a, b in itertools.product([
            0, 1, 2, 35812, 10 ** 9 + 7, 10 ** 6 - 1,
        ], repeat=2):
            self.assertIsClose(rectangle.perimeter(a, b), 2 * (a + b))

    def test_rectangle_area_float(self):
        for a, b in itertools.product([
            0, 0.1, 1.0, 1.2312, 123123.23, 10e10, 1.23e-8, 1 / 3,
        ], repeat=2):
            self.assertIsClose(rectangle.perimeter(a, b), 2 * (a + b))

    def test_rectangle_perimeter_corner_cases(self):
        for a, b in itertools.product([
            0, 0.0, 10 ** 18, 1e18, 1e-6, 1e-9, 1e-18,
        ], repeat=2):
            self.assertIsClose(rectangle.perimeter(a, b), 2 * (a + b))
    
    def test_rectangle_perimeter_valid_arguments(self):
        class A: pass

        for a, b in AtleastOneInvalidComb(
            ['asd', [], '', A, A(), 123 - 3j],
            [1, 1.0]
        ):
            with self.assertRaises(TypeError):
                rectangle.perimeter(a, b)

        for a, b in AtleastOneInvalidComb(
            [-1, -2, -10 ** 9, -1.0, -2.0, -1e9, -1e-6],
            [1, 1.0],
        ):
            with self.assertRaises(ValueError):
                rectangle.perimeter(a, b)

