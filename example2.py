#!/usr/bin/env python3
"""
termcursor
================================================================================

Example file for 'termcursor' project
"""

__author__ = 'Richárd Ádám Vécsey Dr.'
__copyright__ = "Copyright 2022, termcursor"
__credits__ = ['Richárd Ádám Vécsey Dr.']
__license__ = 'MIT'
__version__ = '1.0.0'
__status__ = 'Alpha'

from time import sleep

from termcursor import hidecursor, showcursor

print('--- Begin of the example ---')
# Print a test row with default blinking cursor
print('Test content with default (visible) cursor in the next row.')
sleep(3)
# Hide the console cursor
hidecursor()
# Print a test row without visible console cursor
print('Now the cursor is hidden.')
sleep(3)
# Show the console cursor
showcursor()
# Print a test row with visible console cursor
print('The cursor is visible again.')
sleep(3)
print('--- End of the example ---')
