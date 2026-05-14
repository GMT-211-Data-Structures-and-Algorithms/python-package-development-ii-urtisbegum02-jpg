"""
Unit tests for Point and Line classes.

This module contains comprehensive unit tests for the Point and Line classes
to ensure they work correctly.
"""

import unittest
import math
from work1_bru import Point, Line


class TestPoint(unittest.TestCase):
    """Test cases for the Point class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.p1 = Point(0, 0, "Origin")
        self.p2 = Point(3, 4, "Point A")
        self.p3 = Point(-2, 5, "Point B")
    
    def test_point_creation(self):
        """Test Point object creation."""
        p = Point(1, 2, "Test")
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)
        self.assertEqual(p.name, "Test")
    
    def test_point_creation_with_strings(self):
        """Test Point creation with string coordinates."""
        p = Point("3.5", "4.5", "Test")
        self.assertEqual(p.x, 3.5)
        self.assertEqual(p.y, 4.5)
    
    def test_point_equality(self):
        """Test Point equality."""
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        p3 = Point(1, 3)
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)
    
    def test_distance_to(self):
        """Test distance calculation between points."""
        # Distance from (0,0) to (3,4) should be 5
        distance = self.p1.distance_to(self.p2)
        self.assertAlmostEqual(distance, 5.0)
    
    def test_distance_same_point(self):
        """Test distance between same point is zero."""
        distance = self.p1.distance_to(self.p1)
        self.assertAlmostEqual(distance, 0.0)
    
    def test_distance_to_invalid_type(self):
        """Test distance_to raises error for non-Point objects."""
        with self.assertRaises(TypeError):
            self.p1.distance_to((3, 4))
    
    def test_midpoint(self):
        """Test midpoint calculation."""
        mid = self.p1.midpoint(self.p2)
        self.assertEqual(mid.x, 1.5)
        self.assertEqual(mid.y, 2.0)
    
    def test_midpoint_negative_coordinates(self):
        """Test midpoint with negative coordinates."""
        p1 = Point(-2, -2)
        p2 = Point(2, 2)
        mid = p1.midpoint(p2)
        self.assertEqual(mid.x, 0.0)
        self.assertEqual(mid.y, 0.0)
    
    def test_point_str(self):
        """Test Point string representation."""
        p = Point(1, 2, "Test")
        self.assertIn("1", str(p))
        self.assertIn("2", str(p))
        self.assertIn("Test", str(p))


class TestLine(unittest.TestCase):
    """Test cases for the Line class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.p1 = Point(0, 0, "Start")
        self.p2 = Point(3, 4, "End")
        self.p3 = Point(0, 0)
        self.p4 = Point(0, 5)
        self.line1 = Line(self.p1, self.p2, "TestLine")
        self.line_vertical = Line(self.p3, self.p4, "Vertical")
    
    def test_line_creation(self):
        """Test Line object creation."""
        line = Line(self.p1, self.p2, "TestLine")
        self.assertEqual(line.start, self.p1)
        self.assertEqual(line.end, self.p2)
        self.assertEqual(line.name, "TestLine")
    
    def test_line_creation_invalid_start(self):
        """Test Line creation with invalid start point."""
        with self.assertRaises(TypeError):
            Line((0, 0), self.p2)
    
    def test_line_creation_invalid_end(self):
        """Test Line creation with invalid end point."""
        with self.assertRaises(TypeError):
            Line(self.p1, (3, 4))
    
    def test_line_length(self):
        """Test line length calculation."""
        # Line from (0,0) to (3,4) has length 5
        length = self.line1.length()
        self.assertAlmostEqual(length, 5.0)
    
    def test_line_length_zero(self):
        """Test line with zero length."""
        line = Line(self.p1, self.p1, "Zero")
        self.assertAlmostEqual(line.length(), 0.0)
    
    def test_line_midpoint(self):
        """Test line midpoint calculation."""
        mid = self.line1.midpoint()
        self.assertEqual(mid.x, 1.5)
        self.assertEqual(mid.y, 2.0)
    
    def test_line_slope(self):
        """Test line slope calculation."""
        slope = self.line1.slope()
        # Slope should be 4/3
        self.assertAlmostEqual(slope, 4/3)
    
    def test_line_slope_vertical(self):
        """Test slope of vertical line is None."""
        slope = self.line_vertical.slope()
        self.assertIsNone(slope)
    
    def test_line_slope_horizontal(self):
        """Test slope of horizontal line."""
        p1 = Point(0, 5)
        p2 = Point(5, 5)
        line = Line(p1, p2)
        self.assertAlmostEqual(line.slope(), 0.0)
    
    def test_line_equation(self):
        """Test line equation calculation."""
        m, b = self.line1.equation()
        # y = (4/3)x + 0
        self.assertAlmostEqual(m, 4/3)
        self.assertAlmostEqual(b, 0)
    
    def test_line_equation_vertical(self):
        """Test equation of vertical line is None."""
        eq = self.line_vertical.equation()
        self.assertIsNone(eq)
    
    def test_line_equation_with_offset(self):
        """Test line equation with y-intercept offset."""
        p1 = Point(0, 2)
        p2 = Point(1, 4)
        line = Line(p1, p2)
        m, b = line.equation()
        self.assertAlmostEqual(m, 2)
        self.assertAlmostEqual(b, 2)
    
    def test_line_str(self):
        """Test Line string representation."""
        line_str = str(self.line1)
        self.assertIn("TestLine", line_str)


class TestIntegration(unittest.TestCase):
    """Integration tests for Point and Line classes."""
    
    def test_create_complex_geometry(self):
        """Test creating multiple points and lines."""
        points = [
            Point(0, 0, "A"),
            Point(10, 2, "Bölüm Binası"),
            Point(15, 30, "Merkez Kütüphane"),
            Point(5, 27, "Spor Salonu"),
            Point(-4, 17, "Yemekhane"),
            Point(-15, 25, "BAM")
        ]
        
        self.assertEqual(len(points), 6)
        
        # Create lines between points
        line1 = Line(points[0], points[1], "Ana yol")
        line2 = Line(points[1], points[2], "Merkez yolu")
        
        self.assertAlmostEqual(line1.length(), math.sqrt(104))
        self.assertGreater(line2.length(), 0)
    
    def test_geometry_transformations(self):
        """Test various geometric transformations."""
        p1 = Point(0, 0)
        p2 = Point(4, 0)
        p3 = Point(4, 3)
        
        # Create triangle
        lines = [
            Line(p1, p2, "Base"),
            Line(p2, p3, "Height"),
            Line(p3, p1, "Hypotenuse")
        ]
        
        # Check triangle sides
        self.assertAlmostEqual(lines[0].length(), 4)
        self.assertAlmostEqual(lines[1].length(), 3)
        self.assertAlmostEqual(lines[2].length(), 5)


if __name__ == '__main__':
    unittest.main()
