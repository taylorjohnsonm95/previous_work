#!/usr/bin/env python3.6

#create a function to multiply two numbers 
def multiply(a, b):
	""" This function will multiply a and b """
	x = a * b
	return x










#create a function to print "Hello, {name}!"
def hello_name(first_name = 'you'):
    """ print "Hello, {first_name}!" """
    hello = ("Hello, {}!".format(first_name))
    #print(hello)
    return hello








#create a function to print a list of numbers that are less than 10
def less_than_ten(numbers):
    """ takes a list of numbers and returns only numbers less than 10"""
    list = []
    for number in numbers:
        if number < 10:
            list.append(number)
    return list


