import numpy
import numpy as np


class Plane:

    def getNormal(self):
        return self.normal

    def setNormal(self,normal):
        self.normal = normal

    def setpoint(self,point):
        self.point = point

    def getpoint(self):
        return self.point

    def setdirection(self,direction):
        self.direction = direction

    def getdirection(self):
        return self.direction
class Point:
    def setpoint(self,point):
        self.point = point

    def getpoint(self):
        return self.point


# Read in file and store the data

inputFile = input("Please enter the file you would like to analyze: ex(input/testData.txt)")
outputFile = input("Please enter the name of your output file: ex(output/testData.txt) ")
txt_output = open(outputFile, 'w')

pointsList = []
plane = Plane()

with open(inputFile,'r') as f:
    planeData = f.readline().split()

    planePoint = np.array([float(planeData[0]),float(planeData[1]),float(planeData[2])])
    plane.setpoint(planePoint)

    planeNormal = np.array([float(planeData[3]),float(planeData[4]),float(planeData[5])])
    plane.setNormal(planeNormal)

    planeDirection = np.array([float(planeData[6]),float(planeData[7]),float(planeData[8])])
    plane.setdirection(planeDirection)

    for line in f:
        point1 = Point()
        point2 = Point()
        point3 = Point()

        rl = line.split()
        rl1 = np.array([float(rl[0]),float(rl[1]),float(rl[2])])
        rl2 = np.array([float(rl[3]),float(rl[4]),float(rl[5])])
        rl3 = np.array([float(rl[6]),float(rl[7]),float(rl[8])])

        point1.setpoint(rl1)
        point2.setpoint(rl2)
        point3.setpoint(rl3)

        pointsList.append(point1)
        pointsList.append(point2)
        pointsList.append(point3)

# Implement parallel projection. For each point, project it along the projection direction to into the plane.
primepoints = []
for point in range(len(pointsList)):
    t = np.divide(np.dot((np.subtract(plane.getpoint(),pointsList[point].getpoint())),plane.getNormal()),np.dot(plane.getdirection(),plane.getNormal()))
    primepoint = np.add(pointsList[point].getpoint(),np.multiply(t,plane.getdirection()))

    primepoints.append(primepoint)

# Write points to text file
for a in range(len(primepoints)):
    if a % 3 == 0:
        txt_output.write('\n')

    txt_output.write(str(primepoints[a]))







