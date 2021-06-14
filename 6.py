'''
Solve each of the following problems using Python Scripts. Make sure you use appropriate variable names and comments.
 there is a final answer have Python print it to the screen.
A person’s body mass index (BMI) is defined as:
BMI=mass in kg / (height in m)2.
'''
#getting input from question
height=float(input('ENTER height in meter:'))
mass=float(input('enter mass in kg:'))
#formula for BIM
BMI=mass  / (height**2)
print(f"the value of BIM is{BMI}")
#using conditional statement
if (BMI<20):
    print("python")
else:
    print("PYTHON")
