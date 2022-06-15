import math

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

    def set_vector_v(self,vectorv):
        self.vvector = vectorv

    def get_vector_v(self):
        return self.vvector

    def set_vector_w(self, vectorw):
        self.wvector = vectorw

    def get_vector_w(self):
        return self.wvector

    def set_normal(self,norm):
        self.normal = norm

    def get_normal(self):
        return self.normal



facet_list = []
file = input("Please enter the name of the file you would like to read: Ex(input/test_input2.txt)")
outputFile = input("Please enter the name of the output file to write to: (ex: output_files/pa2_output_2.txt) ")
txt_output = open(outputFile, 'w')

with open(file,'r') as f:
    first_line = f.readline().split()
    eye_location= np.array([float(first_line[0]),float(first_line[1]),float(first_line[2])])
    light_source = np.array([float(first_line[3]),float(first_line[4]),float(first_line[5])])

    for tri in f:
        triangle = Triangle()
        tempList = tri.split()

        if len(tempList) > 8:
            point_p = np.array([float(tempList[0]),float(tempList[1]),float(tempList[2])])
            point_q = np.array([float(tempList[3]),float(tempList[4]),float(tempList[5])])
            point_r = np.array([float(tempList[6]),float(tempList[7]),float(tempList[8])])
            v_vector = np.subtract(point_q,point_p)
            w_vector = np.subtract(point_r,point_p)

            crossvw = np.cross(v_vector,w_vector)
            norml = norm(crossvw)

            n1 = float(crossvw[0]) / float(norml)
            n2 = float(crossvw[1]) / float(norml)
            n3 = float(crossvw[2]) / float(norml)

            normal = np.array([n1,n2,n3])
            triangle.set_point1(point_p)
            triangle.set_point2(point_q)
            triangle.set_point3(point_r)
            triangle.set_vector_v(v_vector)
            triangle.set_vector_w(w_vector)
            triangle.set_normal(normal)

            facet_list.append(triangle)

# Culling for the triangle

for i in range(len(facet_list)):

    centroidx = (facet_list[i].get_point1()[0] + facet_list[i].get_point2()[0] + facet_list[i].get_point3()[0]) / 3
    centroidy = (facet_list[i].get_point1()[1] + facet_list[i].get_point2()[1] + facet_list[i].get_point3()[1]) / 3
    centroidz = (facet_list[i].get_point1()[2] + facet_list[i].get_point2()[2] + facet_list[i].get_point3()[2]) / 3
    centroid = np.array([centroidx,centroidy,centroidz])

    # print(centroid)

    e_c = np.subtract(eye_location,centroid)
    facet_vector = e_c / np.linalg.norm(e_c)
    facet_direction = np.dot(facet_list[i].get_normal(),facet_vector)
    # print(facet_direction)

    if facet_direction >= 0:
        print('1')
        txt_output.write('1\t\t')
    else:
        print('0')
        txt_output.write('0\t\t')

# Light Intensity
txt_output.write('\n')
for i in range(len(facet_list)):
    centroidx = (facet_list[i].get_point1()[0] + facet_list[i].get_point2()[0] + facet_list[i].get_point3()[0]) / 3
    centroidy = (facet_list[i].get_point1()[1] + facet_list[i].get_point2()[1] + facet_list[i].get_point3()[1]) / 3
    centroidz = (facet_list[i].get_point1()[2] + facet_list[i].get_point2()[2] + facet_list[i].get_point3()[2]) / 3
    centroid = np.array([centroidx, centroidy, centroidz])

    light_direction = np.subtract(centroid, light_source)
    # print("light directions", light_direction)
    normal_light_intensity = np.linalg.norm(light_direction)
    # print("lighting normalized", normal_light_intensity)

    normalized_light = np.divide(light_direction,normal_light_intensity)
    # print(normalized_light)

    angle_of_incidence = np.dot(normalized_light,facet_list[i].get_normal())
    # print(angle_of_incidence)

    # |cos(x)|
    final_intensity = abs(math.cos(angle_of_incidence))
    print(final_intensity)
    txt_output.writelines("{0:.4g}\t".format(final_intensity))

txt_output.write('\n')
for i in range(len(facet_list)):
    centroidx = (facet_list[i].get_point1()[0] + facet_list[i].get_point2()[0] + facet_list[i].get_point3()[0]) / 3
    centroidy = (facet_list[i].get_point1()[1] + facet_list[i].get_point2()[1] + facet_list[i].get_point3()[1]) / 3
    centroidz = (facet_list[i].get_point1()[2] + facet_list[i].get_point2()[2] + facet_list[i].get_point3()[2]) / 3
    centroid = np.array([centroidx, centroidy, centroidz])

    # print(centroid)

    e_c = np.subtract(eye_location, centroid)
    facet_vector = e_c / np.linalg.norm(e_c)
    facet_direction = np.dot(facet_list[i].get_normal(), facet_vector)
    # print(facet_direction)

    if facet_direction >= 0:
        centroidx = (facet_list[i].get_point1()[0] + facet_list[i].get_point2()[0] + facet_list[i].get_point3()[0]) / 3
        centroidy = (facet_list[i].get_point1()[1] + facet_list[i].get_point2()[1] + facet_list[i].get_point3()[1]) / 3
        centroidz = (facet_list[i].get_point1()[2] + facet_list[i].get_point2()[2] + facet_list[i].get_point3()[2]) / 3
        centroid = np.array([centroidx, centroidy, centroidz])

        light_direction = np.subtract(centroid, light_source)
        # print("light directions", light_direction)
        normal_light_intensity = np.linalg.norm(light_direction)
        # print("lighting normalized", normal_light_intensity)

        normalized_light = np.divide(light_direction, normal_light_intensity)
        # print(normalized_light)
        # If it is perpendicular, then x is 1. However, if it is not, then x is the angle between the perpendicular light source
        # and the actual angle of the light intensity vector. This is the angle that I need to find.....

        angle_of_incidence = np.dot(normalized_light, facet_list[i].get_normal())
        # print(angle_of_incidence)

        # |cos(x)|
        final_intensity = abs(math.cos(angle_of_incidence))
        print(final_intensity)
        txt_output.write("{0:.4g}\t".format(final_intensity))
    else:
        print("Culled")
        txt_output.write('Culled\t')







