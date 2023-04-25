#
#  Example program for Targil 1
#
import math
from myboolfuncs import *

#
# Area calculation program  
def rectangleArea(w, h):
     return w*h
#
def circleArea(r):
     return math.pi * r**2
#
def sphereVolume(r):
    return (4/3) * math.pi * r**3
#
def coneVolume(r, h):
    return (math.pi * r**2 * h)/3
#
def squarePyramidVolume(a, h):
    return (a * h) / 3
#


#
# printing the menu options
def prtMenu(shapes):
   for i in range(len(shapes)):
      print (i+1, shapes[i])
   return
#
# main program
#
print ("Welcome to the Area calculation program")
print ("---------------------------------------\n")  
# Print out the menu
shapes = ("Rectangle", "Circle","sphere","cone","square pyramid")
while True:
    print ("\nPlease select a shape (press 0 to quit):")
    prtMenu(shapes) 
    # Get the user's choice: 
    shape = input("> ")
    # Calculate the area: 
    if shape == "1":
         height = getNumber("Please enter the height: ")    
         width  = getNumber("Please enter the width: ")
         area = rectangleArea(width, height)
         print ("The area is", area)
         continue
    elif shape == "2":
         radius = getNumber("Please enter the radius: ")
         area   = circleArea(radius)
         print ("The area is", area)
         continue
    elif shape == "3":      #sphere
        radius = getNumber("Please enter the radius: ")
        area = sphereVolume(radius)
        print("The sphere volume is", area)
    elif shape == "4":  # cone
        radius = getNumber("Please enter the radius: ")
        height = getNumber("Please enter the height: ")
        area = coneVolume(radius, height)
        print("The cone volume is", area)
    elif shape == "5":  # square pyramid
        a = getNumber("Please enter the base area: ")
        height = getNumber("Please enter the height: ")
        area = squarePyramidVolume(a, height)
        print("The square pyramid volume is", area)
    elif shape == "0":
         print ("Bye!")
         break
    else:     
         print ("Invalid shape")


# Welcome to the Area calculation program
# ---------------------------------------
#
#
# Please select a shape (press 0 to quit):
# 1 Rectangle
# 2 Circle
# 3 sphere
# 4 cone
# 5 square pyramid
# > 3
# Please enter the radius: 3.0
# The sphere volume is 113.09733552923254
#
# Please select a shape (press 0 to quit):
# 1 Rectangle
# 2 Circle
# 3 sphere
# 4 cone
# 5 square pyramid
# > 4
# Please enter the radius: 2.5
# Please enter the height: 4.7
# The cone volume is 30.76142806640006
#
# Please select a shape (press 0 to quit):
# 1 Rectangle
# 2 Circle
# 3 sphere
# 4 cone
# 5 square pyramid
# > 5
# Please enter the base area: 2.0
# Please enter the height: 5.2
# The square pyramid volume is 3.466666666666667
#
# Please select a shape (press 0 to quit):
# 1 Rectangle
# 2 Circle
# 3 sphere
# 4 cone
# 5 square pyramid
# > 0
# Bye!