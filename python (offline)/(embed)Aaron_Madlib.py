'''
<Mad Lib>
Author: Lee Zhe Tse (Aaron)
Date: August 20, 2020
Description: This is the first time that we use the input() function. input() function is where the program takes in user input from the keyboard,
store it in a variable,
And use it like any other variable.
'''


yourName = input("Your Name: ") #Asking the user to provide their name.
print("Hello", yourName, ", have a great day!") #Greetings to the user.
oneName = input("Give me a name: ") #Asking the user to give out a random name.
oneLocation = input("Give me a location: ")#Asking the user to provide a random location.
oneAdjective = input("Give me an adjective: ") #Asking the user to provide an adjective.
pluralNoun = input("Give me a plural noun: ") #Asking the user to give a plural noun.
plural2Noun = input("Give me another plural noun: ") # Asking the user to give out another plural noun.
oneAnimal = input("Give me an animal: ") #Asking the user to provide an animal.
twoAnimal = input("Give me another animal: ") #Asking the user to provide another animal.
oneWeapon = input("List a weapon/dangerous/sharp objects: ")#Asking the user to type in something hazardous.
oneAmount = input("Give me a number: ") #Asking the user to provide a random number.
twoAmount = input("Give me another number: ") #Asking the user to provide another number.
veryFunny = input ("Give me a funny sentence: ") #Asking the user to provide a funny sentence.
#This concludes the script for the user to provide information.

#Below the code is where the Python generates the answer based on what the user provides.

#This concludes the code and ends the script.



print("======================================================================")
print(" Crime scene in", oneLocation)
print("======================================================================")
print("A very serious crime scene has happened in", oneLocation)
print("It was a very", oneAdjective, "scene")
print("There were", pluralNoun, "everywhere in the area")
print("It turns out that a/an", oneAnimal, "has been killed with a", oneWeapon)
print("The body contains", oneAmount, "stab wounds and was covered with", plural2Noun)
print("Below the table there is a letter written")
print("It reads:", "'", veryFunny, "'")
print("After analyzing the animal's DNA, it turns out that there is a fingerprint of a/an", twoAnimal, "named", oneName)
print("It was then caught by the police and sentenced to jail for", twoAmount, "years")
print("=======================================================================")
print("Thanks for Playing,", yourName, "!")
print("=======================================================================")
