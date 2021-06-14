'''
Write a Python program to convert seconds to day, hour, minutes and seconds.
'''
hour=int(input('enter hour:'))
minute=int(input('enter minute:'))
second=int(input('enter second:'))
day_in_second=hour*minute*second
print(f"In one day there is {day_in_second} second")