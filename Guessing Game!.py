import random 

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

flag = True

while flag:
    num =  input("Please type in a number to get an upper bound!")
    if num.isdigit():
         print("Lets Play!")
         num = int(num)
         flag = False
    else:
        print("Guess is out of bounds!")

secret =  random.randint(1,num)
guess =  None
count = 1 

while guess != secret:
    guess = input("Try to guess a number between 1 and " + "  "+ str(num)+ " : ")

    if guess.isdigit():
        guess = int(guess)


    if guess == secret:
        print("Congratulations you have guessed it!")
       
    else:
        print("Wrong ! Guess again!")
        count = count + 1

print("It took you ",count, " times to figure it out!52")




    

