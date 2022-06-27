'''Write a program that convert a list of temperatures in Celsius into Fahrenheit
using map() function.'''
a = [10, 20, 30, 40]
def celsius(f):
    fah = ((9)/5)*f + 32
    return fah
Farenheit = map(celsius,a)
print ("temperatures in fernheit:",list(Farenheit))