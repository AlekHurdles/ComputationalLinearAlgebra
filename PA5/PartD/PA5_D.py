# Part D solves for the intersection of a line and various planes (Bounded by 3 vertecies(1) of unbounded(0))

import numpy as np

class Plane:
    def setV1(self, v1):
        self.v1 = v1

    def getV1(self):
        return self.v1

    def setV2(self, v2):
        self.v2 = v2

    def getV2(self):
        return self.v2

    def setV3(self, v3):
        self.v3 = v3

    def getV3(self):
        return self.v3

# read in file, and store line + plane information

inputfile = input("Please enter the file you would like to read: EX: input/testData.txt ")
outputfile = input("Please enter the output file to store information: EX: output/testData.txt")
txt_output = open(outputfile, 'w')

planelist = []
line = []

with open(inputfile,'r') as f:
    firstline = f.readline().split()

    linepoint1 = np.array([float(firstline[0]),float(firstline[1]), float(firstline[2])])
    linepoint2 = np.array([float(firstline[3]),float(firstline[4]), float(firstline[5])])

    line = np.subtract(linepoint2,linepoint1)

    for line in f:
        plane = Plane()
        data = line.split()

        plane.setV1(np.array([float(data[0]), float(data[1]), float(data[2])]))
        plane.setV2(np.array([float(data[3]), float(data[4]), float(data[5])]))
        plane.setV3(np.array([float(data[6]), float(data[7]), float(data[8])]))

        planelist.append(plane)

# Calculate the intersection point of the line and each plane

for x in range(len(planelist)):

    # To find the intersection, find to T to satisfy: p +tV = p1 + u1(p2 - p1) + u2(p3 - p1)
    print()




