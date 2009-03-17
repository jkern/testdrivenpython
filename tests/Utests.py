#!/usr/bin/python

import unittest
import sys

# first we need to make sure that we are in the right directory to start the test
TEST_ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(TEST_ROOT + "/..")
# This is pretty much just boiler plate. Copy Pasta.
sys.path = [ROOT] + sys.path

# Since we are doing TEST driven development, we need to start with a test.
# duh.

# In general, a calculator should be able to add subtract divide and multiply.
# Testing shouldn't be too hard then.

# Checking for sanity, is an important step in any test or development process.

class IsThisThingOn:
        def MicCheck(self):
                return 1

class SanityTest(unittest.TestCase):
        def testIsThisThingOn(self):
                test = IsThisThingOn()
                localCheck = test.MicCheck()
                self.assertEqual(1, localCheck)

# The above blocks of code will help us build more tests below

# Let's start the tests!

class UnitTests(unittest.TestCase):
        def testADD(self):




if __name__ == '__main__':
        unittest.main()
