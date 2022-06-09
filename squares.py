#here ive imported a function from functions file
'''from functions import square
for i in range(10):
    print(f"Square of {i} is {square(i)}.")'''
'''here ive imported complete functions file,
so need to mention functions.square'''
import functions
for i in range(10):
    print(f"Square of {i} is {functions.square(i)}.")