"""A demo app for Greeter"""
print('Hi from me!')
# import sys
# import os
# from pprint import pprint as pp
# pp(os.path.relpath())
# sys.path.append(os.path.pardir(os.path.abspath(__file__)))
from anapp.demo.greeter import Greeter


def main():
    g = Greeter()
    g.hello()


if __name__ == "__main__":
    main()
