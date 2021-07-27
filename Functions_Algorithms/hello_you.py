#!/usr/bin/env python3

import sys


def hello_name(first_name):
    """return first_name """
  
            
if __name__ == "__main__":
    #check number of arguments
    arg_count = len(sys.argv) - 1
    if arg_count == 1:
        first_name = sys.argv[1]
        print("Hello, {}!".format(first_name))  
    else:
        print("Hello, you!")
                                                                    



