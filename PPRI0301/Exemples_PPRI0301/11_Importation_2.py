import math
from pydoc import Doc
import numpy as np
# too much values
# from math import acos, asin, atan,ceil,floor,factorial
from math  import pi as MATH_PI
from numpy import pi as NP_PI
from numpy.typing import NDArray
from typing import Any

import Toolbox

def print_values(values : NDArray[np.float64], format : str ="9.6f", carriage_return : int = 5):
    """Print values from an array

    Args:
        values (array like): several values
        format (str, optional): Format for the values printing. Defaults to "9.8f".
        carriage_return (int, optional): Number of value before adding a carriage return. Defaults to 5.
    """
    for i,value in enumerate(values):
        shift:bool=False
        if any(values)<0.0:
            shift=True
        if i>0 and i%carriage_return==0:
            print()
        if shift and value > 0 : print(" ",end="")
        print(f"{value:{format}}", end=" ")
    print()

# print()
# print(f"{MATH_PI:13.12f}")
# print(f"{NP_PI:13.12f}")

# print()
# if MATH_PI==NP_PI:
#     print("\t==> This is the same pi value !!! <==")

# print()
# print(math.cos(MATH_PI/2))
# print(  np.cos(NP_PI  /2))

# print()
# print(f"{math.cos(MATH_PI/2):6.5f}")
# print(f"{  np.cos(NP_PI  /2):13.12f}")

# print()
# values : NDArray[np.float64] = np.linspace(-np.pi,np.pi,10)
# print_values(values)

# print()
# print(math.cos(values))
# values=np.cos(values)
# print_values(values)

# print()
# values=4*values
# Toolbox.print_values_2(values,carriage_return=3)
# print()
