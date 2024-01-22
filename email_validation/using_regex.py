import re

# a-z
# 0-9
# . _ time 1
# @ time 1
# . 2,3
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your email: ")

if re.search(email_condition , user_email):
    print("valid email")
else:
    print("Please enter right email")