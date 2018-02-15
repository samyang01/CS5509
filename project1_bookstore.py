# using a dictionary, create a list of books and corresponding book prices\
# for a range of user prices, return books that are available in user input range

'''instead of creating a book list with prices as a dictionary, I found a book list with prices as a
   .xlsx file on the internet, and imported that as the book list for this project'''

import openpyxl, pprint
wb=openpyxl.load_workbook('Booklist.xlsx')          # save the booklist.xlsx file as an excel object in wb
sheet=wb['Sheet1']                                  # access the first sheet of wb and save as object 'sheet'
book_shop={}

for row in range(2, sheet.max_row+1):               # by iterating over the rows of the first two columns of 'sheet'/
    book_title = sheet['A'+str(row)].value          # I imported the data into the empty an empty dictionary
    book_price = sheet['D'+str(row)].value
    book_shop.setdefault(book_title, book_price)
book_file=open('book_file.py', 'w')                 # write the dictionary to a new file for later access
book_file.write('book_price_list =' + pprint.pformat(book_shop))
book_file.close()

import book_file
print('Enter minimum price for books\n')            # query user for price range for books in the list
userMin = int(input())
print('Enter maximum price for books\n')
userMax = int(input())

for k, v in book_file.book_price_list.items():      # using a for loop to search the dictionary for values that
    if v <= userMax and v>= userMin:                # within the user input range and returning the key
        print(k+'\n')
