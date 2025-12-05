from tests._testing import TestCase
from geometric import square


class TestSquareArea(TestCase):
    def test_square_area_int(self):
        for a in [
            0, 1, 2, 35812, 10 ** 9 + 7, 10 ** 6 - 1,
        ]:
            self.assertIsClose(square.area(a), a ** 2)

    def test_square_area_float(self):
        for a in [
            0, 0.1, 1.0, 1.2312, 123123.23, 10e10, 1.23e-8, 1 / 3,
        ]:
            self.assertIsClose(square.area(a), a ** 2)

    def test_square_area_corner_cases(self):
        for a in [
            0, 0.0, 10 ** 18, 1e18, 1e-6, 1e-9, 1e-18,
        ]:
            self.assertIsClose(square.area(a), a ** 2)
    
    def test_square_area_valid_arguments(self):
        class A: pass

        for a in [
            'asd', [], '', A, A(), 123 - 3j,
        ]:
            with self.assertRaises(TypeError):
                square.area(a)

        for a in [
            -1, -2, -10 ** 9, -1.0, -2.0, -1e9, -1e-6,
        ]:
            with self.assertRaises(ValueError):
                square.area(a)


class TestSquarePerimeter(TestCase):
    def test_square_perimeter_int(self):
        for a in [
            0, 1, 2, 35812, 10 ** 9 + 7, 10 ** 6 - 1,
        ]:
            self.assertIsClose(square.perimeter(a), 4 * a)

    def test_square_perimeter_float(self):
        for a in [
            0, 0.1, 1.0, 1.2312, 123123.23, 10e10, 1.23e-8, 1 / 3,
        ]:
            self.assertIsClose(square.perimeter(a), 4 * a)

    def test_square_perimeter_corner_cases(self):
        for a in [
            0, 0.0, 10 ** 18, 1e18, 1e-6, 1e-9, 1e-18,
        ]:
            self.assertIsClose(square.perimeter(a), 4 * a)
    
    def test_square_perimeter_valid_arguments(self):
        class A: pass

        for a in [
            'asd', [], '', A, A(), 123 - 3j,
        ]:
            with self.assertRaises(TypeError):
                square.perimeter(a)

        for a in [
            -1, -2, -10 ** 9, -1.0, -2.0, -1e9, -1e-6,
        ]:
            with self.assertRaises(ValueError):
                square.perimeter(a)

