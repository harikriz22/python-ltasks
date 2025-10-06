

# # # def addz(*args): #takes as a tuple    return args

# # # addz(4,5,6,4,7)

# # # passing multiple positional arguments

# # def adz(*args):
# #     s = 0
# #     for i in args:
# #         s+=i
# #     return s

# # print(adz(423,32,23,232,5,2,3,3,34,54,6,7,2))
# # def fullname(**kwargs):
# #     f =''
# #     for i in kwargs:
# #         f= f + kwargs[i]+' '
# #     return f

# # print(fullname(fname='robert',mname='downie',lname='jr',secname='mohan',fifthname='kumar',sixname='das'))


# # lambda function

# # is an anonymous function

# # lambda arguments : expression


# # def sumz(a,b):
# #     return a+b

# # # z = lambda x,y : x+y
# # # print(z(6,7))

# # sqr = lambda x : x**2

# # print(sqr(5))

# # square root of a number
# # full name of a person
# # average of 5 numbers
# # perimeter of a circle
# # product of 3 numbers


# # if a person is elligible to vote or not


# # def vote(age):
# #     if age>=18:
# #         print('eligible to vote')
# #     else:
# #         print('not eligible')

# vote = lambda age: 'eligible' if age>=18 else 'not'

# print(vote(35))


# recursion


# to go back


# higher order function

# 2

# function returns a function
# function takes arguments as a function


# def hello():
#     print('mohan')
#     return hello()
#             print('mohan')
#             return hello()
#                      print('mohan')
#                     return hello()
#                          print('mohan')
#                             return hello()


# 10 --> 0

# def tozero(n):
#     if n == 1:
#         return 1
#     return n * tozero(n-1)
# print(tozero(5))


# factorial of a number 


# fibanocci series 

# 10+ 9 + 8 + 7 + 6 + 5 + 4 + 3+ 2+ 1+ 0



def fact(n):
    if n == 1:
        return 1
    else:
        return n * (fact( n - 1))

# 5 * 4 * 3 * 2* 1

print(fact(5))
# sum 

# 10  9 8 7 6 5 4 3 2 1 0


# a = 'hello good morning nice to meet you'
# word = ''
# b = []
# for i in a:
#     if i != ' ':
#         word += i 
#     else:
#         b.append(word)
#         word=''
# b.append(word)
# print(b)
# b = ['hello','good','morning','nice','to','meet','you']
