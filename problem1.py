"""Module for calculate the number of floating-point from an input file and their sum.
   According to https://docs.python.org/3/reference/lexical_analysis.html#floating, 
   floating point literals are described by the following lexical definitions:
   floatnumber   ::=  pointfloat | exponentfloat
   pointfloat    ::=  [intpart] fraction | intpart "."
   exponentfloat ::=  (intpart | pointfloat) exponent
   intpart       ::=  digit+
   fraction      ::=  "." digit+
   exponent      ::=  ("e" | "E") ["+" | "-"] digit+
"""

import sys
import math

#description:   function to print the help info of this program.	
#progname:      the name of the program.
def usage(progname):
    print(""" 
    This program is used to calculate the number of floating-point from an input file and their sum.
    And please use Python 3 to run this program.
    Usage:      %s [option] floatfile
    -h:         print this help message and exit (also --help)
    floatfile:  the path of the input file which contain floating-point numbers for calculation
    
    Run it like this:
                python %s <path-to-float-file>
    For help info:
                python %s -h or python %s --help
                
    Note:       the result of sum may loss of accuracy or precision in some extent due to
                the Python’s floating point precision, and may return nan.                
    """ % (progname, progname, progname, progname))

    
#description:   function to calculate the number of floating-point from an input file and their sum.	
#inputfile:     the input file that contains floating-point numbers for calculation.
#return:        a tuple (count, sum), count is the number of floating-point from the input file,
#               and sum is the summation of them
def procFloatsFromFile(inputfile):
    count = 0
    sum = 0.0
    with open(inputfile, 'r') as f:
        while True:
            line = f.readline()
            if line:
                l = line.split()
                for word in l:
                    try:
                        value = float(word)
                    except (ValueError, NameError, OverflowError):
                        #such invalid floating-point numbers will not be handled here, and just jump to the next number
                        continue
                    else:
                        if math.isinf(value) or math.isnan(value):
                            #if the floating-point numbers is INF or NaN, then just jump to the next number
                            continue
                        count += 1
                        sum += value
                        #Judgment of whether sum is nan or not may be removed in the future to improve performance
                        if math.isnan(sum):
                            #if current sum is nan, then no need to continue the calculation
                            print("procFloatsFromFile(): traversing for %s is stopped since current sum is nan(current count = %d)" % (inputfile, count))
                            return(count, sum)
            else:  
                break
    return (count, sum)    
	
    
if __name__ == '__main__':
    #the number of the command line parameters should be 2 for this program
    if len(sys.argv) != 2:
        usage(sys.argv[0])
    else:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            usage(sys.argv[0])
        else:
            (count, sum) = procFloatsFromFile(sys.argv[1])
            if not math.isnan(sum):
                print("A total of %s floating-point numbers are found in the given file %s, and their sum is %s." % (count, sys.argv[1], sum))
    sys.exit()