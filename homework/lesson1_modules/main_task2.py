# 2. Mastering Python Modules and Aliases
# Task 1: Custom Module with Aliases

# Problem Statement: Create a custom module named text_utils.py with functions for string manipulation 
# (e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.

from text_utils import capitalize_string as caps, upper_case_string as uppies


caps("i love you.")

uppies("she doesn't even go here!")