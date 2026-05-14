import unittest
import math
from work1_bru import Point, Line

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(0, 0, "Origin")
        self.p2 = Point(3, 4, "Point A")
        self.p3 = Point(-2, 5, "Point B")

    def test_creation(self):
        p = Point(1, 2, "Test")
        self.assertEqual(p.x, 1.0)
        self.assertEqual(p.y, 2.0)
        self.assertEqual(p.name, "Test")
        # String koordinat dönüşümü
        p_str = Point("5", "10", "StrPoint")
        self.assertEqual(p_str.x, 5.0)
        self.assertEqual(p_str.y, 10.0)

    def test_equality(self):
        p_a = Point(1, 2)
        p_b = Point(1, 2)
        p_c = Point(1, 3)
        self.assertEqual(p_a, p_b)
        self.assertNotEqual(p_a, p_c)
        self.assertNotEqual(p_a, "not a point")

    def test_distance_to(self):
        # (0,0) -> (3,4) = 5
        self.assertAlmostEqual(self.p1.distance_to(self.p2), 5.0)
        self.assertAlmostEqual(self.p1.distance_to(self.p1), 0.0)
        with self.assertRaises(TypeError):
            self.p1.distance_to((1, 2))

    def test_midpoint(self):
        mid = self.p1.midpoint(self.p2)
        self.assertAlmostEqual(mid.x, 1.5)
        self.assertAlmostEqual(mid.y, 2.0)
        
        p_neg1 = Point(-2, -2)
        p_neg2 = Point(2, 2)
        mid_neg = p_neg1.midpoint(p_neg2)
        self.assertAlmostEqual(mid_neg.x, 0.0)
        self.assertAlmostEqual(mid_neg.y, 0.0)
        
        with self.assertRaises(TypeError):
            self.p1.midpoint([1, 2])

    def test_distance_to_line(self):
        line = Line(Point(0, 0), Point(10, 0), "X-axis")
        p_above = Point(5, 3)
        self.assertAlmostEqual(p_above.distance_to_line(line), 3.0)
        with self.assertRaises(TypeError):
            p_above.distance_to_line("not a line")

    def test_string_representation(self):
        p = Point(1, 2, "Test")
        s = str(p)
        self.assertIn("1", s)
        self.assertIn("2", s)
        self.assertIn("Test", s)

class TestLine(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(0, 0, "Start")
        self.p2 = Point(3, 4, "End")
        self.p3 = Point(0, 0)
        self.p4 = Point(0, 5)
        self.line1 = Line(self.p1, self.p2, "TestLine")
        self.line_vertical = Line(self.p3, self.p4, "Vertical")

    def test_creation(self):
        self.assertEqual(self.line1.start, self.p1)
        self.assertEqual(self.line1.end, self.p2)
        self.assertEqual(self.line1.name, "TestLine")
        with self.assertRaises(TypeError):
            Line((0, 0), self.p2)
        with self.assertRaises(TypeError):
            Line(self.p1, (3, 4))

    def test_length(self):
        self.assertAlmostEqual(self.line1.length(), 5.0)
        zero_line = Line(self.p1, self.p1, "Zero")
        self.assertAlmostEqual(zero_line.length(), 0.0)

    def test_midpoint(self):
        mid = self.line1.midpoint()
        self.assertAlmostEqual(mid.x, 1.5)
        self.assertAlmostEqual(mid.y, 2.0)

    def test_slope(self):
        self.assertAlmostEqual(self.line1.slope(), 4/3)
        self.assertIsNone(self.line_vertical.slope())
        horiz = Line(Point(0, 5), Point(5, 5), "Horiz")
        self.assertAlmostEqual(horiz.slope(), 0.0)

    def test_equation(self):
        m, b = self.line1.equation()
        self.assertAlmostEqual(m, 4/3)
        self.assertAlmostEqual(b, 0.0)
        self.assertIsNone(self.line_vertical.equation())
        
        p1 = Point(0, 2)
        p2 = Point(1, 4)
        line = Line(p1, p2)
        m, b = line.equation()
        self.assertAlmostEqual(m, 2.0)
        self.assertAlmostEqual(b, 2.0)

    def test_perpendicular_point(self):
        line = Line(Point(0, 0), Point(10, 0))
        p = Point(5, 5)
        proj = line.perpendicular_point(p)
        self.assertAlmostEqual(proj.x, 5.0)
        self.assertAlmostEqual(proj.y, 0.0)
        
        # Segment dışına taşan projeksiyon (clamping testi)
        p_out = Point(15, 5)
        proj_out = line.perpendicular_point(p_out)
        self.assertAlmostEqual(proj_out.x, 10.0)  # end noktasına kilitlenmeli
        
        with self.assertRaises(TypeError):
            line.perpendicular_point("not a point")

    def test_distance_to_point(self):
        line = Line(Point(0, 0), Point(10, 0))
        p = Point(5, 3)
        self.assertAlmostEqual(line.distance_to_point(p), 3.0)
        with self.assertRaises(TypeError):
            line.distance_to_point("not a point")

    def test_string_representation(self):
        s = str(self.line1)
        self.assertIn("TestLine", s)
        self.assertIn("Start", s)
        self.assertIn("End", s)

class TestIntegration(unittest.TestCase):
    def test_geometry_consistency(self):
        p1 = Point(0, 0)
        p2 = Point(4, 0)
        p3 = Point(4, 3)
        self.assertAlmostEqual(Line(p1, p2).length(), 4.0)
        self.assertAlmostEqual(Line(p2, p3).length(), 3.0)
        self.assertAlmostEqual(Line(p3, p1).length(), 5.0)

    def test_midpoint_distance_relation(self):
        p1 = Point(1, 1)
        p2 = Point(5, 7)
        line = Line(p1, p2)
        mid = line.midpoint()
        self.assertAlmostEqual(mid.distance_to(p1), mid.distance_to(p2))
        self.assertAlmostEqual(line.length(), 2 * mid.distance_to(p1))

if __name__ == '__main__':
    unittest.main()