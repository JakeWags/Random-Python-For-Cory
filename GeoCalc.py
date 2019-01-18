# Calculates geometric shapes' attributes.

import math

def calculate(shape):
    if shape == "Square":
        sideLength = int(input("Side length: "))
        print("Perimeter: " + str(sideLength * 4) + ", Area: " + str(sideLength * sideLength))
    elif shape == "Equal Triangle":
        base = int(input("Base: "))
        print("Perimeter: " + str(base * 3) + ", Area: " + str(base * base))
    elif shape == "Circle":
        radius = int(input("Radius: "))
        print("Circumference: " + str(2 * math.pi * radius) + ", Area: " + str(math.pi * radius * radius))

shapes = ["Square", "Equal Triangle", "Circle"]

shapeChoice = input("Choose one of the following options: " + str(shapes) + ":\n")

for shape in shapes:
    if shapeChoice == shape:
        calculate(shape)

