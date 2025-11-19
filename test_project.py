# Author: Eduardo Salinas

import pytest  # This will allow me to do unit testing with pytest

# This imports the 3 functions that I want to test from project.py
from project import damage_calculation, health_points_remaining_calculation, drink_potion

""" ## Unit tests for testing project.py, that is, tests for testing my final project.

"""

""" ### Unit test for function 1: Test to test the Damage Calculation function.

I will see if I get a Value Error if I try to insert a negative number to the Damage Calculation function. If so,
I'll pass the test. I will check if it detects numbers between -30 and -10 (it will never reach 9), since it will 
generate random numbers, so I need to detect a range of numbers.

I need to use "with pytest.raises(ValueError):" to check with pytest if a Value Error occurs (source: my 
"Refueling" assignment from Week 5 from my 2025 homework assignment submission for Harvard's CS50 Python's course).
"""


def test_damage_calculation_negative_numbers():
    with pytest.raises(ValueError):
        assert (damage_calculation(-20)) in range(-30, -9)
