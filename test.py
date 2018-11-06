import ctypes

class UserArray(ctypes.Structure):
    _fields_ = [('n', ctypes.c_int),
                ('x', ctypes.c_double),
                ('f_value', ctypes.CFUNCTYPE(None, ctypes.c_double, ctypes.c_double))]

#    def __init__(self):
#        self.n = 0
#        self.x = 1
#
#    def __init__(n, x):
#        self.n = 0
#        self.x = 1

_test = ctypes.CDLL('/home/jdiffen1/diffen_math13/home/jdiffen1/ctypes-test/libtest.so')
_test.test.argtypes = [ctypes.POINTER(UserArray)]

def test(UserArray):
    global _test
    result = _test.test(UserArray)
    return int(result)
