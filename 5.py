"""Write a program that prints out the sine and cosine of the angles ranging from 0 to 345◦
in 15◦ increments. Each result should be rounded to 4 decimal places.
Sample output is shown below:"""
from math import *
for i in range(0,360,15):
    print(i,'___', round(sin(i),4),round(cos(i),4))
    
