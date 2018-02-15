'''In any mobile , there is contact list.
Create a list of contacts and then prompt the user to do the following:
a)Display contact by name
b)Display contact by number
c)Edit contact by name
d)Exit '''

import re

contact_list=[{'name':'john','number':'4567834578','email':'john@aol.com'}, {'name':'tammy','number':'9345874758','email':
'tammy@gmail.com'},{'name':'george','number':'8344592039','email':'george@yaoo.com'}]

print('''
a)Display contact by name                      
b)Display contact by number
c)Edit contact by name
d)Add contact
e)Exit''')

a_menu=input()                                          # store user choice in a_menu
if a_menu=='a':
    print('enter name to show contact information')
elif a_menu=='b':
    print('enter number to show contact information')
elif a_menu == 'c':
    print('enter name of contact to edit')
elif a_menu =='d':
    print('enter name of new contact')
elif a_menu =='e':
    print('done')

b_menu=input()                                          # given user choice, store next user input into b_menu

# user chooses to display contact information by name lookup
if b_menu.isalpha() and a_menu == 'a':
    for contact in contact_list:                        # using for statement loop over each entry in list
        if b_menu in contact.values():                  # to find matching name
            list_index = contact_list.index(contact)    # store matching index
            print(contact_list[list_index])
            if b_menu not in contact.values():          # exception if user input not in contact list
                print('no contact information exists for that name')

# user chooses to display contact information by phone number lookup
if b_menu.isdigit() and a_menu == 'b':                 # check to see that user input is a valid phone number
    for contact in contact_list:                       # for-loop over contact list to find matching value
        if b_menu in contact.values():
            list_index = contact_list.index(contact)   # store matching index
            print(contact_list[list_index])
            if b_menu not in contact.values():
                print('no contact exists for this number')

# user chooses to update contact information
if b_menu.isalpha() and a_menu == 'c':                 # email regex to check user input for valid email address
    emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
     )''', re.VERBOSE)
    for contact in contact_list:
        if b_menu in contact.values():
            print('enter new contact information')
            c_menu=input()
            if c_menu.isdigit():                       # if user input matches phone number format, update phone number
                contact['number']=c_menu
                print('contact information updated')
            elif emailRegex.search(c_menu):            # if user input matches email format, update email
                contact['email']=c_menu
                print('email information updated')
            else:
                print('enter a valid email or phone number')
# user chooses to add new contact
if b_menu.isalpha and a_menu == 'd':                   # append new name if user input is valid name
    contact_list.append({'name':b_menu})
    print('enter contact phone number')
    contact_list[-1]['number']=input()
    print('enter contact email address')
    contact_list[-1]['email']=input()

print(contact_list)