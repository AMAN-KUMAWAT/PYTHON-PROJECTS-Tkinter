import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe") 

        self.current_player = "X"
        self.game_over = False
        self.board = ["", "", "", "", "", "", "", "", ""]

        self.buttons = []
        for i in range(9):
            button = tk.Button(master, text="", font=("Helvetica", 20), width=3, height=1, command=lambda i=i: self.button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.status_label = tk.Label(master, text="Player X's turn", font=("Helvetica", 16))
        self.status_label.grid(row=3, column=0, columnspan=3)

        self.reset_button = tk.Button(master, text="Reset", font=("Helvetica", 16), command=self.reset)
        self.reset_button.grid(row=4, column=0, columnspan=3)                              

    def button_click(self, i):
        if not self.game_over and self.board[i] == "":
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player)
            if self.check_win():
                self.status_label.config(text="Player {} wins!".format(self.current_player))
                self.game_over = True
            elif self.check_tie():
                self.status_label.config(text="Tie game!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text="Player {}'s turn".format(self.current_player))

    def check_win(self):
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def check_tie(self):
        return "" not in self.board

    def reset(self):
        self.current_player = "X"
        self.game_over = False
        self.board = ["", "", "", "", "", "", "", "", ""]
        for i in range(9):
            self.buttons[i].config(text="")
        self.status_label.config(text="Player X's turn")


root = tk.Tk()
tic_tac_toe = TicTacToe(root)
root.mainloop()
