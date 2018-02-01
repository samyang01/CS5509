#assignment number 1
#write a program in order to validation password requirements
#check to see that password length is 6-16 characters
#should have at least 1 number
#should have at least 1 special character
#should have at least 1 lower case and one upper case character


def checkpassword(password):
    global x
    if (len(password) > 5) and (len(password) < 17) \
        and password.isdigit() == False \
        and password.isalpha() == False \
        and password.islower() == False \
        and password.isupper() == False \
        and password.isalnum() == False:
            """password is between 6 and 7 characters long, .isalpha() and .isdigit() both being false
               checks to make sure password is not ALL numbers or ALL letters.  .islower() and .isupper
               both being false checks to make sure there is at least one upper and one lower case.  isalum()
               being false checks to make sure password is not ALL letters or number"""
            print('password accepted')
            x = False
    else:
        print('password does not meet requirements')

x = True
while x == True:                      #while loop will re-prompt user for password if it doesn't meet requirements
    print('enter a valid password')
    password = input()
    checkpassword(password)

