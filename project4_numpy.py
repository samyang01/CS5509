# Using Numpy create random vector of size 15 having only Integers in the range 0 - 20.
# Write a program to find the most frequent item/value in the vector list

import numpy as np

array = np.random.randint(0,20,15)                 # generate 1D array with 15 entries, store random integer from 0-20
array.sort()

''' this project would have been much easier if I just used a dictionary to store the count of each randomly
generated number, but instead, I used a while loop to shorten the array beginning from the item array[0].  
The array is shortened when array[x] is different from array[x+1] and the list of numbers previous to array[x], which
 are by definition identical, are appended as a nested list in alist'''
alist=[]
while True:                                        #
    x = len(array)
    if len(array) == 0:
        break
    for i in range(x):
        if array[0] == array[-1]:
            alist.append(list(array[:]))
            array=array[x:]
            break
        elif array[i] != array[i+1]:
            alist.append(list(array[0:i+1]))
            array = array[i+1:]
            break
'''The length of each list of repeated integers in alist is stored in a new list called key_list, key_list is then 
sorted to find the length of the most frequent integer'''
key_list=[]
for i in range(len(alist)):
    key_list.append(len(alist[i]))
key_list.sort()

'''using a for loop we search each list in alist for those with length equal to the last entry in key_list'''
for i in alist:
    if len(i) == key_list[-1]:
        print(i[0])
