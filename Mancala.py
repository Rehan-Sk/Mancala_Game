import tkinter as tk
from tkinter import messagebox
class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title("Game")
        
        self.widgets()

    def widgets(self):
        text=tk.Label(self, text="Welcome to Mancala")
        text.pack(pady=10)
        button = tk.Button(self, text="Start", command=self.open_window)
        button.pack(pady=20)
        
    def open_window(self):
        self.withdraw() 
        top = Mancala(self)
        top.protocol("WM_DELETE_WINDOW", self.on_top_window_close)
        top.deiconify() 

    def on_top_window_close(self):
        self.deiconify() 
        self.destroy()
class Mancala(tk.Toplevel):
    def __init__(self,master):
        super().__init__(master)
        self.title("Mancala")
        self.canvas = tk.Canvas(self, width=800, height=400)
        self.canvas.pack()
        self.board = [4] * 14  
        self.board[6] = self.board[13] = 0  
        self.create_board()
        self.current_player = 0
        self.player_names = ["Player 1", "Player 2"]
        self.label = tk.Label(self, text=f"Current Player: {self.player_names[self.current_player]}(1-6)")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Make Move", command=self.make_move)
        self.button.pack()
        self.result = tk.Label(self, text="")
        self.result.pack()
        

    def create_board(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(70, 70, 720, 350, outline="black", width=5)
        for i in range(6):
            self.canvas.create_rectangle(70 + i * 110, 100, 170 + i * 110, 300, outline="black", width=2)
            self.canvas.create_text(120 + (5-i) * 110, 150, text=f"{self.board[i]}", font=("Helvetica", 20))
            self.canvas.create_text(120 +  (5-i)  * 110, 230, text=f"{self.board[12 - i]}", font=("Helvetica", 20))
            self.canvas.create_text(120 + (5-i) * 110, 85, text=f"{i+1}", font=("Helvetica", 20))
            self.canvas.create_text(120 +  (5-i)  * 110, 330, text=f"{13-i}", font=("Helvetica", 20))
        self.canvas.create_rectangle(20, 100, 70, 300, outline="black", width=2)
        self.canvas.create_rectangle(720, 100, 780, 300, outline="black", width=2)
        self.canvas.create_text(45, 200, text=f"{self.board[6]}", font=("Helvetica", 20))
        self.canvas.create_text(750, 200, text=f"{self.board[13]}", font=("Helvetica", 20))
        self.canvas.create_line(70,200,720,200)
        self.canvas.create_text(400, 40, text=f"Player 1", font=("Helvetica", 20))
        self.canvas.create_text(400, 380, text=f"Player 2", font=("Helvetica", 20))

    def switch_player(self):
        self.current_player = 1 - self.current_player
        if  self.current_player==0:
             self.label.config(text=f"Current Player: {self.player_names[self.current_player]}(1-6)")
        else:
            self.label.config(text=f"Current Player: {self.player_names[self.current_player]}(8-13)")

    def make_move(self):
        
        move = int(self.entry.get()) - 1
        
        self.make_player_move(move)
        

    def make_player_move(self, move):
        if move not in self.get_valid_moves():
            messagebox.showerror("Invalid Move", "Please choose a valid position.")
            return
        stones = self.board[move]
        self.board[move] = 0
        current_pos = move
        while stones > 0:
            current_pos = (current_pos + 1) % 14
            if current_pos == 13 and self.current_player == 0:
                continue  
            if current_pos == 6 and self.current_player == 1:
                continue  
            self.board[current_pos] += 1
            stones -= 1
        self.handle_special_conditions(current_pos)
        self.create_board()
        if not self.is_game_over():
            self.switch_player()
        else :
            score = self.evaluate()
            if score > 0:
                self.result.config(text="Player 1 wins")
            elif score < 0:
                self.result.config(text="Player 2 wins")
            else:
                self.result.config(text="It's a tie!")
            
            

    def handle_special_conditions(self, last_pos):
        if last_pos == 6 or last_pos == 13: 
            return
        if self.board[last_pos] == 1 and self.board[12 - last_pos] > 0:
            self.board[self.current_player * 6 + 6+self.current_player] += self.board[12 - last_pos] + 1
            self.board[last_pos] = self.board[12 - last_pos] = 0

    def get_valid_moves(self):
        if self.current_player == 0:
            return [i for i in range(6) if self.board[i] > 0]
        else:
            return [i for i in range(7, 13) if self.board[i] > 0]

    def is_game_over(self):
        return sum(self.board[:6]) == 0 or sum(self.board[7:13]) == 0

    def evaluate(self):
        return self.board[6] - self.board[13]
        

game = GUI()
game.mainloop()
