'''Write a program to create a new list containing the first letters of every
element in an already existing list.'''
s= input("Enter the comma sepearted values:") 
x=s.split(",") 
print("Original list:",x) 
l=[i[0] for i in x] 
print("Modified list:",l)