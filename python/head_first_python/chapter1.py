#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
A python file to contain all the example code and the logid from Chapter1.

The Chapter 1 of Head First Python Book. All the sample code are in the
function examples while all the to do programs are in the functions with
the prefix exercises.
"""

from datetime import datetime


class Chapter1:
    """
    Chapter1 class contains all the code for First Chapter in HFPython Book.

    All the code is to implement the ideas and the logic from the book.
    """

    def __init__(self):
        """
        Init is the function used to start the objects execution.

        All the variables can be initialized here.
        """
        print("Class Chapter 1 Initialzed!\n")

    def examples(self):
        """
        First function inside the class.

        All the code is from the Chapter 1.
        """
        print("Examples:")
        # Question 1
        print("What's REPL?: \n read-eval-print-loop")
        print("Example 1:- Code to find out current minute is odd or not.")
        # Example 1
        right_this_minute = datetime.today().minute
        if right_this_minute % 2 == 0:
            print("Not an odd minute.")
        else:
            print("This minute seems a little odd.")
        # Question 2
        print("Is python interåreter and the Java JVM are the same?\n Java ",
              "depends on the class files and use them during their ",
              "execution. However Python interpreter runs the source code ",
              "directly while no class files are generated in that stage.")
        #  Question 3
        # https://stackoverflow.com/questions/48878730/what-is-the-difference-between-python-function-and-python-module
        print("What's the difference between a function and a module?\n ",
              " Needs PEP Definitions here:- \n",
              " For now I'm using the good explanation from Stack ",
              " Overflow. A function is a code block that can be called.",
              " Where as a module can contain functions, and classes ",
              " The module can also be executed like a python program. ")
        # Functions + Modules = Standard Library
        # For example, refer the datetime module(3.7) here in the following URL
        # https:/ github.com/python/cpython/blob/3.7/Lib/datetime.py


def main():
    """
    Execution of the code in this file will start from this function.

    So Main function will be called from main().
    """
    chapter_1 = Chapter1()
    chapter_1.examples()


if __name__ == '__main__':
    main()
