# [SIG Python Task 1] 

"""
Tasks to performs: 
a) Print 'Hello, World! From SIG Python - <your name>' to the screen
b) Calculate Volume of a Sphere
c) Create a customised email template for all students, 
   informing them about a workshop.

PS: This is called a docstring... and it will not be interepreted
    So leave these instructions here.. no problems.
    The first line having '#' is called a comment. It will be ignored too.
    You can write your own comments and docstrings to make your code clear
    and documented.
"""


# a) Print 'Hello, World! From SIG Python - <your name>' to the screen
# Write you code here
print("hello, World! From SIG Python - Gaurangi Rawat")

# b) Calculate Volume of a Sphere
# Take the radius as input from the user and use the math module
r=int(input('enter radius of the sphere'))
volume=4/3*3.14*r*r*r
print("volume=",volume,)


#c) Create a customised email template for all students, informing them about a workshop that the student applied for earlier.
# Task the student's name, workshop, Time, Date, writer's name, organization's name as input from the program's user 
student_name=input('enter student name:')
workshop=input('workshop:')
Time=input('time:')
Date=input('date:')
writer_name=input("writer's name:")
organization_name=input('organization name:')


# Use the given string as your template [This is a multi-line string]
email_msg = f"""Dear {student_name},
We have received your request to register for the Workshop event and the 
workshop you applied for {workshop} has been scheduled at {Time} on {Date }.
We will be seeing you there! Thanks for participating.
Regards,
{writer_name}
{organization_name}"""
# Format using .format or f-strings


print(email_msg)


# NOTE: Make sure to print few empty lines after each task
