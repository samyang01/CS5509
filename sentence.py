"""Lab 1 assignment #2, write a program that accepts a sentence from the user
and returns
    1. middle word
    2. longest word in the sentence
    3. reverse all the worse in the sentence"""

print('Enter a sentence')
sentence = input()

senList = sentence.split()                             #split sentence into a list of individual words store in senList

def midword(senList):                                  #define function to return the middle word
    x = len(senList)//2                                #x is the floored quotient of list length/2
    if len(senList)%2 == 0:                            #check to see if list length is even
        print (senList[x-1:x+1])                       #if list length is even then the middle words are in indexes/
    else:                                              # x-1, x
        print (senList[x])

midword(senList)

def longword(senList):                                 #define function to return longest word in list
    newlist = []
    x = len(senList)                                   #x=list length
    for i in range(x):
        newlist.insert(i, len(senList[i]))             #create new list with values=the length of words in senList
        newlist.sort()                                 #sort the new list to find the largest value

    for j in range(x):
        if len(senList[j]) == int(newlist[-1]):        #compare the length of each word in senList with largest/
            print(senList[j])                          #value in newlist and print words that match in value

longword(senList)
"""I think the trick here is to treat each word as an individual list"""
def reverseword(senList):                              #define function to return sentence in reverse
    x = len(senList)
    for i in range (x):
        newlist = list(senList[i])                     #create a newlist *INSIDE* the for statement that contains the/
        newlist.reverse()                              #letters of each word then reverse order the newlist
        newlist2=''.join(newlist)                      #join the list back together to return a string
                                            #??? joining list in place and printing does not work, must place value/
        print(newlist2, end=' ')            #??? in new list

reverseword(senList)
