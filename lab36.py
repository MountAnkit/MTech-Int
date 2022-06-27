'''Write a program to create a generator that starts counting from 0 and raise an
exception when counter is equal to 10.'''

def numberGenerator(n):
     counter = 0
     while counter < n:
         yield counter
         counter += 1

myGenerator = numberGenerator(10)

print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))