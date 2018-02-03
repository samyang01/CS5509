# using sets, find the number of vowels in a user input sentence
# the program should be able to return vowels even if there are duplicates

print('provide a sentence to find the number of vowels\n')
userStr = input()
count = 0
vowels = {'a','e','i','o','u','A','E','I','O','U'}    # create set of all vowels, both lower and upper case
for i in userStr:                                     # iterate over the letters of userinput string to find\
    letters = {i}                                     # creating a set for each letter and finding interection\
    aset = letters & vowels                           # of the letter set and vowel set
    if aset != set():                                 # if the intersection is not empty then the letter is a vowel
        count += 1
print(count)