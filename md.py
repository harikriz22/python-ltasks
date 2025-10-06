
# # # # # number = int(input('enter num : - '))

# # # # # # print(len(str(number)))

# # # # # count = 0
# # # # # while number > 0 :
# # # # #     count += 1
# # # # #     number //= 10
# # # # # print(count)


# # # # # nested loop

# # # # # for i in range(1, 6):
# # # # #     for j in range(1, 6):
# # # # #         if i == 1 or i == 5 or j == 3:
# # # # #             print('*', end='')
# # # # #         else:
# # # # #             print('', end=' ')

# # # # #     print()


# # # # # for i in range(1,5):
# # # # #     print(i*'8')

# # # # # pattern
# # # # # palindrome
# # # # # fibanocci series
# # # # # prime or not


# # # # # obj

# # # # # class A:
# # # # #     def hello():
# # # # #         print('h1')
# # # # # class B(A):
# # # # #     def hello():
# # # # #         print('h2')


# # # # # b= B
# # # # # b.hello()
# # # # # pattern printing
# # # # # chessboard pattern

# # # # # WBWBWBWB
# # # # # BWBWBWBW
# # # # # WBWBWBWB
# # # # # BWBWBWBW
# # # # # WBWBWBWB
# # # # # BWBWBWBW
# # # # # WBWBWBWB
# # # # # BWBWBWBW


# # # # # for i in range(1,9):
# # # # #     for j in range(1,9):
# # # # #         if (i+j)%2 == 0 :
# # # # #             print('W',end=' ')
# # # # #         else:
# # # # #             print('B',end=' ')
# # # # #     print()

# # # # # try:

# # # # # except:


# # # # # create a rpg game using python


# # # # # role playing game


# # # # # player
# # # # # enemy

# # # # # playerhp  - 100
# # # # # enemyhp  - 100


# # # # # player x eneymy

# # # # # 100  - (1-20)
# # # # # enemy x player

# # # # import time, random
# # # # playerName=input('Enter the name of the player: ')
# # # # playerhp,enemyhp=100,100
# # # # while playerhp>0 or enemyhp>0:
# # # #     print('Player attacked enemy')
# # # #     time.sleep(2)
# # # #     playerhp=playerhp-random.randint(1,20)
# # # #     print('Playerhp:',playerhp)
# # # #     if playerhp<=0:
# # # #         print(playerName,'lost')
# # # #         break
# # # #     print('Enemy attacked',playerName)
# # # #     enemyhp=enemyhp-random.randint(1,20)
# # # #     print('Enemyhp:',enemyhp)
# # # #     if enemyhp<=0:
# # # #         print('Enemy lost')
# # # #         break

# # # # hp regain


# # # # snake and ladder

# # # import random
# # # player = input('enter players name:- ')
# # # enemy = random.choice(['dragon', 'goblin', 'troll'])
# # # playerhp, enemyhp = 100, 100
# # # turn = 1
# # # while playerhp > 0 and enemyhp > 0:

# # #     print(f'Turn {turn}')
# # #     print('player attack eneymy')
# # #     enemyhp = enemyhp - random.randint(1, 20)
# # #     print(f' enemy delth some damage remainaing enemy hp {enemyhp}')

# # #     print('ememy attacks player')
# # #     playerhp = playerhp - random.randint(1, 20)
# # #     print(f' player dealth some damage remainaing enemy hp {playerhp}')

# # #     if playerhp <= 0:
# # #         print('enemy won player is dead')
# # #         break
# # #     elif enemyhp <= 0:
# # #         print('player won enemy died')

# # #     turn = turn + 1


# # # dice game


# # # 2 player game


# # # player

# # #initially rolls a dice
# # # 1-6 -

# # 4

# # 4 x throw

# # 2
# # 3
# # 1
# # 1


# # score - 7


# # initial throw

# # 6

# # 6xthrow

# # 2
# # 2
# # 1
# # 1
# # 1
# # 1


# # score - 8


# # p2 eins


# p1

# p2


# # initial dice throw 1-6


# p1

# 3

# 3x

# 1
# 4
# 2


# 7

# # p2 - initial throw

# 5

# # 5 x throw

# 1
# 1
# 1
# 1
# 1

# 5


# p1 wins
# snake and ladder 
