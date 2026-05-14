================================
Geometry Package Documentation
================================

Welcome to the Geometry Package documentation!

This package provides classes for working with geometric points and lines in 2D space.

Contents
========

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
   usage

Overview
========

The Geometry Package includes:

- **Point Class**: Represents a point in 2D space with coordinates (x, y) and an optional name
- **Line Class**: Represents a line segment between two points with various geometric properties

Features
========

- Create and manipulate geometric points
- Create and manipulate line segments
- Calculate distances between points
- Find midpoints
- Calculate line slopes and equations
- Load points and lines from files

Installation
============

To install this package, you will need:

- Python 3.6 or higher
- Basic Python knowledge

Quick Start
===========

Creating Points
---------------

.. code-block:: python

    from work1_bru import Point
    
    # Create a point
    p1 = Point(0, 0, "Origin")
    p2 = Point(3, 4, "Point A")
    
    # Calculate distance
    distance = p1.distance_to(p2)
    print(f"Distance: {distance}")

Creating Lines
--------------

.. code-block:: python

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

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
