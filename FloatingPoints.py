# HOMEWORK 3 --- ES2
# Floating Point Numbers

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Zosia Stafford
# NUMBER OF HOURS TO COMPLETE:
# YOUR COLLABORATION STATEMENT(s):
#
#
#*****************************************


# One weird problem with Python is that floating numbers are saved in
# a way that causes Python to represent decimals in a way that is slightly
# different from the actual value of the decimal. This is because our number
# system is what is called base 10, meaning the units represent multiples of
# 10 (for example, 100, 10, 1, 1/10, 1/100, etc). Python stores values as binary
# numbers. That is base 2 (for example, 16, 8, 4, 2, 1, 1/2, 1/4 1/8, 1/16).
# It is not important to deeply understand binary numbers at this point except to understand how
# decimal numbers are influenced.

# Some decimal numbers work "well" in both base 10 and base 2 counting and these numbers are stored
# in a Python in a way that floats behave as we would expect.
# For example, .125 is 1/10+2/100+5/1000 in base 10 and is 0/2 + 0/4 + 1/8 in base 2.
# But most fractions and decimals cannot be accurately represented by floats.

# You may want to read more here about floats : https://docs.python.org/3/tutorial/floatingpoint.html

# We can see this problem in action. Try the following commands in a REPL:
# >>>  .1 + .1 + .1 == .3

# >>> .3

# Round the numbers does not work either, as the issue is not with a rounding problem and is actually
# coming from how the number is stored.
# >>> round(.1, 2) + round(.1, 2) + round(.1, 2) == round(.3, 2)

# This issue is also often reflected in fractions.


# Run this code in Python 3 mode.

# ****************************************************************************************************
# ***** Import Statements ****************************************************************************
# ****************************************************************************************************
import math

# ****************************************************************************************************
# **************** Custom Function*******************************************************************
# ****************************************************************************************************

def almost_equal(A, B):
    close = 10**-9
    if abs(A-B) >= close:
    # Complete a function called almost_equal, which takes two arguments (two floating numbers) and
    # returns True (boolean) if the difference is less than or equal to 0.000000001 which in Python may be written as 10**-9.
    # It should return False (boolean) if the difference is greater than 0.000000001.
    # Create your function here.
        return False


# ****************************************************************************************************
# ******* Body of Code *******************************************************************************
# ****************************************************************************************************

print("This should be 'True', but floating point error make it 'False': ", .1+.1+.1 == .3)
print("Our almost_equal function returns the correct result: ", almost_equal(.1+.1+.1,.3))