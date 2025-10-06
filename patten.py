# # # nested loop 


# # # for i in range(1,6):
# # #     for j in range(1,6):     
# # #             print(i,j)

# # # *
# # # **
# # # ***
# # # ****
# # # *****



# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print('*',end='')
# #     print()
        
   

    
# # #    *
# # #   * *
# # #  * * *
# # # * * * *
# # #* * * * *


# # # for i in range(1,6):
# # #     for k in range(0,6-i):#   
# # #         print(' ',end='')
# # #     for j in range(1,i+1):
# # #         print('* ',end='')
# # #     print()


# # # chessboard pattern 



# # # for i in range(1,10):
# # #     print(i,end='')

# # # WBWBWBWBWB
# # # BWBWBWBWBW
# # # WBWBWBWBWB
# # # BWBWBWBWBW
# # # WBWBWBWBWB
# # # BWBWBWBWBW
# # # WBWBWBWBWB
# # # BWBWBWBWBW




# # for i in range(1,9):
# #     for j in range(1,9):
# #         if (i+j)%2 == 0:
# #             print('W ',end='')
# #         else:
# #             print('B ',end='')
# #     print()


# # # *****
# # #  ****
# # #   ***
# # #    **
# # #     *


# # # string indexing 



# # a = 'hari'
# #     #  0123

# # # string a of index 2 
# # print(a[2])



# # name = 'mohan'
# # # [start,stop,step]
# # print(name[::-1])


# # string 
# # list 


# # tuple
# # dict 


# # itrables 
# # index based 
# # name = 'mohandasxaedfsdavruwo'

# # for i in name:
# #     print(i)
# # for i in range(0,len(name)):
# #     print(i,name[i])

# # find the vowels and their position from a string 

# # hari 

# # a at position 1
# # i at position 3

# # print(len(name))


# # data = input('eneter your data: - ')
# # for i in range(len(data)):        
# #     if data[i] in 'aeiou':
# #         print(f'{data[i]} at position {i}')

# # reverse of a string without using [::-1]
# # n word input 

# a = 'hari'
# z = ''
# for i in range(len(a)-1,-1,-1):
#     z = z + a[i]

# # print(z)


# # 5

# # enter hello
# # how
# # are
# # you
# # python 

# # hello how are you python 

# #     a
# #    a p
# #   a p p 
# #  a p p l 
# # a p p l e