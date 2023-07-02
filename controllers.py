import tkinter as tk

from views import GameWindow

class Game:
    def __init__(self):
        # Launch tkinter root
        self.root = tk.Tk()
        self.root.title("Underworld")
        
        # Initialize GameWindow with tkinter root
        self.game_window = GameWindow(self.root)

    def run(self):
        self.root.mainloop()

# if you want to directly run the controller.py file
if __name__ == "__main__":
    game = Game()
    game.run()
