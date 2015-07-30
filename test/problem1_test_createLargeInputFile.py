"""Module for creating large input file."""

import sys
import os

#the floating-point numbers that will be written into the large input file
g_dim = (10000000, "1.0\n")


#description:   function to print the help info of this program.	
#progname:      the name of the program.
def usage(progname):
    print(""" 
    This program is used to create a large input file for testing problem1.py.
    And please use Python 3 to run this program.

    Usage:      %s [option] largefile
    -h:         print this help message and exit (also --help)
    largefile:  the path of the large file which contain floating-point numbers for testing problem1.py,
                if this largefile already exists, then the old one will be delete before starting,
                so use it carefully in such cases.

    Run it like this:
                python %s <path-to-large-file>
    For help info:
                python %s -h or python %s --help
                
    Note:       the functionalities of this program will be enhanced in the future for various test requirements                
    """ % (progname, progname, progname, progname))


#description:   function to create a large input file for testing problem1.py.	
#largefile:     the output file that contains a huge number of floating-point numbers for testing.
#               if this largefile already exists, then the old one will be delete before starting,
#               so use it carefully in such cases!
def createLargeInputFile(largefile):
    count = 0
    if os.path.exists(largefile):
        print("%s exists, and will delete it firstly!" % (largefile))
        #the existing largefile will be removed firstly
        os.remove(largefile)
    with open(largefile, 'a') as f:
        while count < g_dim[0]:
            f.write(g_dim[1])
            count += 1
        if (count == g_dim[0]):
            print("Successfully create %s with %s lines, and each line contain a float number %s!" % (largefile, g_dim[0], g_dim[1]))
        else:
            print("Fail to create %s as expected, currently it has %s lines, and each line contain a float number %s!" % (largefile, g_dim[0], g_dim[1]))
	
    
if __name__ == '__main__':
    #the number of the command line parameters should be 2 for this program
    if len(sys.argv) != 2:
        usage(sys.argv[0])
    else:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            usage(sys.argv[0])
        else:
            if sys.argv[1].startswith('-'):
                print("Failed to create the large file: the given path or name of it cannot begin with '-'")
            else:            
                createLargeInputFile(sys.argv[1])
    sys.exit()