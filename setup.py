import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

v = '0.1.0'
print "Setting up sympa"

setup(
  name = 'sympa',
  version = v,
  packages = ['sympa'],
  description = 'Symbolic math for pandas',
  long_description=(read('README.rst')),
  author = 'Jeffrey McLarty',
  author_email = 'jeffrey.mclarty@gmail.com',
  url = 'https://github.com/jnmclarty/sympa',
  download_url = 'https://github.com/jnmclarty/sympa/tarball/' + v,
  keywords = ['symbolic', 'symbol', 'sympa', 'sympy', 'pandas', 'math'],
  classifiers = ['Development Status :: 1 - Planning',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Education',
                 'Intended Audience :: Financial and Insurance Industry',
                 'Intended Audience :: Healthcare Industry',
                 'Intended Audience :: Science/Research',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.4',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Scientific/Engineering :: Mathematics'])