'''Write a program using reduce() function to calculate the sum of first 10 natural numbers '''
import functools
list = [1,2,3,4,5,6,7,8,9,10]
print("The sum of the list elements is :", end ="")
print(functools.reduce(lambda a, b: a+b,list))