"""
Point and Line Classes Module

This module provides classes for representing geometric points and lines in 2D space.
"""

import math


class Point:
    """
    A class to represent a point in 2D space.
    
    A point is defined by its x and y coordinates and an optional name.
    
    Attributes:
        x (float): The x-coordinate of the point
        y (float): The y-coordinate of the point
        name (str): The name or label of the point
    """
    
    def __init__(self, x, y, name=""):
        """
        Initialize a Point object.
        
        Args:
            x (float): The x-coordinate of the point
            y (float): The y-coordinate of the point
            name (str, optional): The name of the point. Defaults to empty string.
        """
        self.x = float(x)
        self.y = float(y)
        self.name = str(name)
    
    def __str__(self):
        """Return string representation of the point."""
        return f"Point({self.x}, {self.y}, '{self.name}')"
    
    def __repr__(self):
        """Return detailed string representation of the point."""
        return f"Point({self.x}, {self.y}, '{self.name}')"
    
    def __eq__(self, other):
        """Check if two points are equal."""
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    
    def distance_to(self, other):
        """
        Calculate Euclidean distance to another point.
        
        Args:
            other (Point): The other point
            
        Returns:
            float: The Euclidean distance between the two points
        """
        if not isinstance(other, Point):
            raise TypeError("other must be a Point object")
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def midpoint(self, other):
        """
        Calculate the midpoint between this point and another point.
        
        Args:
            other (Point): The other point
            
        Returns:
            Point: A new Point representing the midpoint
        """
        if not isinstance(other, Point):
            raise TypeError("other must be a Point object")
        mid_x = (self.x + other.x) / 2
        mid_y = (self.y + other.y) / 2
        return Point(mid_x, mid_y, f"midpoint({self.name},{other.name})")


class Line:
    """
    A class to represent a line segment in 2D space.
    
    A line is defined by two endpoints (points) and an optional name.
    
    Attributes:
        start (Point): The starting point of the line
        end (Point): The ending point of the line
        name (str): The name or label of the line
    """
    
    def __init__(self, start, end, name=""):
        """
        Initialize a Line object.
        
        Args:
            start (Point): The starting point of the line
            end (Point): The ending point of the line
            name (str, optional): The name of the line. Defaults to empty string.
        """
        if not isinstance(start, Point):
            raise TypeError("start must be a Point object")
        if not isinstance(end, Point):
            raise TypeError("end must be a Point object")
        
        self.start = start
        self.end = end
        self.name = str(name)
    
    def __str__(self):
        """Return string representation of the line."""
        return f"Line('{self.name}': {self.start} -> {self.end})"
    
    def __repr__(self):
        """Return detailed string representation of the line."""
        return f"Line('{self.name}': {self.start} -> {self.end})"
    
    def length(self):
        """
        Calculate the length of the line segment.
        
        Returns:
            float: The length of the line segment
        """
        return self.start.distance_to(self.end)
    
    def midpoint(self):
        """
        Calculate the midpoint of the line segment.
        
        Returns:
            Point: A Point representing the midpoint of the line
        """
        return self.start.midpoint(self.end)
    
    def slope(self):
        """
        Calculate the slope of the line.
        
        Returns:
            float: The slope of the line, or None if the line is vertical
        """
        if self.start.x == self.end.x:
            return None  # Vertical line
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)
    
    def equation(self):
        """
        Get the equation of the line in the form y = mx + b.
        
        Returns:
            tuple: A tuple (m, b) where m is slope and b is y-intercept,
                   or None if the line is vertical
        """
        m = self.slope()
        if m is None:
            return None
        b = self.start.y - m * self.start.x
        return (m, b)


def load_points_from_file(filename):
    """
    Load points from a text file.
    
    File format: x,y,name (one per line)
    
    Args:
        filename (str): Path to the file containing points
        
    Returns:
        list: A list of Point objects
    """
    points = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split(',')
                    if len(parts) >= 2:
                        x = float(parts[0])
                        y = float(parts[1])
                        name = parts[2].strip() if len(parts) > 2 else ""
                        points.append(Point(x, y, name))
    except FileNotFoundError:
        print(f"File {filename} not found")
    return points


def load_lines_from_file(filename):
    """
    Load lines from a text file.
    
    File format: name, x1,y1, x2,y2 (one per line)
    
    Args:
        filename (str): Path to the file containing lines
        
    Returns:
        list: A list of Line objects
    """
    lines = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = [p.strip() for p in line.split(',')]
                    if len(parts) >= 5:
                        name = parts[0]
                        x1 = float(parts[1])
                        y1 = float(parts[2])
                        x2 = float(parts[3])
                        y2 = float(parts[4])
                        start = Point(x1, y1)
                        end = Point(x2, y2)
                        lines.append(Line(start, end, name))
    except FileNotFoundError:
        print(f"File {filename} not found")
    return lines


if __name__ == "__main__":
    # Example usage
    p1 = Point(0, 0, "Origin")
    p2 = Point(3, 4, "Point A")
    p3 = Point(10, 2, "Bölüm Binası")
    
    print("Points:")
    print(p1)
    print(p2)
    print(p3)
    
    print("\nDistance between Origin and Point A:", p1.distance_to(p2))
    print("Midpoint between Origin and Point A:", p1.midpoint(p2))
    
    # Create lines
    line1 = Line(p1, p2, "Ana yol")
    line2 = Line(p1, p3, "Test Line")
    
    print("\nLines:")
    print(line1)
    print(line2)
    
    print("\nLine 1 length:", line1.length())
    print("Line 1 slope:", line1.slope())
    print("Line 1 equation (m, b):", line1.equation())
    
