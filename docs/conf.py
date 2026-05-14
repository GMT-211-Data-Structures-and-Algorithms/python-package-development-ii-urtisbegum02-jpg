# Configuration file for Sphinx documentation generator.

import os
import sys

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Project information
project = 'Geometry Package'
copyright = '2026, Student'
author = 'Student'
release = '0.1.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that should be ignored when building the documentation.
exclude_patterns = ['_build']

# The theme to use for HTML and HTML Help pages.
# Using Alabaster theme (one of the popular Sphinx themes)
html_theme = 'alabaster'

# Theme options are theme-specific and used by builders.
html_theme_options = {
    'logo': '',
    'github_user': '',
    'github_repo': '',
    'description': 'A Python package for geometric point and line operations',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the build-time HTML is built.
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names to template names.
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}

# Output file base name for HTML help builder.
htmlhelp_basename = 'GeometryPackagedoc'

# Sphinx napoleon extension settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True

# Autodoc settings
autodoc_member_order = 'bysource'
autoclass_content = 'both'
