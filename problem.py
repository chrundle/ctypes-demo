from test import UserArray 
import test
import ctypes 

def py_f_value(a,b):
    print("a = ", a)
    print("b = ", b)
    a = a - b
    b = 0
    print("a = ", a)
    print("b = ", b)

F_VALUE = ctypes.CFUNCTYPE(None, ctypes.c_double, ctypes.c_double)
f_value = F_VALUE(py_f_value)

A = UserArray()
A.n = 0
A.x = 3.2 
A.f_value = f_value 

print(test.test(A))
