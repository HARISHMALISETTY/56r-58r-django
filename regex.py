# # regex or regular expressions

# x=12345
# y=25.45
# a="hello"
# ip="har123...123com"

# #regex is used to validate,extract,replace a specifc patterns.

# pancardnum="kihjo3987r"

# "5alpahabes4numberssinglealphabet"
# r"[a-z]{5}[0-9]{4}[a-z]{1}"

# match()
# search()
# fullmatch()
# find()
# findall()
# sub()


#to define the patterns using regex
# r"pattern"

# 1.every string should starts with IND

# eg: INDhello, INDwelcome, IND1234,INDok

import re 

# # re.match(pattern,input)
# x=re.match(r"IND","IND123")
# if x:
#     print("it is valid input only")
# else:
#     print("invalid input")
#match method will check only at the starting of the input string
#to check the prefix of given string

# "SBIN98987"
# "ICICI0098"
# "AXIS97987"

# ifsc="SBIN12345"
# sbiValidate=re.match(r"SBIN",ifsc)
# iciciValidate=re.match(r"ICICI",ifsc)
# axisValidate=re.match(r"AXIS",ifsc)

# if sbiValidate:
#     print("it is valid sbi ifsc")
# elif iciciValidate :
#     print("it is valid icici ifsc")
# elif axisValidate:
#     print("it is valid axis ifsc")
# else:
#     print("invalid ifsc")

# bio="AKhil knows python and sql"

# x=re.search(r"python",bio)
# # print(x)
# if x:
#     print("will hire the person")
# else:
#     print("will not hire")


# ip1="cat"
# ip2="cut"
# ip3="c2t"
# ip4="blt"
# ip5="cotokcatch"
# x=re.match(r"c.t",ip3)
# print(x)


#. is basic regex pattern indicates any single character can be present
#^ indicates pattern/string should starts with
#$ indicates pattern/string should ends with 
#[a-z] indicates string should contains any alphabates range
#{m} indicates length of string
#{m,} indicates minimum should be m and maximum anything
#{m,n} indicates max and min length of string
#[0-9] indicates the range of numbers from 0-9

#input should alweays starts with any numbers
# ^
# [0-9]
# ip="1234567890hello world"
# ip1="7hello hyderabad"
# ip2="980hello kukatpally"

# x1=re.match(r"^[0-9]{4}hello",ip2)
# print(x1)

ip1="10000coders"
ip2="10000founders"
ip3="10000developers"
ip4="10000actors"
ip5="10000"

x=re.match(r"^[0-9]{1,}[a-z]{2,}$",ip5)
print(x)
pan1="AXGHT5202O"
validate=re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$",pan1)
print(validate)