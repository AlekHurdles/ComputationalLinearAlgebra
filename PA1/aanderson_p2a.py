import numpy as np

#Read matrix files
mat1=np.loadtxt("aanderson_p1_mat1.txt", dtype='i', delimiter=' ')
print(mat1)
print()

mat2=np.loadtxt("aanderson_p1_mat2.txt", dtype='i', delimiter=' ')
print(mat2)
print()

mat3=np.loadtxt("aanderson_p1_mat3.txt", dtype='i', delimiter=' ')
print(mat3)
print()

mat4=np.loadtxt("aanderson_p1_mat4.txt", dtype='i', delimiter=' ')
print(mat4)
print()

mat5=np.loadtxt("aanderson_p1_mat5.txt", dtype='i', delimiter=' ')
print(mat5)
print()

#Add 1 & 2
try:
    mat12=np.add(mat1,mat2)
    print()
    print("Matrix 1 + Matrix 2")
    print(mat12)
except ValueError:
    print("Unable to add Matrix 1 and Matrix 2",ValueError)
    f1 = open("aanderson_p2a12.txt", "a")
    f1.write("Unable to add Matrix 1 and Matrix 2")
    f1.close()

#Add 1 & 3
try:
    mat13=np.add(mat1,mat3)
    print()
    print("Matrix 1 + Matrix 3")
    print(mat13)
except ValueError:
    print("Unable to add Matrix 1 and Matrix 3",ValueError)
    f2 = open("aanderson_p2a13.txt", "a")
    f2.write("Unable to add Matrix 1 and Matrix 3")
    f2.close()

#Add 1 & 4
try:
    mat14=np.add(mat1,mat4)
    print()
    print("Matrix 1 + Matrix 4")
    print(mat14)
except ValueError:
    print("Unable to add Matrix 1 and Matrix 4",ValueError)
    f3 = open("aanderson_p2a14.txt", "a")
    f3.write("Unable to add Matrix 1 and Matrix 4")
    f3.close()

#Add 1 & 5
try:
    mat15=np.add(mat1,mat5)
    print()
    print("Matrix 1 + Matrix 5")
    print(mat15)
except ValueError:
    print("Unable to add Matrix 1 and Matrix 5",ValueError)
    f4 = open("aanderson_p2a15.txt", "a")
    f4.write("Unable to add Matrix 1 and Matrix 5")
    f4.close()

#Add 2 & 3
try:
    mat23=np.add(mat2,mat3)
    matrix23 = np.matrix(mat23)
    print()
    print("Matrix 2 + Matrix 3")
    print(mat23)

    with open('aanderson_p2a_out23.txt', "wb") as f:
        for line in matrix23:
            np.savetxt(f, line, fmt='%.2f')
except ValueError:
    print("Unable to add Matrix 2 and Matrix 3",ValueError)

#Add 2 & 4
try:
    mat24=np.add(mat2,mat4)
    print()
    print("Matrix 2 + Matrix 4")
    print(mat24)
except ValueError:
    print("Unable to add Matrix 2 and Matrix 4",ValueError)

#Add 2 & 5
try:
    mat25=np.add(mat2,mat5)
    print()
    print("Matrix 2 + Matrix 5")
    print(mat25)
except ValueError:
    print("Unable to add Matrix 2 and Matrix 5",ValueError)

#Add 3 & 4
try:
    mat34=np.add(mat3,mat4)
    print()
    print("Matrix 3 + Matrix 4")
    print(mat34)
except ValueError:
    print("Unable to add Matrix 3 and Matrix 4",ValueError)

#Add 3 & 5
try:
    mat35=np.add(mat3,mat5)
    print()
    print("Matrix 3 + Matrix 5")
    print(mat35)
except ValueError:
    print("Unable to add Matrix 3 and Matrix 5",ValueError)

#Add 4 & 5
try:
    mat45=np.add(mat5,mat4)
    matrix45=np.matrix(mat45)
    print()
    print("Matrix 5 + Matrix 4")
    print(mat45)

    with open('aanderson_p2a_out45.txt', "wb") as f:
        for line in matrix45:
            np.savetxt(f, line, fmt='%.2f')
except ValueError:
    print("Unable to add Matrix 4 and Matrix 5",ValueError)


