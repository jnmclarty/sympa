
# coding: utf-8

# In[1]:

from sympy import *
from sympy.interactive.printing import init_printing
init_printing()


# In[2]:

from sympa import domath


# In[3]:

import pandas as pd


# In[4]:

df = pd.DataFrame({'x' : range(7)})
df['x'] = df.x * 10
df['y'] = df.x * 0.05
df['r'] = pi * df['y'] / 2
df


# In[5]:

#for those who don't know..."pi" is irrational...
df['r'][1]


# In[6]:

x,y,r,rn1,x1,xn1,yn1 = symbols('x y r r_-1 x_1 x_-1 y_-1')
f = x + xn1
g = x**y + x*y*3.0 + (x1 * 0.5 + xn1 * pi / (yn1 + 1.0))**2
h = sin(r)
i = sin(r) / cos(rn1 + 1)


# In[7]:

f, g, h, i


# In[8]:

df.x + df.x.shift(1) #this is easy...but not exactly 


# In[9]:

#3.0 * df.x * df.y + df.x.mul(df.y) + (df.shift(1).mul(pi).div(df.shift(1) + 1.0))# + (0.5 * df.x.shift(-1))) # what the heck am I doing???


# In[10]:

df['f'] = domath(df,f)
df['g'] = domath(df,g)
df['h'] = domath(df,h)
df['i'] = domath(df,i)


# In[11]:

#round the excessive decimals...
df.g, df.h, df.i = (df[c].round(4) for c in ('g','h','i')); df


# In[12]:

assert f.subs([(x,50),(xn1,40)]) == df['f'].iloc[5]
assert round(g.subs([(x,50),(y,2.5),(xn1,40),(x1,60),(yn1,2.0)]),4) == df['g'].iloc[5]
assert round(h.subs([(r,1.25*pi)]),4) == df['h'].iloc[5]
assert round(i.subs([(r,1.25*pi),(rn1,pi)]),4) == df['i'].iloc[5]


# In[12]:




# In[ ]:



