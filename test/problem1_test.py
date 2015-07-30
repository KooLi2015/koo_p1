"""Program for testing problem1.py """

import sys
import os
import time

sys.path.append(os.path.abspath('..'))
from problem1 import procFloatsFromFile

ExpectedResult = [(13, 54428.147600000004), (11, -7581.798728999999), (2, float('inf')), (10000000, 10000000.0)]


#description:    function to do the preparation work before testing.
#note:           i.e., rebuild problem1_testxxx.dat file
def prepare_test():
    pass      


#description:    function to do the 1st test against problem1.py.
#                all the floating-point numbers in the input file follow the floating-point lexical definitions in Python 3
#note:           use problem1_test1.dat as the input file
def test1():
    start = time.clock()
    #run the test
    (count, sum) = procFloatsFromFile("problem1_test1.dat")
    end = time.clock() 
    print("Finish Test1!   It costs %f seconds process time." % (end - start))
    try:
        assert (count, sum) == ExpectedResult[0]
    except AssertionError:
        print("Test1 Failed!   (count = %s, sum = %s) != expected %s" % (count, sum, ExpectedResult[0])) 
    else:
        print("Test1 Pass!")
    

#description:    function to do the 2nd test against problem1.py.
#                not all the floating-point numbers in the input file follow the floating-point lexical definitions in Python 3,
#                it consists of special or invalid floating-point like INF, NaN, or result in overflow, and so on 
#note:           use problem1_test2.dat as the input file
def test2():
    start = time.clock()
    #run the test
    (count, sum) = procFloatsFromFile("problem1_test2.dat")
    end = time.clock() 
    print("Finish Test2!   It costs %f seconds process time." % (end - start))
    try:
        assert (count, sum) == ExpectedResult[1]
    except AssertionError:
        print("Test2 Failed!   (count = %s, sum = %s) != expected %s" % (count, sum, ExpectedResult[1])) 
    else:
        print("Test2 Pass!")


#description:    function to do the 3rd test against problem1.py.
#                it is designed for a boundary test against sys.float_info.max and inf,
#note:           use problem1_test3.dat as the default input file, and please note that the test data in problem1_test3.dat
#                maybe need to be changed according to value of sys.float_info.max on your test machine!
def test3():
    start = time.clock()
    #run the test
    (count, sum) = procFloatsFromFile("problem1_test3.dat")
    end = time.clock() 
    print("Finish Test3!   It costs %f seconds process time." % (end - start))
    try:
        assert (count, sum) == ExpectedResult[2]
    except AssertionError:
        print("Test3 Failed!   (count = %s, sum = %s) != expected %s" % (count, sum, ExpectedResult[2])) 
    else:
        print("Test3 Pass!")
        
        
#description:    function to do the 4th test against problem1.py.
#                it is designed for testing the robustness and performance of problem1.py when using a large file as the input  
#note:           problem1_test4.dat is used as the default input file
def test4():
    start = time.clock()
    #run the test
    (count, sum) = procFloatsFromFile("problem1_test4.dat")
    end = time.clock() 
    print("Finish Test4!   It costs %f seconds process time." % (end - start))
    try:
        assert (count, sum) == ExpectedResult[3]
    except AssertionError:
        print("Test4 Failed!   (count = %s, sum = %s) != expected %s" % (count, sum, ExpectedResult[3])) 
    else:
        print("Test4 Pass!")
    

#description:    function to test problem1.
def problem1_test():
    test1()
    test2()
    test3()
    test4()    
	
    
if __name__ == '__main__':
    prepare_test()
    problem1_test()
    sys.exit()