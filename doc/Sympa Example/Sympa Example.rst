
.. code:: python

    from sympy import *
    from sympy.interactive.printing import init_printing
    init_printing()
.. code:: python

    from sympa import domath
.. code:: python

    import pandas as pd
.. code:: python

    df = pd.DataFrame({'x' : range(7)})
    df['x'] = df.x * 10
    df['y'] = df.x * 0.05
    df['r'] = pi * df['y'] / 2
    df



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>x</th>
          <th>y</th>
          <th>r</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>  0</td>
          <td> 0.0</td>
          <td>       0</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 10</td>
          <td> 0.5</td>
          <td> 0.25*pi</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 20</td>
          <td> 1.0</td>
          <td>  0.5*pi</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 30</td>
          <td> 1.5</td>
          <td> 0.75*pi</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 40</td>
          <td> 2.0</td>
          <td>  1.0*pi</td>
        </tr>
        <tr>
          <th>5</th>
          <td> 50</td>
          <td> 2.5</td>
          <td> 1.25*pi</td>
        </tr>
        <tr>
          <th>6</th>
          <td> 60</td>
          <td> 3.0</td>
          <td>  1.5*pi</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    #for those who don't know..."pi" is irrational...
    df['r'][1]



.. math::

    0.25 \pi



.. code:: python

    x,y,r,rn1,x1,xn1,yn1 = symbols('x y r r_-1 x_1 x_-1 y_-1')
    f = x + xn1
    g = x**y + x*y*3.0 + (x1 * 0.5 + xn1 * pi / (yn1 + 1.0))**2
    h = sin(r)
    i = sin(r) / cos(rn1 + 1)
.. code:: python

    f, g, h, i



.. math::

    \left ( x + x_{-1}, \quad 3.0 x y + x^{y} + \left(\frac{\pi x_{-1}}{y_{-1} + 1.0} + 0.5 x_{1}\right)^{2}, \quad \sin{\left (r \right )}, \quad \frac{\sin{\left (r \right )}}{\cos{\left (r_{-1} + 1 \right )}}\right )



.. code:: python

    df.x + df.x.shift(1) #this is easy...but not exactly 



.. parsed-literal::

    0    NaN
    1     10
    2     30
    3     50
    4     70
    5     90
    6    110
    Name: x, dtype: float64



.. code:: python

    #3.0 * df.x * df.y + df.x.mul(df.y) + (df.shift(1).mul(pi).div(df.shift(1) + 1.0))# + (0.5 * df.x.shift(-1))) # what the heck am I doing???
.. code:: python

    df['f'] = domath(df,f)
    df['g'] = domath(df,g)
    df['h'] = domath(df,h)
    df['i'] = domath(df,i)
.. code:: python

    #round the excessive decimals...
    df.g, df.h, df.i = (df[c].round(4) for c in ('g','h','i')); df



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>x</th>
          <th>y</th>
          <th>r</th>
          <th>f</th>
          <th>g</th>
          <th>h</th>
          <th>i</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>  0</td>
          <td> 0.0</td>
          <td>       0</td>
          <td> NaN</td>
          <td>        NaN</td>
          <td> 0.0000</td>
          <td>    NaN</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 10</td>
          <td> 0.5</td>
          <td> 0.25*pi</td>
          <td>  10</td>
          <td>   118.1623</td>
          <td> 0.7071</td>
          <td> 1.3087</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 20</td>
          <td> 1.0</td>
          <td>  0.5*pi</td>
          <td>  30</td>
          <td>  1371.9676</td>
          <td> 1.0000</td>
          <td>-4.6958</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 30</td>
          <td> 1.5</td>
          <td> 0.75*pi</td>
          <td>  50</td>
          <td>  2942.9143</td>
          <td> 0.7071</td>
          <td>-0.8403</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 40</td>
          <td> 2.0</td>
          <td>  1.0*pi</td>
          <td>  70</td>
          <td>  5771.1786</td>
          <td> 0.0000</td>
          <td> 0.0000</td>
        </tr>
        <tr>
          <th>5</th>
          <td> 50</td>
          <td> 2.5</td>
          <td> 1.25*pi</td>
          <td>  90</td>
          <td> 23220.5400</td>
          <td>-0.7071</td>
          <td> 1.3087</td>
        </tr>
        <tr>
          <th>6</th>
          <td> 60</td>
          <td> 3.0</td>
          <td>  1.5*pi</td>
          <td> 110</td>
          <td>        NaN</td>
          <td>-1.0000</td>
          <td>-4.6958</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    assert f.subs([(x,50),(xn1,40)]) == df['f'].iloc[5]
    assert round(g.subs([(x,50),(y,2.5),(xn1,40),(x1,60),(yn1,2.0)]),4) == df['g'].iloc[5]
    assert round(h.subs([(r,1.25*pi)]),4) == df['h'].iloc[5]
    assert round(i.subs([(r,1.25*pi),(rn1,pi)]),4) == df['i'].iloc[5]

