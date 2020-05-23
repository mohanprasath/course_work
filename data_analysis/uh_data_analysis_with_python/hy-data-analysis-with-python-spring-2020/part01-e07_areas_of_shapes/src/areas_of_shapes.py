#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    while(True):
        choice = str(input("Choose a shape (triangle, rectangle, circle): "))
        if choice == 'triangle':
            base = int(input("Give base of the triangle: "))
            height = int(input("Give height of the triangle: "))
            print("The area is %.6f" %(0.5 * base * height))
        elif choice == 'rectangle':
            width = int(input("Give width of the rectangle: "))
            height = int(input("Give height of the rectangle: "))
            print("The area is %.6f" %(width * height))
        elif choice == 'circle':
            radius = int(input("Give radius of the circle: "))
            print("The area is %.6f" %(math.pi * radius ** 2))
        elif choice == "":
            break
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
