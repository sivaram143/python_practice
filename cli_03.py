#!/usr/bin/python

import sys
import pprint


def listMethods():
    module = sys.argv[1]
    if not module:
        import module
    print(dir(module))

if __name__ == '__main__':
    listMethods()