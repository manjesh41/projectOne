'''
5. A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.

'''
a = int(input("the number of student in class a:"))
b = int(input("the number of student in class b:"))
c = int(input("the number of student in class c:"))
deskt_in_class_one=a//2
print(deskt_in_class_one)
deskt_in_class_two=b//2
print(deskt_in_class_two)
deskt_in_class_three=c//2
print(deskt_in_class_three)

reminder_in_class_a=a%2
print(reminder_in_class_a)
reminder_in_class_b=b%2
print(reminder_in_class_b)
reminder_in_class_c=c%2
print(reminder_in_class_b)
