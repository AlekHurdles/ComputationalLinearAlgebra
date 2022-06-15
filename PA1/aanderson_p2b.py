import numpy as np

#Read matrix files
mat1=np.loadtxt("aanderson_p1_mat1.txt", dtype='i', delimiter=' ')
#print(mat1)

mat2=np.loadtxt("aanderson_p1_mat2.txt", dtype='i', delimiter=' ')
#print(mat2)


mat3=np.loadtxt("aanderson_p1_mat3.txt", dtype='i', delimiter=' ')
#print(mat3)


mat4=np.loadtxt("aanderson_p1_mat4.txt", dtype='i', delimiter=' ')
#print(mat4)


mat5=np.loadtxt("aanderson_p1_mat5.txt", dtype='i', delimiter=' ')
#print(mat5)


#Mat 1 * Mat 2
mat12=np.zeros(shape=(10,8))
for i in range(len(mat1)):
    for j in range(len(mat2)):
        for k in range(len(mat2)):
            mat12[i][j] += mat1[i][k] * mat2[k][j]
print("Mat 1 * Mat 2")
print(mat12)
savemat12=open("aander24_p2b_out12.txt", "a")
savemat12.write(str(mat12))

#Mat 1 * Mat 3
print("\nMat 1 * Mat 3")
savemat13 = open("aander24_p2b_out13.txt", "a")
try:
    mat13 = np.matmul(mat1,mat3)
    print(mat13)
    savemat12.write(str(mat13))
except ValueError:
    print("Unable to multiply Mat 1 & Mat 3")
    savemat13.write("Unable to multiply Mat 1 & Mat 3")

#Mat 1 * Mat 4
print("\nMat 1 * Mat 4")
saveMat14=open("aander24_p2b_out14.txt", "a")
try:
    mat14 = np.matmul(mat1,mat4)
    print(mat14)
    saveMat14.write(str(mat14))
except ValueError:
    print("Unable to multiply Mat 1 & Mat 4")
    saveMat14.write("Unable to multiply Mat 1 & Mat 4")

#Mat 1 * Mat 5
print("\nMat 1 * Mat 5")
saveMat15=open("aander24_p2b_out15.txt", "a")
try:
    mat15=np.matmul(mat2,mat5)
    print(mat15)
    saveMat15.write(str(mat15))
except ValueError:
    print(ValueError)
    saveMat15.write("Unable to multiply Mat 1 & Mat 5")

#Mat 2 * Mat 1
print("\nMat 2 * Mat 1")
saveMat21=open("aander24_p2b_out21.txt", "a")
try:
    Mat21=np.matmul(mat2,mat1)
    print(Mat21)
    saveMat21.write(str(Mat21))
except ValueError:
    print("Unable to multiply Mat 2 & Mat 1")
    saveMat21.write("Unable to multiply Mat 2 & Mat 1")

#Mat 2 * Mat 3
print("\nMat 2 * Mat 3")
saveMat23=open("aander24_p2b_out23.txt", "a")
try:
    mat23 = np.matmul(mat2,mat3)
    print(mat23)
    saveMat23.write(str(mat23))
except ValueError:
    print("Unable to multiply Mat 2 & Mat 3")
    saveMat23.write("Unable to multiply Mat 2 & Mat 3")

#Mat 2 * Mat 4
print("\nMat 2 * Mat 4")
saveMat24=open("aander24_p2b_out24.txt", "a")
try:
    mat24=np.matmul(mat2,mat4)
    print(mat24)
    saveMat24.write(str(mat24))
except ValueError:
    print("Unable to multiply Mat 2 & Mat 4")
    saveMat24.write("Unable to multiply Mat 2 & Mat 4")

#Mat 2 * Mat 5
print("\nMat 2 * Mat 5")
saveMat25=open("aander24_p2b_out25.txt", "a")
try:
    mat25=np.matmul(mat2,mat5)
    print(mat25)
    saveMat25.write(str(mat25))
except ValueError:
    print("Unable to multiply mat2 & mat5")
    saveMat25.write("Unable to multiply Mat 2 & Mat 5")

#Mat 3 * Mat 1
print("\nMat 3 * Mat 1")
saveMat31=open("aander24_p2b_out31.txt", "a")
try:
    mat31=np.matmul(mat3,mat1)
    print(mat31)
    saveMat31.write(str(mat31))
except ValueError:
    print("Unable to multiply Mat 3 & Mat 1")
    saveMat31.write("Unable to multiply Mat 3 & Mat 1")

#Mat 3 * Mat 2
print("\nMat 3 * Mat 2")
saveMat32=open("aander24_p2b_out32.txt", "a")
try:
    mat32 = np.matmul(mat3,mat2)
    print(mat32)
    saveMat32.write(str(mat32))
except ValueError:
    print("Unable to multiply Mat 3 & Mat 2")
    saveMat32.write("Unable to multiply Mat 3 & Mat 2 ")

#Mat 3 * Mat 4
print("\nMat 3 * Mat 4")
saveMat34=open("aander24_p2b_out34.txt", "a")
try:
    mat34=np.matmul(mat3,mat4)
    print(mat34)
    saveMat34.write(str(mat34))
except ValueError:
    print("Unable to multiply Mat 3 & Mat 4")
    saveMat34.write("Unable to multiply Mat 3 & Mat 4")

#Mat 3 * Mat 5
print("\nMat 3 * Mat 5")
saveMat35=open("aander24_p2b_out35.txt", "a")
try:
    mat35=np.matmul(mat3,mat5)
    print(mat35)
    saveMat35.write(str(mat35))
except ValueError:
    print("Unable to multiply Mat 3 & Mat 5")
    saveMat35.write("Unable to multiply Mat 3 & Mat 5")

#Mat 4 * Mat 1
print("\nMat 4 * Mat 1")
saveMat41=open("aander24_p2b_out41.txt", "a")
try:
    mat41 = np.matmul(mat4,mat1)
    print(mat41)
    saveMat41.write(str(mat41))
except ValueError:
    print("Unable to multiply Matrix 4 & Matrix 1")
    saveMat41.write("Unable to multiply Mat 4 & Mat 1")

#Mat 4 * Mat 2
print("\nMat 4 * Mat 2")
saveMat42=open("aander24_p2b_out42.txt", "a")
try:
    mat42=np.matmul(mat4,mat2)
    print(mat42)
    saveMat42.write(str(mat42))
except ValueError:
    print("Unable to multiply Mat 4 & Mat 2 ")
    saveMat42.write("Unable to multiply Mat 4 & Mat 2")
#Mat 4 * Mat 3
print("\nMat 4 * Mat 3")
saveMat43=open("aander24_p2b_out43.txt", "a")
try:
    mat43=np.matmul(mat4,mat3)
    print(mat43)
    saveMat43.write(str(mat43))
except ValueError:
    print("Unable to multiply Mat 4 & Mat 3")
    saveMat43.write("Unable to multiply Mat 4 & Mat 3")

#Mat 4 * Mat 5
print("\nMat 4 * Mat 5")
saveMat45=open("aander24_p2b_out45.txt", "a")
try:
    mat45=np.matmul(mat4,mat5)
    print(mat45)
    saveMat45.write(str(mat45))
except ValueError:
    print("Unable to multiply Mat 4 & Mat 5")
    saveMat45.write("Unable to multiply Mat 4 & Mat 5")

#Mat 5 * Mat 1
print("\nMat 5 * Mat 1")
saveMat51=open("aander24_p2b_out51.txt", "a")
try:
    mat51=np.matmul(mat5,mat1)
    print(mat51)
    saveMat51.write(str(mat51))
except ValueError:
    print("unable to multiply Mat 5 & Mat 1")
    saveMat51.write("Unable to multiply Mat 5 & Mat 1")

#Mat 5 * Mat 2
print("\nMat 5 * Mat 2")
saveMat52=open("aander24_p2b_out52.txt", "a")
try:
    mat52=np.matmul(mat5,mat2)
    print(mat52)
    saveMat52.write(str(mat52))
except ValueError:
    print("Unable to multiply Mat 5 & Mat 2")
    saveMat52.write("Unable to multiply Mat 5 & Mat 2")

#Mat 5 * Mat 3
print("\nMat 5 * Mat 3")
saveMat53=open("aander24_p2b_out53.txt", "a")
try:
    mat53=np.matmul(mat5,mat3)
    print(mat53)
    saveMat53.write(str(mat53))
except ValueError:
    print("Unable to multiply Mat 5 & Mat 3")
    saveMat53.write("Unable to multiply Mat 5 & Mat 3")

#Mat 5 * Mat 4
print("\nMat 5 * Mat 4")
saveMat54=open("aander24_p2b_out54.txt", "a")
try:
    mat54=np.matmul(mat5,mat4)
    print(mat54)
    saveMat54.write(str(mat54))
except ValueError:
    print("Unable to multiply Mat 5 & Mat 4")
    saveMat54.write("Unable to multiply Mat 5 & Mat 4")




