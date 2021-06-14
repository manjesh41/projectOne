'''You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10
stops on the way. How long will the bus journey take?
Alternatively, you could run to university.
You jog the first mile at 7mph; then run the next two at15mph;before jogging the last at 7mph again.
 Will this be quicker or slower than the bus?
'''
lives_apart=4
drives_velocity=25
time_taken=(lives_apart/drives_velocity)*60

total_spend=20
total_time=time_taken+total_spend
print(f'time taken by bus is{total_time}')

jog_one=(1/7)*60
jog_two=()