from setuptools import setup

setup(name='anapp',
      version='0.1',
      author='Haris Dimitriou (xarisd)',
      author_email='xaris.dimitriou@gmail.com',
      packages=['anapp', 'anapp.demo'],
      entry_points={
          'console_scripts': [
              'anapp_demo=anapp.demo.greeter_demo:main',
          ],
      },
      )

__author__ = 'Haris Dimitriou (xarisd)'
