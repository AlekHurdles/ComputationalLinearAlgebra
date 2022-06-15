import math
import numpy as np
import numpy.linalg
from sympy import symbols, solve

class Matrix:

    # first column vector
    def set_first_col_vector1(self, v1):
        self.n11 = v1

    def set_first_col_vector2(self,v2):
        self.n21 = v2

    def get_first_col_vector(self):
        vlist= [self.n11, self.n21]
        return vlist

    # second column vector
    def set_second_col_vector1(self,v1):
        self.n12 = v1

    def set_second_col_vector2(self,v2):
        self.n22 = v2

    def get_second_col_vector(self):
        vlist = [self.n12, self.n22]
        return vlist

    # third column vector
    def set_third_col_vector1(self, v1):
        self.n13 = v1

    def set_third_col_vector2(self,v2):
        self.n23 = v2

    def get_third_col_vector(self):
        vlist = np.array([int(self.n13),int(self.n23)])
        return vlist

    def get_determinant(self):
        determinant = (self.n11*self.n22) - (self.n12*self.n21)
        return determinant

    def matrixA(self):
        matrix_a = np.array([[int(self.n11),int(self.n12)],[int(self.n21),int(self.n22)]])
        return matrix_a

# ~~~~~~~~~~ Read in file ~~~~~~~~~~
file = input("Enter the name of the .txt file to read from (ex: input_files/pa2_input_1.txt): ")
outputFile = input("Please enter the name of the output file to write to: (ex: output_files/pa2_output_2.txt) ")
txt_output = open(outputFile, 'w')

matrix = Matrix()

with open(file, 'r') as f:
    first_row = f.readline().split(" ")
    second_row = f.readline().split(" ")

    matrix.set_first_col_vector1(float(first_row[0]))
    matrix.set_second_col_vector1(float(first_row[1]))
    matrix.set_third_col_vector1(float(first_row[2]))

    matrix.set_first_col_vector2(float(second_row[0]))
    matrix.set_second_col_vector2(float(second_row[1]))
    matrix.set_third_col_vector2(float(second_row[2]))

# Solve for Eigen Values
eig = symbols("eig")
quadratic_equation = eig**2 - (matrix.n11*eig) - (matrix.n22 * eig) + (matrix.n11*matrix.n22) - (matrix.n12*matrix.n21)

eig_values = solve(quadratic_equation)

eig1 = 0
eig2 = 0
if abs(eig_values[0]) > abs(eig_values[1]):
    eig1 = eig_values[0]
    eig2 = eig_values[1]
elif abs(eig_values[0]) < abs(eig_values[1]):
    eig1 = eig_values[1]
    eig2 = eig_values[0]
elif abs(eig_values[0]) == abs(eig_values[1]):
    eig1 = eig_values[0]
    eig2 = eig_values[0]

eigen_matrix = np.array([[eig1,0],[0,eig2]])
# print("\nThe eigen matrix is:\n",eigen_matrix)


# ~~~~~~ Solve for R=[r1 r2] ~~~~~~~~
r1_homogeneous_matrix_11 = matrix.n11 - eig1
r1_homogeneous_matrix_22 = matrix.n22 - eig1

# Shear matrix for forward elimination
s11 = 1
s12 = 0
s_21_d1 = symbols('d')
s_21_d2 = symbols('d2')
s22 = 1

solve_for_d1 = solve((s_21_d1 * r1_homogeneous_matrix_11) + (s22 * matrix.n21))[0]
#print("\nd=",solve_for_d1)

shear_output_11 = 0
shear_output_21 = 0
shear_output_12 = 0
shear_output_22 = 0

try:

    shear_output_11 = float((s11 * r1_homogeneous_matrix_11) + (s12 * matrix.n21))
    shear_output_21 = (float(solve_for_d1) * r1_homogeneous_matrix_11) + (s22 * matrix.n21)
    shear_output_12 = float((s11 * matrix.n12) + (s12 * matrix.n22))
    shear_output_22 = (float(solve_for_d1) * matrix.n12) + (s22 * r1_homogeneous_matrix_22)
    txt_output.writelines(str(eigen_matrix))
except TypeError:
    print("No real Eigen Values")
    txt_output.write("\nNo Real Eigen Values")
    quit()

shear_output_matrix = np.array([[shear_output_11,shear_output_12],[shear_output_21,shear_output_22]])
print("Shearing the r1 matrix produces: \n",shear_output_matrix)

# ~~~~ Solve for r1 ~~~~~
r11 = symbols('r1')
r21 = symbols('r2')

if shear_output_21 == 0 and shear_output_22 == 0:
    r21 = float( float(shear_output_11) / float(shear_output_12))

else: # Check on this with a different example !!!
    r21 = solve( float(shear_output_22) * r21)[0]

r11 = solve((r21 * float(shear_output_12)) + (r11 * float(shear_output_11)))[0]
print(r11, r21)

# Find normal to normalize vector 1 / ||r||

normalize_vector = r21**2 + r11**2
normalize = math.sqrt(normalize_vector)

if normalize != 0:
    r11 = float(1/normalize) * r11
    r21 = float(1/normalize) * r21

r1 = np.array([[r11,r21]])

# print("r1=", r1)

# ~~~~~~~ solve for r2 ~~~~~~~
r2_homogeneous_matrix_11 = matrix.n11 - eig2
r2_homogeneous_matrix_22 = matrix.n22 - eig2

solve_for_d2 = solve((s_21_d2 * r2_homogeneous_matrix_11) + (s22 * matrix.n21))[0]
# print("\nd2=", solve_for_d2[0])

r2shear_output_11 = (s11 * r2_homogeneous_matrix_11) + (s12 * matrix.n21)
r2shear_output_21 = (float(solve_for_d2) * r2_homogeneous_matrix_11) + (s22 * matrix.n21)
r2shear_output_12 = (s11 * matrix.n12) + (s12 * matrix.n22)
r2shear_output_22 = (float(solve_for_d2) * matrix.n12) + (s22 * r2_homogeneous_matrix_22)

r2shear_output_matrix = np.array([[r2shear_output_11,r2shear_output_12],[r2shear_output_21,r2shear_output_22]])
# print("Shearing the r2 matrix produces: \n",r2shear_output_matrix)

r12 = symbols('r1')
r22 = symbols('r2')

if r2shear_output_21 == 0 and r2shear_output_22 == 0:
    r22 = r2shear_output_11 / r2shear_output_12

else: # Check on this with a different example !!!
    r22 = solve(r2shear_output_22 * r22)[0]

r12 = solve((r22 * r2shear_output_12) + (r12 * r2shear_output_11))[0]

# Find normal to normalize vector 1 / ||r||
normalize_vector = r22**2 + r12**2
normalize = math.sqrt(normalize_vector)

if normalize != 0:
    r12 = float(1/normalize) * r12
    r22 = float(1/normalize) * r22

r2 = np.array([[r12 , r22]])
# print("r2=", r2)

r_matrix = np.array([[float("{0:.4g}".format(r11)),float("{0:.4g}".format(r12))],[float("{0:.4g}".format(r21)),float("{0:.4g}".format(r22))]])
print("\nR matrix =\n",r_matrix)
txt_output.write("\n")
txt_output.writelines(str(r_matrix))

r_transpose = r_matrix.T
# print("\nR Transpose Matrix =\n", r_transpose)

# Multiply the 3 Matrix: R * Eigen * R_transpose
first_step_multiplication = np.matmul(eigen_matrix,r_transpose)
matrix_composition = np.matmul(r_matrix,first_step_multiplication)
print("\nMatrix Composition = \n", matrix_composition)
txt_output.write("\n")
txt_output.writelines(str(matrix_composition))

# Compare Matrix A with Matrix Composition
comparison = matrix.matrixA() == matrix_composition
equal_matrix = comparison.all()
identitcal_boolean = 0

if equal_matrix == False:
    identitcal_boolean = 0
else:
    identitcal_boolean = 1

print(identitcal_boolean)
txt_output.write("\n")
txt_output.write(str(identitcal_boolean))
