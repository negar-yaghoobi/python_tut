from Mypackage.module1 import some_function      # (1)
from Mypackage import module1                    # (2)
from Mypackage.subpackage.mysub import aaa,bbb       # (3)

def func1():
    print('function1')

def func2():
    print('function2')

some_function()                                  # (1)

module1.some_function()                          # (2)

aaa()                                            # (3)
bbb()