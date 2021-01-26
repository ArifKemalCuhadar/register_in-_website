import re, os
# 1- Write a user registration program.

################################################################################
# Functions:

# This function is checking password.
def check_password(psw, psw2):
    if psw != psw2:
        raise Exception("\nThe second password different from first password.\n")
    elif len(psw) < 8 :
        raise Exception("\nThe password less than 8 characters.\n")
    elif re.search("[\s]", psw):
        raise Exception("\nYou mustn't use space in the password.\n")
    elif not re.search("[0-9]", psw):
        raise Exception("\nYou must use at least one number in the password.\n")
    elif not re.search("[A-Z]", psw):
        raise Exception("\nYou must use at least one uppercase letter in the password.\n")

def check_nickname(nick):
    if len(nick) < 3:
        raise Exception("\nNickname is too short.\n")
    elif re.search("[\s]", nick):
        raise Exception("\nYou mustn't use spaces in nicknames.\n")

def check_name(name):
    if len(name) < 2:
        raise Exception("\nName is too short.\n")

def check_surname(sName):
    if len(sName) < 2:
        raise Exception("\nSurname is too short.\n")

def error(func):
    try:
        if func == check_name:
            func(defName)
        elif func == check_surname:
            func(defSurname)
        elif func == check_nickname:
            func(defNickname)
        elif func == check_password:
            func(defPassword, defPassword2)
    except Exception as ex:
        print(ex)
        error_1 = 0
    else:
        print("----> Okay :)")
    finally:
        pass

################################################################################
    # Add trial right(ekle manasında).

error_1 = 0

while(error_1 == 0):

    error_1 = 1

    defName = input("\tName: ")
    error(check_name)
    defSurname = input("\tSurname: ")
    error(check_surname)
    defNickname = input("\tNickname: ")
    error(check_nickname)
    defPassword = input("\tPassword: ")
    defPassword2 = input("\tAgain Password: ")
    error(check_password)
