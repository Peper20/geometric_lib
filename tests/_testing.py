import math
import unittest


class TestCase(unittest.TestCase):
    def assertIsClose(self, a, b, rel_tol=1e-9, abs_tol=0):
        return self.assertTrue(math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol))
