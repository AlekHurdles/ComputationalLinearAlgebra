# This program will read through a file, each line contains plane data and an outlier point. The goal is to
# Calculate the distance between the point on the plane and the outlier point.

import numpy as np

class Plane:

    def getNormal(self):
        return self.normal

    def setNormal(self,normal):
        # normalized = np.linalg.norm(normal)
        self.normal = normal

    def setpoint(self,point):
        self.point = point

    def getpoint(self):
        return self.point

    def setx(self,pointx):
        self.pointx = pointx

    def getx(self):
        return self.pointx


# Read in file and store the data
inputFile = input("Please enter the file you would like to analyze: ex(input/testData.txt)")
outputFile = input("Please enter the name of your output file: ex(output/testData.txt) ")
txt_output = open(outputFile, 'w')

pointsList = []

with open(inputFile,'r') as f:

    for line in f:
        plane = Plane()
        data = line.split()

        point = np.array([float(data[0]),float(data[1]),float(data[2])])
        plane.setpoint(point)

        normal = np.array([float(data[3]),float(data[4]),float(data[5])])
        plane.setNormal(normal)

        xpoint = np.array([float(data[6]),float(data[7]),float(data[8])])
        plane.setx(xpoint)

        pointsList.append(plane)

for x in range(len(pointsList)):

    # normalize normal
    magnitude = np.linalg.norm(pointsList[x].getNormal())
    normalizedn = np.divide(pointsList[x].getNormal(),magnitude)
    ndotn = np.dot(normalizedn,normalizedn)

    # solve for c
    c = np.negative(np.dot(normalizedn,pointsList[x].getpoint()))

    # solve for distance / normalized Tval
    distance = (c + np.dot(normalizedn,pointsList[x].getx()))
    print(distance)

    # solve for q (point on plane)
    q = np.subtract(pointsList[x].getx(),np.multiply(distance,normalizedn))
    print(q)

    txt_output.write(str(q))
    txt_output.write(str(distance))
    txt_output.write('\n')


