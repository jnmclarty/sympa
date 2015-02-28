Sympa
=====

*Symbolic math for pandas.*

Description
===========

Links symbolic expressions created using sympy to columns of data in pandas DataFrames.
Any expression created with sympy, which can be "lambdified", will/should/might work. 

Warning
=======

The API design for sympa is subject to change, depending on feedback, if any.

Usage
=====

.. code:: python

   from pandas import DataFrame
   from sympy import symbols
   from sympa import domath
   
   df = pd.DataFrame({'x' : [1,2,3,4] * 2, 'y' : [0.1, 0.2] * 4)
   
   # Notice x_-1 and x_-2 are used to reference x @ t=-1, and x @ t=-2.
   x, xn1, xn2, y = symbols('x x_-1 x_-2 y')
   
   f = 3.0 * x ** 3 + 2.0 * xn1 ** 2 + xn2 + (y * 2) / 2
   
   df['f'] = domath(df,f)

Docs
====

For now, there isn't much documentation.  I think it's pretty straightforward.
Check out the /doc folder of the repo on github for more examples.

Requirements
============

* Sympy >= 0.7.6 but should work with much older versions (untested).
* Pandas >= 0.15 but should work with much older versions (untested).

Python
------
Works on 2.7, untested on all other versions.
It is expected to be ported to 3.4 soon, and likely 2.6 as well.

Install
=======

    pip install sympa