'''
<Looping Activity: While User == Guilible:
Author:Lee Zhe Tse (Aaron)
Date: September 4, 2020
Description: This is the first time of me using the "for" and "while" function to create loops.
            I've created a game where the user summons the game and enter the number other than the number
            stated by the program. It has two modifications.
'''



def game(): #Creates a function where user could summons the game.
    num_iterations = int(input("Hi, choose how many answers you want the computer to be patient: ")) #Asks the user for how many iterations on how many do they want the program to loop.
    for count in range(num_iterations): #The program is going to repeat on how many times depends on num_iterations before the program ends using "for" statements.
        aNumber = int(input("Enter a number other than 5!")) #It will ask the user to enter a number instead of 5.
        if aNumber == 5: ##If user enters the number 5,
            print("You are not suppose to enter 5!") #It will print out a line saying that the user should not enter 5.
            break #The program will stop looping
    else: #If the user plays the loop after the number of iterations they enter,
        print("Wow, you have patience! I don't have one, so you win!") #The program lose it's patience and stops the program.



def puzzle(): #Same is line 12 but creates another function for another modifications.
    dontEnter = -1 #number that the user should not enter and it will increase the number by 1 at line 28
    num_iterations = int(input("Hi, choose how many answers you want the computer to be patient: "))#Same as Line 13 but for this function instead.
    for count in range(num_iterations):#Same as line 14 but for this function.
        dontEnter = dontEnter + 1 #It will add 1 everytime the program loops, so the number of the user that has to not type increases by 1 every loop.
        aNumber = int(input("enter a number other than " + str(dontEnter)+"!"))#Same as line 15 but to ask the user to enter a number instead of the number generated by "dontEndter"
        if aNumber == dontEnter: #If the user enters the number the programs says to not to,
            print("You are not suppose to enter " + str(dontEnter) + "!") #It will print out a line saying that the user should not enter a number based on the amount of "dontEnter". 
            break #the program will stop looping.
        
    else:#If the user plays the loop after the number of iterations they enter,
        print("Wow, you have patience! I don't have one, so you win!") #The program lose it's patience and stops the program.
        



       




