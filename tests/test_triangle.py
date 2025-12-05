import itertools

from tests._testing import TestCase
from geometric import triangle


def AtleastOneInvalidComb(invalid, valid=None):
    if valid is None:
        valid = []

    yield from itertools.product(invalid, repeat=3)
    yield from itertools.product(valid, itertools.product(invalid, repeat=2))
    yield from itertools.product(invalid, itertools.product(valid, repeat=2))


class TestTriangleArea(TestCase):
    def test_triangle_area_int(self):
        for a, h in itertools.product([
            0, 1, 2, 35812, 10 ** 9 + 7, 10 ** 6 - 1,
        ], repeat=2):
            self.assertIsClose(triangle.area(a, h), a * h / 2)

    def test_triangle_area_float(self):
        for a, h in itertools.product([
            0, 0.1, 1.0, 1.2312, 123123.23, 10e10, 1.23e-8, 1 / 3,
        ], repeat=2):
            self.assertIsClose(triangle.area(a, h), a * h / 2)

    def test_triangle_area_corner_cases(self):
        for a, h in itertools.product([
            0, 0.0, 10 ** 18, 1e18, 1e-6, 1e-9, 1e-18,
        ], repeat=2):
            self.assertIsClose(triangle.area(a, h), a * h / 2)
    
    def test_triangle_area_valid_arguments(self):
        class A: pass

        for a, h in itertools.product(
            ['asd', [], '', A, A(), 123 - 3j],
            [1, 1.0]
        ):
            with self.assertRaises(TypeError):
                triangle.area(a, h)

        for a, h in itertools.product(
            [-1, -2, -10 ** 9, -1.0, -2.0, -1e9, -1e-6],
            [1, 1.0],
        ):
            with self.assertRaises(ValueError):
                triangle.area(a, h)


class TestTrianglePerimeter(TestCase):
    def test_triangle_area_int(self):
        for a, b, c in itertools.product([
            0, 1, 2, 35812, 10 ** 9 + 7, 10 ** 6 - 1,
        ], repeat=3):
            self.assertIsClose(triangle.perimeter(a, b, c), a + b + c)

    def test_triangle_area_float(self):
        for a, b, c in itertools.product([
            0, 0.1, 1.0, 1.2312, 123123.23, 10e10, 1.23e-8, 1 / 3,
        ], repeat=3):
            self.assertIsClose(triangle.perimeter(a, b, c), a + b + c)

    def test_triangle_perimeter_corner_cases(self):
        for a, b, c in itertools.product([
            0, 0.0, 10 ** 18, 1e18, 1e-6, 1e-9, 1e-18,
        ], repeat=3):
            self.assertIsClose(triangle.perimeter(a, b, c), a + b + c)
    
    def test_triangle_perimeter_valid_arguments(self):
        class A: pass

        for a, b, c in AtleastOneInvalidComb(
            ['asd', [], '', A, A(), 123 - 3j],
            [1, 1.0]
        ):
            with self.assertRaises(TypeError):
                triangle.perimeter(a, b, c)

        for a, b, c in AtleastOneInvalidComb(
            [-1, -2, -10 ** 9, -1.0, -2.0, -1e9, -1e-6],
            [1, 1.0],
        ):
            with self.assertRaises(ValueError):
                triangle.perimeter(a, b, c)

