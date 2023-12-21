import math
import numpy as np

        
def strassen_matrix_multiplication(a,b):   
    n = a.shape[0]
    if n == 1:
        return np.dot(a, b)
    
    row, col = a.shape
    x,y = row//2, col//2
    #assert len(Amatrix) == 2
    #assert len(Bmatrix) == 2
    #assert Amatrix[1] == Bmatrix[0]  
    

    #a matrice partition into 4 rows

    a11  = a[:x,:y]
    a12 =  a[:x, y:]
    a21 =  a[x:, :y]
    a22 =  a[x:, y:]
    
     
    brow, bcol = b.shape
    c,w = brow//2, bcol//2
    #b matrice partition into 4 columns
    b11 =  b[:c, :w]
    
    b12 =  b[:c, w:]
    b21 =  b[c:, :w]
    b22 =  b[c:, w:]

    
    C = np.zeros((a.shape[0], b.shape[0]), dtype=int)
    crow, ccol = C.shape
    g,p = crow//2, ccol//2
    c11 =  C[:g, :p]
    c12 =  C[:g, p:]
    c21 =  C[g:, :g]
    c22 =  C[g:, g:]
   
    
    # matrice product of a,b 
    p1 = strassen_matrix_multiplication(np.add(a11,a22),np.add(b11,b22))
    p2 = strassen_matrix_multiplication(np.add(a21,a22),b11) 
    p3 = strassen_matrix_multiplication(a11, np.subtract(b12,b22))
    p4 = strassen_matrix_multiplication(a22,np.subtract(b21,b11))
    p5 = strassen_matrix_multiplication(np.add(a11,a12),b22) 
    p6 = strassen_matrix_multiplication(np.subtract(a21,a11),np.add(b11,b12))
    p7 = strassen_matrix_multiplication(np.subtract(a12,a22), np.add(b21,b22))
    
   
     # blocks of c matrix

    c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5
    c21  = p2 + p4
    c22 = p1 - p2 + p3 + p6
    C = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22)))) 
    return C
    

A = np.array([
     [1,1,1,1],
     [2,2,2,2],
     [3,3,3,3],
     [2,2,2,2]
     ])
B = np.array(
    [
        [1,1,1,1],
        [2,2,2,2],
        [3,3,3,3],
        [2,2,2,2]
     ])


x = strassen_matrix_multiplication(A,B)
print(x)
