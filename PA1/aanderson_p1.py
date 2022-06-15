import numpy as np

firstName = "Aleksandra"
lastName = "Anderson"

#Matrix 1: columns first, then over rows second

mat1 = np.zeros(shape=(len(firstName),len(lastName)))
counter=0

for row in mat1:
    for i,col in enumerate(row):
        row[i]=counter
        counter+=1

matrix1=np.matrix(mat1)
with open('aanderson_p1_mat1.txt', "wb") as f:
    for line in matrix1:
        np.savetxt(f, line, fmt='%.2f')

print(matrix1)
print()

#Matrix 2: rows first, then over columns second
counter2 = 2
mat2=np.zeros(shape=(len(lastName),len(firstName)))

for rows in mat2.T:
    for i,cols in enumerate(rows):
        rows[i]=counter2
        counter2+=3

matrix2=np.matrix(mat2)
with open('aanderson_p1_mat2.txt', "wb") as f:
    for line in matrix2:
        np.savetxt(f, line, fmt='%.2f')

print(matrix2)
print()


#Matrix 3: rows first, then over columns second
counter3=.6
mat3=np.zeros(shape=(len(lastName),len(firstName)))

for rows in mat3.T:
    for i,cols in enumerate(rows):
        rows[i]=counter3
        counter3+=.2

matrix3=np.matrix(mat3)
with open('aanderson_p1_mat3.txt', "wb") as f:
    for line in matrix3:
        np.savetxt(f, line, fmt='%.2f')

print(matrix3)
print()

#Matrix 4: rows first, then over columns second
counter4=3
mat4=np.zeros(shape=(5,9))
for rows in mat4.T:
    for i,cols in enumerate(rows):
        rows[i]=counter4
        counter4+=2

matrix4=np.matrix(mat4)
with open('aanderson_p1_mat4.txt', "wb") as f:
    for line in matrix4:
        np.savetxt(f, line, fmt='%.2f')

print(matrix4)
print()

# Matrix 5: columns first, then over rows second
counter5=-7
mat5=np.zeros(shape=(5,9))

for rows in mat5:
    for i, cols in enumerate(rows):
        rows[i]=counter5
        counter5+=1

matrix5=np.matrix(mat5)
with open('aanderson_p1_mat5.txt', "wb") as f:
    for line in matrix5:
        np.savetxt(f, line, fmt='%.2f')

print(mat5)





