# 123--->integer
# 123.25--->float
# "586ddfgjf"--->string


# "xyz29832213"
# "78979xyz7978"
# "dchdc54645"

#here we are having our own patterns for text.

#regex.--->

#integer,float,string,list,tuple,dictionary,regex.
import re

# ip1="SBIN1234"
# ip2="ICICI1234"
# ip3="AXIS1234"
# ip4="HDFC1234"
#regex
# match()--->it will checks the pattern in the given strin
# regex string or pattern
# op=re.match(r"ICICI",ip1)

# if op:
#     print("it is correct ifsc code")
# else:
#     print("it is incorrect ifsc code")


# ip1="ICICI1234"
# if re.match(r"SBIN",ip1):
#     print("it is sbi ifsc code")
# elif re.match(r"ICICI",ip1):
#     print("it is icici ifsc code")
# elif re.match(r"AXIS",ip1):
#     print("it is AXIS ifsc code")
# elif re.match(r"HDFC",ip1):
#     print("it is hdfc ifsc code")
# else:
#     print("invalid ifsc code")



#it can contains any alphabates but 4
#it can contains any numbers  but 5

#regex->
# [a-z]{4}
# [0-9]{5}

#starts with alphabates--> ^
#ends with number---> $

#user input should starts with any 4 alphabates and ends with any 5 numbers

# ip="CHARANTEJ25869"

# x=re.match(r"^[A-Z]{4,8}[0-9]{5,}$",ip)
# print(x)

# {m}-->length should be exactly m 
# {m,}--->length should be minimum m and maximum user wish 
# {m,n}--->length should be minimum m and maximum n .

# [j-q]
# [4-9]
#KOPLM3067Y
#KKK9996661
# ip_pan1="DEL903897T"

# op_pan=re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$",ip_pan1)
# print(op_pan)
# if op_pan:
#     print("valid pan number")
# else:
#     print("invalid pan number")


# ip1="hello world"
# ip2="world hello welcome"
# ip3="hello hyderabad"

# x1=re.search(r"hello",ip1)
# print(x1)

# x2=re.search(r"hello",ip2)
# print(x2)

# x3=re.search(r"hello",ip3)
# print(x3)



#to validate input data with our customised patterns.

#match and search

#^,$,[],{}

# mobile_num_pattern=r"^[7-8]{1}[0-9]{9}$"
# ip="7524179623"
# op=re.match(mobile_num_pattern,ip)
# print(op)


#username can contains LC,UC,Digits,_ and length
#  should be in b/w 8 and 15

username_pattern=r"^[A-Za-z0-9_\.]{8,15}$"
ip="James.999"
op=re.match(username_pattern,ip)
# print(op)


#strong password.

# password_pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9@._]{9,12}$"

# # (?=.*[A-Z]) --->assure atleast one uppercase in string 
# # (?=.*[a-z])--->assure atleast one lowercase in string
# # (?=.*[0-9])--->assure atleast one digit in string
# pswd="INDIAhello2"
# pop=re.match(password_pattern,pswd)
# print(pop)

# email1="harish.tech@gmail." 
# email2="akhil123.tech@yahoo.in" 
# email3="_kiran.mgr@10000coders.in" 

# 1.pattern before @
# 2.pattern after @ 
# 3.pattern for domain name before and after .

# email_pattern=r"^[A-Za-z0-9._]+@[A-Za-z0-9]+\.[a-zA-Z]{2,}$"
# op=re.match(email_pattern,email1)
# print(op)



