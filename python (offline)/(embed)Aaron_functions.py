'''
<Word in a Box>
Author: Lee Zhe Tse
Date: September 1. 2020
Description: This is the first time of me using the function syntax, "def myFunction():"
            Users have to input a word and the characters for how the outer box would look like
            
'''




def box(aWord, sym): #use the "def" comment to create the new string. User would have to type "box()" and enter a word and a character.
    print(sym * len(aWord)+ sym + sym + sym + sym) #Prints out the first line of the box according to the length of the word user had input so there's enough..... 
    #....space(by using 'len()' comment to calculate the length of the word input.
    print(sym + " " + aWord + " " + sym)#Prints out the second line of the box with the word user inputs.
    print(sym * len(aWord) + sym + sym + sym + sym)#Same as line 15 but prints the last line of the box.




            
        
        

    
