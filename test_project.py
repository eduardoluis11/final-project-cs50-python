# Author: Eduardo Salinas

import pytest  # This will allow me to do unit testing with pytest

# This imports the 3 functions that I want to test from project.py
from project import damage_calculation, health_points_remaining_calculation, drink_potion

""" ## Unit tests for testing project.py, that is, tests for testing my final project.

I changed the name of the 3 unit tests so that they have the exact same name of their respective custom functions,
as requested by the instructions for the Final Project.
"""

""" ### Unit test for function 1: Test to test the Damage Calculation function.

I will see if I get a Value Error if I try to insert a negative number to the Damage Calculation function. If so,
I'll pass the test. I will check if it detects numbers between -30 and -10 (it will never reach 9), since it will 
generate random numbers, so I need to detect a range of numbers.

I need to use "with pytest.raises(ValueError):" to check with pytest if a Value Error occurs (source: my 
"Refueling" assignment from Week 5 from my 2025 homework assignment submission for Harvard's CS50 Python's course).
"""


def test_damage_calculation():
    with pytest.raises(ValueError):
        assert (damage_calculation(-20)) in range(-30, -9)


""" ### Unit test for function 2: Test for the HP Remaining Calculation() function.

Neither the current Health Points nor the Total Damage Dealt can be floats, nor strings. So, I'll try to raise
a Value Error if at least 1 of those parameters are a float, for instance.
"""


def test_health_points_remaining_calculation():
    with pytest.raises(ValueError):
        assert (health_points_remaining_calculation(50.5, 20)) == 30.5


""" ### Unit test for function 3: Test for the Drink Potion() function.

For the potion drinking mechanic, I could simply check that the user’s HP is healed correctly. That is, if you have 
200 HP in total HP, and you have 80 HP left, that if you drink the potion, you will have 160 HP after drinking the 
potion. 
"""


def test_drink_potion():
    assert (drink_potion(80, 200)) == 160
