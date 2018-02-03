'''write a program using dictionaries to return the words in a sentence as keys and the frequency
of each word as values of the dictionary, sort the keys in alphabetical order'''


print('type any sentence to receive word count\n')
userSent = input()
userSent = userSent.lower()          # convert string to all lower case
userList = userSent.split(' ')       # split user input string into a list of individual words
userList.sort()                      # sort the list by alphabetical order
userDict = dict()
for words in userList:               # iterate over the words in list, creating a dictionary with key=word\
    i = userList.index(words)        # and value=frequency of that word
    userDict.update({userList[i]:userList.count(words)})
print(userDict)