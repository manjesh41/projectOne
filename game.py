'''
game finding a secret number within 3 attempts using while loop
'''
secrate_number=4
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input('guess'))
    guess_count+=1
    if guess==secrate_number:
        print('you won!')
    else:
        print('you lose!')