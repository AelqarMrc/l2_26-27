from numpy import array, arange, eye, dot, ndarray
from numpy.random import rand
from numpy.linalg import det,inv
from typing import List

if __name__ == "__main__":
    
    myList : List[int]   = list(range(5))

    print(myList+myList)

    # myArray : ndarray = array(range(5))
    # myArray : ndarray = arange(5)

    # print(myArray+myArray)

    # myArray : ndarray = arange(1,10,0.5)
    # print(myArray)
    # print(myArray%2)

    # print("\neye(3)\n",eye(3))
    # print()
    # print("\nrand(3,3)\n",rand(3,3))
    # print() 
    # print("\ndet(eye(10))\n",eye(10),"\n",det(eye(10)))

    # A : ndarray= array([[1,2,3],
    #            [4,5,6],
    #            [7,8,10]])
    # print("A\n",A)
    # print("\nA+A\n",A+A)
    # print("\nA*A\n",A*A)
    # print("\ndot(A,A)\n",dot(A,A))
    # print("\nA*inv(A)\n",A*inv(A))
    # print("\ndot(A,inv(A))\n", dot(A,inv(A)))