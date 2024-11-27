#Mancala Game with GUI in Python
This is a classic Mancala game implemented using Python and tkinter. Mancala is a two-player strategy board game that involves collecting seeds into "stores" by moving them around the board. The game ends when one player has no more seeds to distribute, and the player with the most seeds in their store wins.

Features
Graphical User Interface (GUI): The game uses the tkinter library to create an interactive board and buttons for each move.
Two-player Mode: Play against a friend on the same computer, with two players taking turns.
Game Rules:
Players take turns selecting a hole on the board and distribute seeds clockwise into other holes.
The goal is to collect more seeds into your store (one of the pits on the board).
Win Condition: The game ends when all pits on one side of the board are empty. The player with the most seeds in their store wins.
Installation Requirements
To run the game, you'll need to have Python 3.x and the tkinter library installed.

Make sure you have Python 3.x installed. You can download it from here.
Install tkinter (it’s usually bundled with Python, but if needed, you can install it separately):
pip install tk

How to Run
Clone or download the repository.
Open a terminal or command prompt.
Navigate to the folder where the script is located.
Run the game using Python:

python Mancala.py
The game window will open, and you can start playing by clicking on the holes on the board.

Gameplay Instructions
The game board consists of 14 holes: 6 on each player's side and 2 stores (one for each player).
Players take turns selecting a hole from their side to distribute seeds.
Clicking a hole will begin the seed distribution process, moving seeds one by one to the following holes in a clockwise direction.
If a player lands a seed in their store, they get another turn.
The game ends when one side of the board is empty. The player with the most seeds in their store at the end of the game wins.

GUI Design
The game board is drawn using buttons and labels in tkinter, and each button represents a hole on the board.
A message box will show the result at the end of the game, announcing the winner.
