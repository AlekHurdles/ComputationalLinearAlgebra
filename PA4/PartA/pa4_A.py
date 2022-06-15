import numpy as np
import numpy.linalg
from numpy.linalg import norm


class Triangle:
    def set_point1(self,points):
        self.point1 = points

    def get_point1(self):
        return self.point1

    def set_point2(self,points):
        self.point2 = points

    def get_point2(self):
        return self.point2

    def set_point3(self,points):
        self.point3 = points

    def get_point3(self):
        return self.point3


deminsions = 0
triangle = Triangle()

file = input("Please enter the name of the file you would like to read: Ex(input/test_input.txt)")
outputFile = input("Please enter the name of the output file to write to: (ex: output_files/pa2_output_2.txt) ")
txt_output = open(outputFile, 'w')

with open(file,'r') as f:
    for line in (f.readlines()[-1:]):
        deminsions = float(line)
    f.close()

with open(file,'r') as f:
    if deminsions != 2 and deminsions != 3:
        print("Invalid Dimension. Quitting Program. ")
        txt_output.write("Invalid Dimension. Quitting Program. ")
        txt_output.write("\n")
        quit()
    elif deminsions == 2:
        line1 = f.readline().split()
        line1_list = np.array([float(line1[0]),float(line1[1])])
        triangle.set_point1(line1_list)
        # print(triangle.get_point1())

        line2 = f.readline().split()
        line2_list = np.array([float(line2[0]), float(line2[1])])
        triangle.set_point2(line2_list)
        # print(triangle.get_point2())

        line3 = f.readline().split()
        line3_list = np.array([float(line3[0]), float(line3[1])])
        triangle.set_point3(line3_list)
        # print(triangle.get_point3())

    elif deminsions == 3:
        line1 = f.readline().split()
        line1_list = np.array([float(line1[0]), float(line1[1]), float(line1[2])])
        triangle.set_point1(line1_list)
        # print(triangle.get_point1())

        line2 = f.readline().split()
        line2_list = np.array([float(line2[0]), float(line2[1]), float(line2[2])])
        triangle.set_point2(line2_list)
        # print(triangle.get_point2())

        line3 = f.readline().split()
        line3_list = np.array([float(line3[0]), float(line3[1]), float(line3[2])])
        triangle.set_point3(line3_list)
        # print(triangle.get_point3())


# First Part (Determinant)
if deminsions == 2:
    area = abs(1/2 * ((triangle.get_point1()[0] * (triangle.get_point2()[1] - triangle.get_point3()[1]))
                      + (triangle.get_point2()[0] * (triangle.get_point3()[1] - triangle.get_point1()[1]))
                      + (triangle.get_point3()[0] * (triangle.get_point1()[1] - triangle.get_point2()[1])) ))
    print("Area: ",area)
    txt_output.writelines(str(area))

elif deminsions == 3:
    pq = np.subtract(triangle.get_point1(),triangle.get_point2())
    pr = np.subtract(triangle.get_point1(),triangle.get_point3())
    area = .5 * (np.linalg.norm(np.cross(pq,pr)))
    print(area)
    txt_output.writelines(str(area))

# Second Part (Distance from point to line / bisector)

if deminsions == 2:
    d = "{0:.4g}".format(np.cross(line1_list - line2_list, line1_list - line3_list) / norm(line1_list - line2_list))
    print("Distance: ", d)
    txt_output.write("\n")
    txt_output.writelines(str(d))
elif deminsions == 3:
    add_p1_p2 = np.add(line1_list,line2_list)
    midpoint = np.divide(add_p1_p2,2)
    # print("Midpoint: ", midpoint)

    vector_p1_p2 = np.subtract(line2_list,line1_list)
    normal = norm(vector_p1_p2)
    normalize = np.divide(vector_p1_p2,normal)
    # print("Normalized vector: ",normalize)

    subtract_p3_midpoint = np.subtract(line3_list,midpoint)
    # print("p3 - midpoint: ", subtract_p3_midpoint)

    distance = abs(np.dot(normalize,subtract_p3_midpoint))
    print("Distance: ",distance)
    txt_output.write("\n")
    txt_output.writelines(str(distance))

