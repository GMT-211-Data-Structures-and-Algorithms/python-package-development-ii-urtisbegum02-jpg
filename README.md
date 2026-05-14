# Geometry Package

A Python package for geometric operations with points and lines in 2D space.

## Features

- Create and manipulate geometric points
- Create and manipulate line segments
- Calculate distances between points
- Find midpoints
- Calculate line slopes and equations
- Load points and lines from files

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Creating Points

```python
from work1_bru import Point

# Create a point
p1 = Point(0, 0, "Origin")
p2 = Point(3, 4, "Point A")

# Calculate distance
distance = p1.distance_to(p2)
print(f"Distance: {distance}")
```

### Creating Lines

```python
from work1_bru import Line, Point

# Create points
start = Point(0, 0)
end = Point(3, 4)

# Create a line
line = Line(start, end, "My Line")

# Get line properties
print(f"Length: {line.length()}")
print(f"Slope: {line.slope()}")
print(f"Midpoint: {line.midpoint()}")
```

## Testing

Run the unit tests:

```bash
python -m pytest test_work1.py
```

Or using unittest:

```bash
python -m unittest test_work1.py
```

## Documentation

To build the documentation:

```bash
cd docs
make html
```

Then open `docs/_build/html/index.html` in your browser.

## License

This project is part of a data structures course assignment.

## Author

Student
