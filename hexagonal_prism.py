#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on August 2020
# This program calculates the surface area and volume of a hexagonal prism
#   with user input

import math


def main():
    # This function calculates the surface area and volume

    # Input
    base_edge = float(input("Enter Length of the Base Edge of the Hexagonal"
                            " Prism (mm): "))
    height = float(input("Enter Height of the Hexagonal Prism (mm): "))

    # Process
    surface_area = 6 * base_edge * height + 3 * math.sqrt(3) * base_edge**2
    volume = (3 * math.sqrt(3)) / 2 * base_edge**2 * height

    # Output
    print("")
    print("If a hexagonal prism has a base edge length of {0}mm, and a height"
          " of {1}mm: ".format(base_edge, height))
    print("")
    print("Surface Area is {0:.2f}mm^2".format(surface_area))
    print("Volume is {0:.2f}mm^3".format(volume))


if __name__ == "__main__":
    main()
