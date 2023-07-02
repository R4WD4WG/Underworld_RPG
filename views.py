import tkinter as tk
from tkinter import scrolledtext, messagebox
import tkinter.simpledialog

import pickle

from models import Player



# Game Window ------------------------------------------------------------------------------

class GameWindow:
    # Launch Window Parameters
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x600') # Resolution
        self.root.resizable(0, 0) # Not resizable

        # Text box to display game text
        self.text_box = scrolledtext.ScrolledText(root, wrap='word') 
        self.text_box.grid(row=0, sticky='nsew') # row=0 - top frame
        self.text_box.insert('end', 'Welcome to the Underworld, a place of crime and degeneracy...\n')

        # Create a list to store all 8 buttons
        self.buttons = [None]*8

        # Button frame
        self.button_frame1 = tk.Frame(root)
        self.button_frame1.grid(row=1, sticky='ew') # row=1 - bottom frame

        self.button_frame2 = tk.Frame(root)
        self.button_frame2.grid(row=2, sticky='ew')

        self.root.grid_rowconfigure(0, weight=3) 
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # New Game Button
        self.btn_new_game = tk.Button(self.button_frame1, text='New Game', command=self.new_game, height=4) 
        self.btn_new_game.pack(side='left', fill='both', expand=True)

        # Load Game Button
        self.btn_load = tk.Button(self.button_frame2, text='Load Game', command=self.load_game, height=4) 
        self.btn_load.pack(side='left', fill='both', expand=True)

        self.player = None


    # BUTTONS ------------------------------------------------------------------------------
    # Disable Button Function
    def disable_button(self, btn):
        btn.config(state='disabled')


    # Basic Message Function
    def msg(self, m):
        self.text_box.insert('end', str(m) + '\n')
        self.text_box.see(tk.END)


    # Default Button Layout Function
    def default_buttons(self):
        self.buttons[0].config(text='Inspect Nearby', command=self.inspect_nearby, state='normal') # button 1 - Inspect nearby area
        self.buttons[1].config(text='Travel Close', command=self.travel_close, state='normal') # button 2 - Travel Close
        self.buttons[2].config(text='Player Stats', command=self.player_stats, state='normal') # button 3 - Player Stats
        self.buttons[3].config(text='Quest Log', command=self.quest_log, state='normal') # button 4 - Quest Log
        self.buttons[4].config(text='Equipment', command=self.show_equipment, state='normal') # button 5 - Equipment
        self.buttons[5].config(text='Inventory', command=self.show_inventory, state='normal') # button 6 - Inventory
        self.buttons[6].config(text='Save', command=self.save_game, state='normal') # button 7 - Save
        self.buttons[7].config(text='Exit', command=self.exit_game, state='normal') # button 8 - Exit



    # Button 1 / Function 1 - UNDER CONSTRUCTION
    # Inspect Nearby Area
    def inspect_nearby(self):
        self.look_around()


    # Button 2 / Function 2 - UNDER CONSTRUCTION
    # Travel Close
    def travel_close(self):
        pass


    # Button 3 / Function 3 - UNDER CONSTRUCTION
    # Show Player Stats
    def player_stats(self):
        self.msg('')
        self.msg('Stats:')
        for key in self.player.stats:
            stat = self.player.stats[key]
            self.text_box.insert('end', str(key) + ' ' + str(stat) + '\n')


    # Button 4 / Function 4
    # Quest Log
    def quest_log(self):
        self.msg('')
        self.msg('Quests:')
        for i, (key, value) in enumerate(self.player.quests.items()):
            quest_status = value['status']
            quest_points = value['quest_points']
            if quest_status == 'Completed':
                message = f"Quest: {key}\nStatus: {quest_status}\nQuest Points: {quest_points}\n"
            else:
                message = f"Quest: {key}\nStatus: {quest_status}\nQuest Points: Unknown\n"

            if i != len(self.player.quests) - 1: # If not the last quest, append an extra newline
                message += '\n'

            self.text_box.insert('end',message)


    # Button 5 / Function 5 - UNDER CONSTRUCTION - add features
    # Show Equipment
    def show_equipment(self):
        self.msg('')
        self.msg('Equipment:')
        for key in self.player.equipment:
            item = self.player.equipment[key]
            self.text_box.insert('end', str(key) + ' ' + str(item) + '\n')

        
    # Button 6 / Function 6 - UNDER CONSTRUCTION - add features
    # Show Inventory Function
    def show_inventory(self):
        # Displays whole inventory
        empty = 0
        self.msg('')
        self.msg('Inventory:')
        # Loops through inventory, lists items, excluding empty inventory.
        for i, key in enumerate(self.player.inventory):
            item = self.player.inventory[key]
            if item is None:
                empty += 1
            else:
                self.text_box.insert('end', f"{key}: {item}\n")
        # If all inventory slots are empty, then say it
        if empty == len(self.player.inventory):
            self.msg('Your inventory is empty')
            self.msg(f'Empty slots: {empty}')
            # Still tell player empty inventory spaces after listing their items.
        else:
            self.msg(f'Empty slots: {empty}')


    # Button 7 / Function 7
    # Save Game Function
    def save_game(self):
        with open('game_save.pkl', 'wb') as f:
            pickle.dump(self.player, f)
        messagebox.showinfo('Game saved', 'Your progress has been saved.')
        self.msg('Your game progress has been saved.')


    # Button 8 / Function 8
    # Exit Game Function
    def exit_game(self):
        exit_confirm = messagebox.askyesno("Confirmation", "Are you sure you want to exit? All unsaved progress will be lost.")
        if exit_confirm == True:
            exit()
        else:
            pass

    # BUTTONS END -----------------------------------------------------------------------------



    # TRAVEL COMMANDS -------------------------------------------------------------------------


    # Look around function (Inspect Nearby Start)
    def look_around(self):
        # Undercity Start
        if self.player.loc == 'Undercity_Start':
            self.undercity_start()
        elif self.player.loc == 'Undercity_Start_North':
            pass
        elif self.player.loc == 'Undercity_Start_South':
            pass
        elif self.player.loc == 'Undercity_Start_East':
            pass
        elif self.player.loc == 'Undercity_Start_West':
            pass


    # *** INSPECTS ***

    # Undercity Start Inspect
    def undercity_start(self):
        self.msg('')
        self.msg('You are standing in a market. The market is moderately busy, with a small crowd around the stalls.')
        self.msg('Besides the stalls stands an Inn & an Equipment Store.')
        self.msg('What would you like to do?')
        self.buttons[0].config(text='Market Stalls', command=self.undercity_start_stalls)
        self.buttons[1].config(text='Visit the Inn', command=self.undercity_start_inn)
        self.buttons[2].config(text='Shop for Equipment', command=self.undercity_start_equip_shop)
        self.buttons[3].config(text='Back', command=self.default_buttons)
        for button in self.buttons[4:7]:
            self.disable_button(button)


    # Undercity Start - Market Stalls
    def undercity_start_stalls(self):
        self.msg('')
        self.msg('You visit the market stalls. You ')


    # Undercity Start - Inn
    def undercity_start_inn(self):
        self.msg('')


    # Undercity Start - Equipment Shop
    def undercity_start_equip_shop(self):
        self.msg('')



    # New Game Screen-------------------------------------------------------------------------
    # Start Screen Button
    # Load Game Function
    def load_game(self):
        try:
            with open('game_save.pkl', 'rb') as f:
                self.player = pickle.load(f)
            self.text_box.insert('end', f'Welcome back, {self.player.name}!\n')
            # Create 8 buttons and place them on the button frames
            for i in range(8):
                if i < 4: # First four buttons go on button_frame1
                    btn = tk.Button(self.button_frame1, height=4, width=10)
                    btn.pack(side='left', fill='both', expand=True)
                else: # Remaining buttons go on button_frame2
                    btn = tk.Button(self.button_frame2, height=4, width=10)
                    btn.pack(side='left', fill='both', expand=True)
                self.buttons[i] = btn
            
            self.btn_new_game.pack_forget() # hides new game button
            self.btn_load.pack_forget() # hides load game button

            self.default_buttons()

        except FileNotFoundError:
            messagebox.showinfo('No saved game', 'There is no saved game to load.')


    # Starts New Game
    def new_game(self):
        name = ""
        # Name can't be blank test
        while not name:
            name = tkinter.simpledialog.askstring('Name', 'What is your name?', parent=self.root)
            name = name.strip()
            self.player = Player(name)

        self.text_box.insert('end', f'Time to journey into the Underworld {name}...\n')
        self.msg('You start in the Undercity, the capital of Underworld.')
        self.player.loc = self.player.locations[0] # Set the starting location

        self.btn_new_game.pack_forget() # hides new game button
        self.btn_load.pack_forget() # hides load game button

        # Create 8 buttons and place them on the button frames
        for i in range(8):
            if i < 4: # First four buttons go on button_frame1
                btn = tk.Button(self.button_frame1, height=4, width=10)
                btn.pack(side='left', fill='both', expand=True)
            else: # Remaining buttons go on button_frame2
                btn = tk.Button(self.button_frame2, height=4, width=10)
                btn.pack(side='left', fill='both', expand=True)
            self.buttons[i] = btn

        self.default_buttons()
        
