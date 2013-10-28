__author__ = 'SunnyYan'
#
# Write an algorithm such that if an element in an M*N matrix is 0,
# set the entire row and column to 0
#

def setMatrixtoZero(matrix):
    rowlen = len(matrix)
    columnlen = len(matrix[0])
    row = [0]*rowlen
    column = [0]*columnlen
    for i in range(0, rowlen):
        for j in range(0, columnlen):
            if matrix[i][j] == 0:
                row[i] = 1
                column[j] = 1


    for i in range(0, rowlen):
        for j in range(0, columnlen):
            if row[i] or column[j]:
                matrix[i][j] = 0
    return matrix

matrixrow = []
matrixcol = []

# initialized the matrix by using list

for row in range(0, 3):
    for column in range(0, 4):
        matrixcol.append(column+row)
    matrixrow.append(matrixcol)
    matrixcol=[]

print "Before setting"
print matrixrow
print "After setting"
print setMatrixtoZero(matrixrow)
