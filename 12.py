'''
 If temperature is greater than 30, it's a hot day other wise if it's less than 10;
 it's a cold day; otherwise, it's neither hot nor cold.
'''
temprature=int(input('the temprature is:'))
if temprature>30 :
    print(f"it's a hot day")
elif temprature<10:
    print(f"it's is a cold day")

else:
    print(f"it's neither hot nor cold")