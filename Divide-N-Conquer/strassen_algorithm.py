import math
import numpy as np

    
    
     
def strassen_matrix_multiplication(a,b): 
    n = len(a)
    if n <= 1:
        return a * b
       
    
    Amatrix = np.array(a)
    row,col = Amatrix.shape
    x,y = row//2, col//2     
     
    Bmatrix = np.array(b)  
    rows,cols = Bmatrix.shape
    r,w = rows//2, cols//2  
    
    R = [[0 for i in range(row)]for j in range(col)]
    C = np.array(R)
    

    #a matrice partition into 4 
    a11 =  Amatrix [:x, :y]
    a12 =  Amatrix [:x,y:]
    a21 =  Amatrix [x:, :y]
    a22 =  Amatrix [x:, y:]
   
    #b matrice partition into 4
    b11 =  Bmatrix[:r, :w]
    b12 =  Bmatrix[:r,w:]
    b21 =  Bmatrix[r:, :w]
    b22 =  Bmatrix[r:, w:]

    #10 submatrices created
    s1 = np.subtract(b12, b22)
    s2 = np.add(a11,a12)
    s3 = np.add(a21,a22)
    s4 = np.subtract(b21, b11)
    s5 = np.add(a11,a22)
    s6 = np.add(b11,b22)
    s7 = np.subtract(a12,a22)
    s8 = np.add(b21,b22)
    s9 = np.subtract(a11,a21)
    s10 = np.add(b11,b12)

    
    # matrice product of a,b 
    p1 = strassen_matrix_multiplication(a11,s1)
    p2 = strassen_matrix_multiplication(s2,b22) 
    p3 = strassen_matrix_multiplication(s3, b11)
    p4 = strassen_matrix_multiplication(a22,s4)
    p5 = strassen_matrix_multiplication(s5,s6) 
    p6 = strassen_matrix_multiplication(s7,s8)
    p7 = strassen_matrix_multiplication(s9, s10)
    
     
    c11 = np.subtract((np.add(p5, p4)), (np.add(p2, p6)))
    c12 = np.add(p1, p2)
    c21 = np.add(p3,p4)
    c22 = np.subtract(np.add(p5,p1 ), np.subtract(p3,p7))

  
    C[:x, :y] = c11 
    C[:x, y:] = c12
    C[x:,:y] = c21
    C[x:,y:] = c22
 
    return C
    

A = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3],
     [2,2,2,2]
     ]
B = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3],
     [2,2,2,2]
     ]

X = np.array(A)
Y = np.array(B)

x = strassen_matrix_multiplication(X,Y)
print(x)

