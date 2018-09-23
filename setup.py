from setuptools import setup

setup(name='wollof',
      version='0.1',
      description='Color code and prefix multiple simultaneous running programs output',
      url='http://github.com/rm-hull/follow',
      author='Richard Hull',
      author_email='rm_hull@yahoo.co.uk',
      license='MIT',
      packages=['wollof'],
      install_requires=['colored'],
      scripts=['bin/wollof'],
      zip_safe=False)
