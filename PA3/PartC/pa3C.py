import numpy as np
import numpy.linalg
# ~~~~~~~~~~ Read in file ~~~~~~~~~~
from numpy.linalg import norm

file = input("Enter the name of the .txt file to read from (ex: input_files/pa2_input_1.txt): ")
outputFile = input("Please enter the name of the output file to write to: (ex: output_files/pa2_output_2.txt) ")
txt_output = open(outputFile, 'w')

p1_x = 0
p1_y = 0

p2_x = 0
p2_y = 0

p3_x = 0
p3_y = 0

with open(file, 'r') as f:
    first_row = f.readline().split(" ")
    second_row = f.readline().split(" ")

    p1_x = float(first_row[0])
    p1_y = float(second_row[0])
    p2_x = float(first_row[1])
    p2_y = float(second_row[1])
    p3_x = float(first_row[2])
    p3_y = float(second_row[2])

# Solve for area of the triangle

area = "{0:.4g}".format(abs((1/2) * ((p1_x *(p2_y - p3_y)) + (p2_x *(p3_y - p1_y)) + (p3_x * (p1_y - p2_y)))))
print(area)
txt_output.write(str(area))

# Solve for the distance from point p3 to line formed by p1 & p2

p1 = np.array([p1_x, p1_y])
p2 = np.array([p2_x, p2_y])
p3 = np.array([p3_x, p3_y])
d = "{0:.4g}".format(norm(np.cross(p2-p1, p1-p3))/norm(p2-p1))
print(d)
txt_output.write("\n")
txt_output.write(str(d))

# Solve for foot of the point to the line

w = p3 - p1
v = p2 - p1
t = (np.dot(v,w))/(norm(v)**2)
footx = p1_x + (t*v[0])
footy = p1_y + (t*v[1])
foot = np.array([footx,footy])
print(foot)
txt_output.write("\n")
txt_output.write(str(foot))
