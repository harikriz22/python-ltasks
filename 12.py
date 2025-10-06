import random 

# random.randint()


# print(random.randint(1,10))
# random.choice()
# fruits = ['apple','orange','banana','pineppale','grapes','waqtermelon']
# print(random.choice(fruits))

# coin toss \
# choice 
# randint 

# ch = ['heads','tails']

# print(random.choice(ch))

# z = random.randint(1,2)
# if z == 1:
#     print('heads')
# else:
#     print('tails')


# rock paper scissor game 






















import random

ch = ['rock','paper','scissor']
comp = random.choice(ch)
player = ''
while player not in ch:
    player = input('enter you choice\nrock/paper/scissor :-').lower()

print(f'computer\'s choice is {comp}')
print(f'player\'s choice is {player}')

if player == comp:
    print('its a tie!!!!!!!!!!!!!!!!')
elif player =='rock':
    if comp == 'paper':
        print(f'paper covers rock computer wins')
    else:
        print('rock beats scissor player wins')

elif player =='paper':
    if comp == 'scissor':
        print('scissor cuts paper computer wins')
    else:
        print('paper covers rock player wins')

elif player == 'scissor':
    if comp == 'rock':
        print('rock beats scuissor computer wins')
    else:
        print('swcissor cuts paper player wins')


