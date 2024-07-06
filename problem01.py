# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

wlist={"Pani":"Water",
       "Aam":"Mango",
       "Angoor":"Grapes",
       "Tarbuj":"Watermelon",
       "Amrood":"Gauva",
       "jamun":"Blackberry"}

word=input("Enter a word:")
print(wlist[word])