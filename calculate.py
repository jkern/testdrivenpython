#!/usr/bin/python
"""By Jospeh Kern
        Demonstrating Test Driven Development in Python Using unittest"""

import sys

from calc import add, sub, mul, div

localadd = add.ADD()
localsub = sub.SUB()
localmul = mul.MUL()
localdiv = div.DIV()


#Since our "REAL" code is separated from the user interface portion,
#and we know that all the other code works, we can just start writing
#the interface portion. Quick and dirty. Let's GO!

def main():

        print "Welcome!"
        a = float(raw_input("Enter your first number: "))
        b = raw_input("Enter your operator: ")
        c = float(raw_input("Enter your last number: "))

        if b == '+':
                print localadd.TWOnumbers(a,c)
        elif b == '-':
                print local.sub.TWOnumbers(a,c)
        elif b == '*':
                print localmul.TWOnumbers(a,c)
        elif b == '/':
                print localdiv.TWOnumbers(a,c)
        else:
                sys.exit(1)

if __name__ == "__main__":
        main()
