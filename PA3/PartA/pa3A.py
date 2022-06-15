# This program will read in a 2x2 matrix A & the column vector b. Afterwards, solving for the solution x
# which will be equal to b or zero vector
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

# ~~~~~~~~Try to find the solution for Ax=b, assuming that the matrix is non-singular and consistent
try:
    output_solution = np.linalg.solve(matrix.matrixA(),matrix.get_third_col_vector())
    print("\nThe solution for Ax=b is: ", output_solution)
    txt_output.write(str(output_solution))
    txt_output.write("\n")

# ~~~~~~~~~~ If the matrix is singular
except numpy.linalg.LinAlgError:
    output_solution = np.linalg.lstsq(matrix.matrixA().T,matrix.get_third_col_vector(), rcond=None)[0]

    if output_solution[0] == 0 and output_solution[1] == 0:
        print("\nThe Solution for Ax=b is UNDER-DETERMINED")
        txt_output.write("\nSystem Under-Determined")
    else:
        print("\nThe Solution for Ax=b is INCONSISTENT")
        txt_output.write("\nSYSTEM INCONSISTENT")

# Choose arbitrary value for x2, to solve for Ax = 0
x2 = int(2)
x1 = symbols('x1')
expr = (matrix.n21 * x1) + (matrix.n22 * x2)
x1_sol = solve(expr)

if (x1_sol[0] * matrix.n11 ) + (matrix.n12 * x2) != 0:
    print("Ax=0: Only trivial solutions exist")
    txt_output.write("\nOnly trivial solutions exist")
else:
    solution = [x1_sol[0], x2]
    print("Ax=0: ", solution)
    txt_output.write("\n")
    txt_output.writelines(str(solution))



