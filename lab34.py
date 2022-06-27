'''Write a program that creates an iterator to print squares of numbers.'''
class Sq:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 0#initial value
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n**2
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = Sq(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))