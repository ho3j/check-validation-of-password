"""
Hossein JALILI
Python program to check validation of password 
mehr 1400
check_validation_of_password.py
ver 1.0
"""

import re

while True:
    #password = "$#ho3jAliLi"
    password=input("\nEnter your password for test  OR foe exit emter 'q' :\n")
    if password=="q":
        exit
    flag = 0
    flag_er_len = 0
    flag_er_a_z = 0
    flag_er_A_Z = 0
    flag_er_0_9 = 0
    flag_er__ = 0
    flag_er_s = 0

    while True:
        if (len(password)<8):
            flag = -1
            flag_er_len = -1
            break

        elif not re.search("[a-z]", password):
            flag = -1
            flag_er_a_z = -1
            break
            
        elif not re.search("[A-Z]", password):
            flag = -1
            flag_er_A_Z = -1
            break
            
        elif not re.search("[0-9]", password):
            flag = -1
            flag_er_0_9 = -1
            break
            
        elif not re.search("[_@$!$%^&*_+=/\`~]", password):
            flag = -1
            flag_er__ = -1
            break
            
        elif re.search("\s", password):
            flag_er_s = -1
            flag = -1
            break
        else:
            flag = 0
            print("Valid Password")
            break

    if flag ==-1:
        print("Not a Valid Password !!")
        if flag_er_len == -1 :
            print("len Password is longer than 7 number !!")
        if flag_er_a_z == -1 :
            print("password include : [a-z]")
        if flag_er_A_Z == -1 :
            print("password include : [A-Z]")
        if flag_er_0_9 == -1:
            print("password include : [0-9]")
        if flag_er__ == -1:
            print("password include : [_@$!$%^&*_+=/\`~]")
        if flag_er_s == -1:
            print("password not include : 'space' ")




