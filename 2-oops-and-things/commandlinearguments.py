#running a python program
#<command> [-options] <programname.py> [<arguments>]

#command line arguments use to read values from user before hand
#all the values will be raw text(string)

#we can convert the argument(string) to appropriate type as well using
#a. implicit specification (where type is unknown)
#b. explicit specification (where type is known)

#implicit using eval() -> built in function to convert to appropriate type
#explicit using explicit type conversion -> int() float() ...

#command line arguments are stored in a special list object called 
#'argv'-> in sys module

#argv[0] is file name
#if giving str as cla then make sure to use '"your input"' as giving just 'your 
#input' will create error as it will start searching for variable from that name

import sys
for value in sys.argv[1:]:
    print(type(value))
  
for value in sys.argv[1:]:
    print(type(eval(value)))

