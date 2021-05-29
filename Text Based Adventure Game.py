#Program begins by defining a callback function dummy_proof_func that is called for incorrect user inputs throughout the program
#Function displays a sarcastic message, and uses the exit command to exit and end the program 
def dummy_proof_func():
    print ('''Ok smart alec that's not a proper response to the question, relaunch the program, my creator doesn't know loops yet,
congrats you broke the code. ''')
    exit()

#program then portrays the origin of the story, and asks the user if they want to play the game. Output is controlled with the if operator 
print ("""Hello, and welcome to the Ashlands wanderer. This is a text based adventure game that will ask you to make 
          many decisions along the way, that will influence the way that you survive and prosper! """)
print ("Beware though traveller, one wrong move, and it may be your last...")
print ('Would you like to start the adventure? (key in "y" or "n" to answer this question and all further ones)')
initial_question = input()

#The program then gives the user 2 choices to advance the story, with a nested if command controlling the output and end of the program 
if initial_question == "y":
    print ("And so, the adventure begins!")
    print ("Its nighttime, and you see 2 paths in front of you, the left one that leads into the woods, brambly and barren is the path.")
    print ("The right path is paved and polished, and leads  to what looks like a castle in the background")
    print ('''"Which path do you take? Type "l" for the left path, and "r" for the right path''')
    response_1 = input()
    if response_1 == "l":
        print("And so you decide to proceed into the woods feeling brave, and inside the woods you see a sword in the ground, which gives ")
        print("off a flash of light so bright, that you are blinded by what you see!")
        print("To be continued.....")

    elif response_1 == "r":
        print("You decide to proceed to the castle in the distance, after all who would trust the woods on your lonesome?")
        print("You start walking on the polished paved path, when you suddenly slip on a banana peel that slips all too well on the polished path")
        print("You died on impact")
        print("********BAD END**********")
        exit()
    else:
        dummy_proof_func()


elif initial_question == "n":
    print ("ok why did you even launch this game then")
    exit()

else :
    dummy_proof_func()


