from tkinter import *
import logic
import design as d

class Game2048(Frame):
    def __init__(self):
        # Initialize the Frame and set up the main window
        Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)
        
        # Corrected the commands dictionary to have unique keys
        self.commands = {
            d.KEY_UP: logic.move_up, 
            d.KEY_DOWN: logic.move_down, 
            d.KEY_LEFT: logic.move_left, 
            d.KEY_RIGHT: logic.move_right  # Fixed the duplicate key issue here
        }

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        # Initialize the game grid
        background = Frame(self, bg=d.BACKGROUND_COLOR, width=d.SIZE, height=d.SIZE)
        background.grid()

        for i in range(d.GRID_LEN):
            grid_row = []
            for j in range(d.GRID_LEN):
                cell = Frame(background, bg=d.BACKGROUND_COLOR_BLOCKS, width=d.SIZE/d.GRID_LEN, height=d.SIZE/d.GRID_LEN)
                cell.grid(row=i, column=j, padx=d.GRID_PADDING, pady=d.GRID_PADDING)
                t = Label(master=cell, text="", bg=d.BACKGROUND_COLOR_BLOCKS, justify=CENTER, font=d.FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)
        
    def init_matrix(self):
        # Initialize the matrix with the starting numbers
        self.matrix = logic.start_game()
        logic.add_two2(self.matrix)
        logic.add_two2(self.matrix)

    def update_grid_cells(self):
        # Update the grid cells based on the current state of the matrix
        for i in range(d.GRID_LEN):
            for j in range(d.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=d.BACKGROUND_COLOR_BLOCKS)
                else:
                    self.grid_cells[i][j].configure(
                        text=str(new_number), 
                        bg=d.BACKGROUND_COLOR_DICT[new_number],  # Use the dictionary to get the color
                        fg=d.CELL_COLOR_DICT[new_number]  # Use the dictionary to get the text color
                    )
        self.update_idletasks()

    def key_down(self, event):
        # Handle key press events and update the game state
        key = event.keysym  # Changed to use keysym for better key recognition
        if key in self.commands:
            self.matrix, changed = self.commands[key](self.matrix)
            if changed:
                logic.add_two2(self.matrix)
                self.update_grid_cells()
                changed = False
                if logic.get_current_state(self.matrix) == "WON":
                    self.grid_cells[1][1].configure(text="You", bg=d.BACKGROUND_COLOR_BLOCKS)
                    self.grid_cells[1][2].configure(text="Win!", bg=d.BACKGROUND_COLOR_BLOCKS)
                if logic.get_current_state(self.matrix) == "LOST":
                    self.grid_cells[1][1].configure(text="You", bg=d.BACKGROUND_COLOR_BLOCKS)
                    self.grid_cells[1][2].configure(text="Lost!", bg=d.BACKGROUND_COLOR_BLOCKS)

# Create the game grid and start the game
gamegrid = Game2048()
