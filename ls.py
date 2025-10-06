

# # # # # # # # list

# # # # # # # # lists are collections of data []

# # # # # # # # a = [11,12,13,14]

# # # # # # # # c = [56,3,2,3,4,6,7,9,6.6,True,'hari',[4,5,6,7,]]


# # # # # # # # properties

# # # # # # # # list ordered

# # # # # # # # a = [1,2,3,4]
# # # # # # # # b = [3,1,2,4]

# # # # # # # # print(a==b)

# # # # # # # # a = [1,1.2,True,'hari',[11,12,13]]
# # # # # # # # string   immutable
# # # # # # # # list

# # # # # # # # mutable
# # # # # # # # list dynamic

# # # # # # # # name = 'hari' #immutable
# # # # # # # # name = 'lari'

# # # # # # # # name[0] = 'l'
# # # # # # # # print(name)

# # # # # # # # a = [11,12,13,14,15] #mutable

# # # # # # # # a[0] = 'hari'
# # # # # # # # print(a)

# # # # # # # #dynamic

# # # # # # # # b =[22,23,24,25,272,28,29]
# # # # # # # # b [2::] = [2,3]
# # # # # # # # print(b)


# # # # # # # # list can be nested
# # # # # # # # b = [11,12,[100,['mohan',['m','o','h'],'das'],300],14,15]
# # # # # # # # print(b[2][1][1][2])

# # # # # # # # list can be indexed
# # # # # # # # z = [11,121,131,14,151,17,181,191,'hs']
# # # # # # # # c = z[4:7]
# # # # # # # # print(type(c))


# # # # # # # # print(c[1])


# # # # # # # # inbult methods in a list

# # # # # # # # add

# # # # # # # # append
# # # # # # # # extend
# # # # # # # # insert

# # # # # # # # 1.append(value)
# # # # # # # # a = [11,12,13]
# # # # # # # # a.append('hari')
# # # # # # # # a.append(18)

# # # # # # # # print(a)

# # # # # # # # 2.extend(itreable)

# # # # # # # # a = [11,12,13]
# # # # # # # # a.extend(['hari','mohan'])
# # # # # # # # print(a)


# # # # # # # # 1.insert(index,value)

# # # # # # # # a = [1,2,3,4]
# # # # # # # # a.insert(0,'hari')
# # # # # # # # print(a)

# # # # # # # # remove

# # # # # # # # a= [5,1,2,5,3,4,5]
# # # # # # # # a.pop(0)
# # # # # # # # a.pop(0)

# # # # # # # # print(a)
# # # # # # # # remove(value)
# # # # # # # # a.remove(5)
# # # # # # # # print(a)

# # # # # # # # pop


# # # # # # # # list operation


# # # # # # # # a = ['a','b']
# # # # # # # # b = ['c','d']
# # # # # # # # print(a*5)

# # # # # # # # print(5 in [1,2,3,4,5])

# # # # # # # # a = 'haripython'[::-1]

# # # # # # # # print(a)


# # # # # # # # itreate a list  index


# # # # # # # # direct
# # # # # # # # index based


# # # # # # # # a = [11,12,13,14,15,26]

# # # # # # # # # for i in a:
# # # # # # # # #     print(i)

# # # # # # # # for i in range(len(a)):
# # # # # # # #     print(i,a[i])

# # # # # # # # x = [1,2,-1,8,8,0,2,-5,-6,7]


# # # # # # # # for i in x:
# # # # # # # #     if i  > 0 :
# # # # # # # #         print(i,'positive')
# # # # # # # #     elif i < 0 :
# # # # # # # #         print(i,'negative')
# # # # # # # #     else:
# # # # # # # #         print(i,'zero')


# # # # # # # # create a list of first 100 numbers
# # # # # # # # [1,2,3,..100]

# # # # # # # # e = []
# # # # # # # # o=[]
# # # # # # # # for i in range(1,101):
# # # # # # # #     z.append(i)
# # # # # # # # print(z)

# # # # # # # # x = [1,1,2,3,4,2,3,4,5,6,7,5,6,7]
# # # # # # # # v = []
# # # # # # # # for i in x:
# # # # # # # #     if i not in v:
# # # # # # # #         v.append(i)
# # # # # # # # print(v)

# # # # # # # ls = [100,2,3,5,-98,3,4,5,-999,3,349]
# # # # # # # # [-999,-98,2,3,3,4]
# # # # # # # largest   = 0
# # # # # # # smallest  = 0

# # # # # # # for i in ls:
# # # # # # #      if i > largest:
# # # # # # #           largest = i
# # # # # # #      elif i < smallest:
# # # # # # #           smallest = i

# # # # # # # print(largest,smallest)


# # # # # # z = [11,12,13,14,15,16,17,18,19,20,21]
# # # # # # l1 = []
# # # # # # l2 = []
# # # # # # mid = len(z)//2
# # # # # # for i in range(len(z)):
# # # # # #      if i <= mid :
# # # # # #         l1.append(z[i])
# # # # # #      else:
# # # # # #         l2.append(z[i])
# # # # # # print(l1)
# # # # # # print(l2)


# # # # # # tuples
# # # # # # sets
# # # # # # dict


# # # # # # tuples
# # # # # # ____

# # # # # # collection of elements
# # # # # # a = (1,2,3,4.5,'hdsu',1,2,3,4,5,(22,2,3,6,3))

# # # # # # ordered
# # # # # # indexed
# # # # # #any elemets
# # # # # # nest

# # # # # # a = [1,2,3,4]
# # # # # # b = (11,12,13,14)


# # # # # # a = 'hari'

# # # # # # del(a)

# # # # # # garbasge collection

# # # # # # del(a[4])
# # # # # # print(a)

# # # # # # ()


# # # # # # set

# # # # # # a = {1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,}
# # # # # # print(a)


# # # # # # mutable
# # # # # # unordered / unindex
# # # # # # no duplicates


# # # # # # set

# # # # # # union
# # # # # # intersection
# # # # # # differece

# # # # # # a = {1,2,3,4,5,6}
# # # # # # b = {6,5,4,3,2,1,6}
# # # # # # print(a==b)
# # # # # # print(a.union(b))
# # # # # # print(a|b)
# # # # # # print(a.intersection(b))
# # # # # # print(a&b)
# # # # # # print(a-b)
# # # # # # print(b-a)


# # # # # # c=str(b)
# # # # # # print(type(c))
# # # # # # list
# # # # # # str
# # # # # # tuple
# # # # # # set
# # # # # # dict


# # # # # # for i in a


# # # # # # itreables


# # # # # # a[1] = 100
# # # # # # b[1] = 200
# # # # # # tuple of index 1
# # # # # #

# # # # # # faster


# # # # # # immutable


# # # # # # dict


# # # # # # collection of data

# # # # # # data key:values

# # # # # # info = {"name":'mohan',"age":32,"location":"kochi"}


# # # # # # print(info["name"])
# # # # # # print(info['age'])


# # # # # # no index
# # # # # # mutable


# # # # # # list
# # # # # # dict


# # # # # # userdata = {}
# # # # # # userdata['name']='mohan'
# # # # # # userdata['age'] = 29
# # # # # # userdata['location'] = 'kochi'
# # # # # # userdata['name'] = 'kumar'
# # # # # # print(userdata)

# # # # # # z = {'name': 'kumar', 'age': 29, 'location': 'kochi','name':{1:'hari'}}
# # # # # # print(z)

# # # # # # dict restriction

# # # # # # key should be unique
# # # # # # key should not be mutable


# # # # # # z = {'name': 'kumar', 'age': 29, 'location': 'kochi',}
# # # # # # pop(8)

# # # # # # z.pop('name')

# # # # # # z.popitem()
# # # # # # print(z)
# # # # # # pop()
# # # # # # popitems()
# # # # # # z.clear()
# # # # # # print(z)
# # # # # # print(z.get('name'))
# # # # # # print(z.keys())
# # # # # # print(z.values())
# # # # # # print(z.items())
# # # # # # z.update({'name':True})
# # # # # # print(z)
# # # # # # ('key','value')
# # # # # # for i in z:
# # # # # #     print(i,z[i])


# # # # # # check if a number is amstrong or not

# # # # # # 153

# # # # # # 1**3+ 5**3+ 3**3
# # # # # # 1+125+27 -- > 153

# # # # # # 1634
# # # # # # 1**4+6**4+3**4+4**4


# # # # # # structural
# # # # # # procedural programming
# # # # # # functional programming
# # # # # # object oriented program


# # # # # # functions

# # # # # # block of code which is executed when it is called


# # # # # # def functioname():
# # # # #     # body of the function


# # # # # def hello():
# # # # #     print('hello good morning')
# # # # # hello()

# # # # #can consider functions as a first class citizen
# # # # # def add():
# # # #     #  print('hello')
# # # # # a = add
# # # # mohan = print
# # # # mohan('mohan')


# # # # arguments


# # # # values to be passed to a functions


# # # def add2(a=0,b=0):
# # #     print(a)
# # #     print(b)

# # # add2(1,3)
# # # # 2 types
# # # # positional
# # # # keyword


# # # a functio  to find fact of a number

# # # XXVII

# # # v
# # # x

# # # v
# # # i

# # # x
# # # x
# # # v
# # # i
# # # i


# # # z= {'I':1,'V':5}

# # # b = "IV"

# # # x = 0

# # # 1
# # # 0
# # # for i in range(len(b)-1,-1,-1):
# # #     if b[i] > b[i-1]:
# # #         x=z[b[i]]-z[b[i-1]]
        
# # # print(x)




# # def fact(num):
# #     f = 1
# #     for i in range(1,num+1):
# #         f *= i
# #     print(f)

# # n = int(input('enter your number : - '))

# # print(fact(5))
      
# # def add2(a,b):
# #     return a,b,a+b
# # print(add2(4,5))


# # print(f'my name is {add2(3,4)}')


# # calculator using function 


# def addz(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return (a*b)
# def div(a,b):
#     return a/b

# def main():
#     while True:
#         num1 = int(input('enter your first number:'))
#         num2 = int(input('enter your second number:'))
#         ch = input('enter your choice \n 1.Addition\n 2.Subtraction\n 3.multiplication\n 4.Division\n 5.Exit\n choice:-')
#         if ch == '1':
#             print(f'sum = {addz(num1,num2)}')
#         elif ch == '2':
#             print(f'diff = {sub(num1,num2)}')
#         elif ch == '3':
#             print(f'pro = {mul(num1,num2)}')
#         elif ch == '4':
#             print(f'qut = {div(num1,num2)}')
#         elif ch == '5':
#             break
#         else:
#             print("invalid choice")


# main()



# # prime numbers within a limit 

# # 10 - 20

# # 2
# # 3
# # 5
# # 7
# # 11
# # 13
# # 17



# # design pattern print 


for i in range(1,6):
    for j in range(1,6):
        if i == 1 or i == 5 or j == 3:
            print('*',end='')
        else:
            print(' ',end='')
    print()


# a = [[1,2],
#     [3,4]]

# b = [[3,4],
#      [5,5]]

# c = [[4,6],
#      [8,9]]

# # 1 1       5
# # 2 1       5 
# # 3 1 2 3 4 5 
# # 4 1       5
# # 5 1       5 
