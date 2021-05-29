Basic Text Based Adventure README Program File 

Program begins by defining a callback function "dummy_proof_func" that is called for incorrect user inputs throughout the program
- Function displays a sarcastic message, and uses the exit command to exit and end the program 
- As Program gets more advanced, this function will be used as/in a loop 

Afterwards, the program then portrays the origin of the story, and asks the user if they want to play the game. Output is controlled with the if operator 
- If user keys in n, the program will display a message, and quit using the quit command 
- If user keys in y, the program will continue the game 
- If the user keys in anything else, the dummy_proof_func function will be called and the program will end 
	- This will change to loop behavior in future iterations of the game

The program then gives the user 2 choices to advance the story, with a nested if command controlling the output and end of the program 
- If the user picks the correct path, the story will proceed, though the next part of the story will come out in a future iteration
- If the user picks the wrong path, the program ends with the death of the character in the game
- If the user keys in anything else, the dummy_proof_func function will be called and the program will end 

Game will be updated to loop type behavior and further finished paths in future iterations