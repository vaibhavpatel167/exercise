"""Complete the Exercises - Representing Abstraction Through Code 
In programming, we deal with two kinds of elements: functions and data. 

Informally, data is stuff that we want to manipulate, and functions describe the rules for manipulating the data. 

By the concept of abstraction create functions representing abstracting principles through function 

Think and design a user-defined function that should provide the result by mare passing few arguments by the calling function."""
def calculate_circle_properties(radius):
    circumference = 2 * 3.14159 * radius
    area = 3.14159 * radius ** 2
    diameter = 2 * radius
    return (circumference, area, diameter)

# example usage
result = calculate_circle_properties(5)
print(result)