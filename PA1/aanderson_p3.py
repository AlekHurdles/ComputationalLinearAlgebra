import math

def addVector(v1, v2, w1, w2):
    result1 = float(v1) + float(w1)
    result2 = float(v2) + float(w2)
    addlist = [result1, result2]
    return addlist

def subtractVector(v1,v2,w1,w2):
    result1 = float(v1) - float(w1)
    result2 = float(v2) - float(w2)
    addlist = [result1, result2]
    return addlist

def dotVector(v1, v2, w1, w2):
    result=(float(v1) * float(w1)) + (float(v2) * float(w2))
    return result

def scalingVector(v1,v2,w1,w2):
    v1square=float(v1) * float(v1)
    v2square=float(v2) * float(v2)
    v1plusv2=v1square+v2square
    magnitudeV=math.sqrt(v1plusv2)

    w1scaled=magnitudeV * float(w1)
    w2scaled=magnitudeV * float(w2)
    scaledList= [w1scaled,w2scaled]

    return scaledList

def projectVectors(w1,w2,v1,v2):
    v1square=math.pow(float(v1),2)
    v2square=math.pow(float(v2),2)
    magnitude=math.sqrt(v1square+v2square)
    vmagnitudeSquared=math.pow(magnitude,2)

    dotProduct= (float(w1)*float(v1)) + (float(w2)+float(v2))

    final1=(dotProduct/vmagnitudeSquared)* float(v1)
    final2=(dotProduct/vmagnitudeSquared)* float(v2)

    finalProjection=[final1,final2]

    return finalProjection


myFile=open("aanderson_p3_output", "a")

with open("aanderson_p3_input.txt", 'r') as f:
    for line in f:
        lineList = line.split(" ")

        if (lineList[0].__contains__("AD")):
            addList=addVector(lineList[1], lineList[2], lineList[3], lineList[4])
            print(lineList[0], "= ",addList)
            myFile.write(str(addList)+"\n")
        elif(lineList[0].__contains__("SU")):
            subtractList=subtractVector(lineList[1],lineList[2],lineList[3],lineList[4])
            print(lineList[0], "= ",subtractList)
            myFile.write(str(subtractList)+"\n")
        elif(lineList[0].__contains__("DO")):
            dotProduct=dotVector(lineList[1],lineList[2],lineList[3],lineList[4])
            print(lineList[0], "= ",dotProduct)
            myFile.write(str(dotProduct)+"\n")
        elif(lineList[0].__contains__("SC")):
            scaledVector=scalingVector(lineList[1],lineList[2],lineList[3],lineList[4])
            print(lineList[0], "= ",scaledVector)
            myFile.write(str(scaledVector)+"\n")
        elif(lineList[0].__contains__("PR")):
            projectedVector=projectVectors(lineList[1],lineList[2],lineList[3],lineList[4])
            print(lineList[0], "= ",projectedVector)
            myFile.write(str(projectedVector)+"\n")
        else:
            print(f"{lineList[0]} is not an allowed operation")
            myFile.write(f"{lineList[0]} is not an allowed operation")


classFile=open("class_p3_output.txt", "a")

with open("class_p3_input.txt", 'r') as f:
    for line in f:
        lineList = line.split(" ")

        if (lineList[0].__contains__("AD")):
            addList=addVector(lineList[1], lineList[2], lineList[3], lineList[4])
            print(lineList[0], "= ",addList)
            classFile.write(str(addList) + "\n")
        elif(lineList[0].__contains__("SU")):
            subtractList=subtractVector(lineList[1],lineList[2],lineList[3],lineList[4])
            print(lineList[0], "= ",subtractList)
            classFile.write(str(subtractList) + "\n")
        elif(lineList[0].__contains__("DO")):
            dotProduct=dotVector(lineList[1],lineList[2],lineList[3],lineList[4])
            print(lineList[0], "= ",dotProduct)
            classFile.write(str(dotProduct) + "\n")
        elif(lineList[0].__contains__("SC")):
            scaledVector=scalingVector(lineList[1],lineList[2],lineList[3],lineList[4])
            print(lineList[0], "= ",scaledVector)
            classFile.write(str(scaledVector) + "\n")
        elif(lineList[0].__contains__("PR")):
            projectedVector=projectVectors(lineList[1],lineList[2],lineList[3],lineList[4])
            print(lineList[0], "= ",projectedVector)
            classFile.write(str(projectedVector) + "\n")
        else:
            print(f"{lineList[0]} is not an allowed operation")
            classFile.write(f"{lineList[0]} is not an allowed operation")










