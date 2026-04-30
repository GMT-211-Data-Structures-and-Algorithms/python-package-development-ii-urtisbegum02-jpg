import unittest
from geometry import Point, Line

class TestGeometry(unittest.TestCase):

    def test_point_creation(self):
        """Nokta doğru koordinatlarla oluşturuluyor mu?"""
        p = Point(10, 20, "TestNoktası")
        self.assertEqual(p.x, 10.0)
        self.assertEqual(p.y, 20.0)
        self.assertEqual(p.label, "TestNoktası")

    def test_point_from_file_line(self):
        """Dosya formatından nokta başarıyla okunuyor mu?"""
        line_data = "15,30, Merkez Kütüphane"
        p = Point.from_file_line(line_data)
        self.assertIsNotNone(p)
        self.assertEqual(p.x, 15.0)
        self.assertEqual(p.label, "Merkez Kütüphane")

    def test_line_length(self):
        """Çizgi uzunluğu (0,0) - (3,4) için 5.0 çıkmalı (3-4-5 üçgeni)"""
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        yol = Line("Test Yolu")
        yol.add_point(p1)
        yol.add_point(p2)
        
        self.assertAlmostEqual(yol.calculate_length(), 5.0)

if __name__ == '__main__':
    unittest.main()