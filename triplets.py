#Lab1 Assignment 3
#Given a list of n number, write a Python program to find triplets in the list which gives the sum of zero

import itertools, re
triplets=[]                                             # define triplets as a list
print('Enter a series of integers separated by comma')
userInput = str(input())                                # store input in userInput as a string
userList = re.findall(r'-?\d+', userInput)              # using the regular expression -?\d+ to find string of \
for groups in itertools.combinations(userList,3):       # integers in the userInput string and store as a list
    triplets.append(groups)                             # combination function in itertools module finds all triplets

count = 0
for i in range(len(triplets)):                          # loop over the number of triplets, adding integers in each triplet
    total=int(triplets[i][0])+int(triplets[i][1])+int(triplets[i][2])
    if total == 0:
        count += 1                                      # for each triplet where sum is zero, count += 1, print the \
        print(triplets[i])                              # triplet
if count == 0:                                          # if count = 0, then there are no triplets that equal zero
    print('no triplets add to 0')

