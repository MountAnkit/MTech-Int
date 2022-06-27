'''Write a program to create a generator to print the Fibonacci number.'''
def Fib(rows):
     a = 0
     b = 1
     sum = 0
     counter = 1
     print(a)
     while counter <= rows-1:
         yield b
         sum = a+b
         a = b
         b = sum
         counter += 1

Fibnocci = Fib(5)
print(next(Fibnocci))
print(next(Fibnocci))
print(next(Fibnocci))
print(next(Fibnocci))