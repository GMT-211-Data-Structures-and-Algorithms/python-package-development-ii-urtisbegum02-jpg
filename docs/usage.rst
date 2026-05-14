======
Usage
======

This section provides examples of how to use the Geometry Package.

Creating Points
===============

Basic Point Creation
--------------------

Points are created with x and y coordinates and an optional name:

.. code-block:: python

    from work1_bru import Point
    
    # Create a simple point
    origin = Point(0, 0, "Origin")
    
    # Create points with different coordinates
    p1 = Point(10, 2, "Building A")
    p2 = Point(15, 30, "Library")
    p3 = Point(-4, 17, "Cafeteria")

Calculating Distances
---------------------

You can calculate the distance between two points:

.. code-block:: python

    p1 = Point(0, 0)
    p2 = Point(3, 4)
    
    # Calculate Euclidean distance
    distance = p1.distance_to(p2)
    print(f"Distance: {distance}")  # Output: 5.0

Finding Midpoints
-----------------

Find the midpoint between two points:

.. code-block:: python

    p1 = Point(0, 0)
    p2 = Point(4, 4)
    
    midpoint = p1.midpoint(p2)
    print(f"Midpoint: ({midpoint.x}, {midpoint.y})")  # Output: (2.0, 2.0)

Creating Lines
==============

Basic Line Creation
-------------------

Lines are created from two Point objects:

.. code-block:: python

    from work1_bru import Point, Line
    
    start = Point(0, 0, "Start")
    end = Point(3, 4, "End")
    
    line = Line(start, end, "Main Street")

Calculating Line Properties
----------------------------

Lines have several properties you can calculate:

.. code-block:: python

    line = Line(Point(0, 0), Point(3, 4), "TestLine")
    
    # Line length
    length = line.length()
    print(f"Length: {length}")  # Output: 5.0
    
    # Line slope
    slope = line.slope()
    print(f"Slope: {slope}")  # Output: 1.333... (4/3)
    
    # Line equation (y = mx + b)
    m, b = line.equation()
    print(f"Equation: y = {m}x + {b}")

Finding Midpoint of a Line
---------------------------

Get the midpoint of a line segment:

.. code-block:: python

    line = Line(Point(0, 0), Point(4, 4))
    
    midpoint = line.midpoint()
    print(f"Midpoint: ({midpoint.x}, {midpoint.y})")  # (2.0, 2.0)

Loading Data from Files
=======================

Loading Points from File
------------------------

Create a file with points in the format: x,y,name

Example ``points.txt``:

.. code-block:: text

    10,2,Building A
    15,30,Library
    5,27,Sports Center
    -4,17,Cafeteria

Load them:

.. code-block:: python

    from work1_bru import load_points_from_file
    
    points = load_points_from_file('points.txt')
    for point in points:
        print(point)

Loading Lines from File
-----------------------

Create a file with lines in the format: name,x1,y1,x2,y2

Example ``lines.txt``:

.. code-block:: text

    Main Road,0,0,3,4
    Side Street,3,4,7,8
    Plaza,0,0,10,0

Load them:

.. code-block:: python

    from work1_bru import load_lines_from_file
    
    lines = load_lines_from_file('lines.txt')
    for line in lines:
        print(f"{line.name}: Length = {line.length()}")

Advanced Examples
=================

Creating a Campus Map
---------------------

.. code-block:: python

    from work1_bru import Point, Line
    
    # Define campus locations
    locations = {
        'entrance': Point(0, 0, "Main Entrance"),
        'library': Point(15, 30, "Library"),
        'cafeteria': Point(-4, 17, "Cafeteria"),
        'gym': Point(5, 27, "Sports Center"),
    }
    
    # Create paths
    main_path = Line(locations['entrance'], locations['library'], "Main Path")
    side_path = Line(locations['library'], locations['gym'], "Side Path")
    
    # Analyze paths
    print(f"Main Path Distance: {main_path.length():.2f} units")
    print(f"Main Path Slope: {main_path.slope():.2f}")

Analyzing Geometric Properties
-------------------------------

.. code-block:: python

    from work1_bru import Point, Line
    
    # Create a triangle
    p1 = Point(0, 0, "A")
    p2 = Point(4, 0, "B")
    p3 = Point(4, 3, "C")
    
    # Create sides
    side1 = Line(p1, p2, "AB")
    side2 = Line(p2, p3, "BC")
    side3 = Line(p3, p1, "CA")
    
    # Calculate perimeter
    perimeter = side1.length() + side2.length() + side3.length()
    print(f"Perimeter: {perimeter}")  # Output: 12.0
