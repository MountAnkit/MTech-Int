'''Write a program that create a custom iterator to create even numbers.'''
class Even:
    def __iter__(self):
        self.num = 0
        return self
    def __next__(self):
        next_num = self.num
        self.num += 2
        return next_num
evens = Even()
even_iter = iter(evens)
print(next(even_iter))
print(next(even_iter))
print(next(even_iter))
print(next(even_iter))
print(next(even_iter))
print(next(even_iter))