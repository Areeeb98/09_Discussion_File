"""
Day: Monday
Date: 16th Jan 2023
Time: 10:50 PM
Topic: Discusssion on strings type
Author: Areeb Ahmed
"""


# a=5; b=7.2; c='py' ; d='on' ; e=8 ; f='6.3'
# print(a+e) # int + int --> int 13
# print(a+e,type(a+e)) # 13 <class 'int'>

# print(a+b) # int + float --> float
# print(a+b,type(a+b)) # 12.2 <class 'float'>

"""print(a+c) # int + str --> TypeError"""
"""print(a+f) # int + str --> TypeError"""

# print(str(a)+f) #str + str --> str
# print(str(a)+f,type(str(a)+f)) # 56.3 <class 'str'>

# print(b+e) # float + int --> float
# print(e+b) # int + float --> float

a=5; b=7.2; c='py' ; d='on' ; e=8 ; f='6.3' ; g='4'

'''print(a+g) # int + str --> TypeError'''

# print(int(g))
# print(float(g))
# print(a+int(g))
# print(a+float(g))

'''print(int(f)) # ValueError''' 

# print(float(f)) #6.3
# print(str(f)) # 6.3

# w=float(f) # 6.3
# print(int(w)) # 6

# print(str(a)+d)
# print(a+float(f))