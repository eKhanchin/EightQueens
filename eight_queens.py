from tkinter import *
from tkinter import ttk
from random import randint


class EightQueensApp:
    '''An app that solves the Eight Queens problem.
    
    Places 8 queens on the chessboard, so that the queens could not attack 
    each other.
    
    Attributes
    ----------
    master : object
        A tkinter root window object
    '''

    def __init__(self, master):
        '''
        Parameters
        ----------
        master : object
            A tkinter root window object
        '''

        self.master = master
        master.title('Eight Queens')
        master.geometry('350x400+300+400')

        self._configure_styles()
        self._x_board_size = 8
        self._y_board_size = 8
        self._queens = 8

        self._create_chess_board()

        ttk.Label(master, text='Eight queens must not attack each other')\
            .place(x=25, y=300)

        ttk.Button(master, text='Place the queens', command=self._place_queens)\
            .place(x=75, y=350, width=200)

    def _configure_styles(self):
        '''Configures style of the app'''

        style = ttk.Style(self.master)
        
        style.configure('TLabel', background='#e0dfde')
        style.configure('TLabel', font=('', 16))

        style.configure('TButton', background='#e0dfde')
        style.configure('TButton', font=('', 14))

        # White slot
        style.configure('White.TLabel', background='#ffffff')
        style.configure('White.TLabel', foreground='#000000')
        style.configure('White.TLabel', font=('', 14, 'bold'))

        # White slot
        style.configure('Black.TLabel', background='#000000')
        style.configure('Black.TLabel', foreground='#ffffff')
        style.configure('Black.TLabel', font=('', 14, 'bold'))

    def _create_chess_board(self):
        '''Creates chess board from black and white labels'''

        base_x = 55
        y = 25
        slot_width = 30
        slot_height = 30
        empty_slots = []
        chess_board = []
        color_num = 0

        for i in range(0, self._x_board_size):
            row = []
            x = base_x

            for j in range(0, self._y_board_size):
                slot_style = self._get_slot_style(color_num)

                slot = ttk.Label(self.master, anchor='center', style=slot_style)
                slot.place(x=x, y=y, width=slot_width, height=slot_height)

                row.append(slot)

                x += slot_width
                color_num = 1 - color_num

                empty_slots.append([i, j])
            
            chess_board.append(row)
            color_num = 1 - color_num
            y += slot_height
        
        self._empty_slots = empty_slots
        self._chess_board = chess_board
                
    def _get_slot_style(self, color_num):
        '''Returns label\'s style.
        
        Parameters
        ----------
        color_num : int
            A number that represents the color - 0 is black, 1 is white
        '''

        if color_num == 0:
            return 'Black.TLabel'
        elif color_num == 1:
            return 'White.TLabel'
        
        return ''
    
    def _place_queens(self):
        '''Places eight queens on the chess board'''

        self._restore_chess_board()

        for queen in range(0, self._queens):
            board_size = len(self._empty_slots)

            try:
                index = randint(0, board_size-1)
            except:
                # Failed to put all 8 queens on the chess board
                # Try again
                self._place_queens()
                break

            next_slot = self._empty_slots[index]

            self._remove_unwanted_slots(next_slot)

            i = next_slot[0]
            j = next_slot[1]

            self._chess_board[i][j].configure(text=u'\u265B', font=('', 20))

    def _remove_unwanted_slots(self, next_slot):
        '''Removes slots where queen is able to attack.
        
        Parameters
        ----------
        next_slot : list
            A list of two numbers that represent the slot on the chess board
        '''

        x = next_slot[0]
        y = next_slot[1]

        # Removes horizontal slots
        for i in range(0, self._x_board_size):
            try:
                self._empty_slots.remove([i, y])
            except:
                continue

        # Removes vertical slots
        for j in range(0, self._y_board_size):
            try:
                self._empty_slots.remove([x, j])  
            except:
                continue

        self._remove_diagonal_unwanted_slots(next_slot, 'upper left')
        self._remove_diagonal_unwanted_slots(next_slot, 'lower left')
        self._remove_diagonal_unwanted_slots(next_slot, 'upper right')
        self._remove_diagonal_unwanted_slots(next_slot, 'lower right')
    
    def _remove_diagonal_unwanted_slots(self, next_slot, direction):
        '''Removes diagonal slots where queen is able to attack.
        
        Parameters
        ----------
        next_slot : list
            A list of two numbers that represent the slot on the chess board
        direction : string
            A direction in which to delete slots
        '''

        i = next_slot[0]
        j = next_slot[1]

        if direction == 'upper left':
            i_increment = -1
            j_increment = -1

            while i>=0 and j>=0:
                try:
                    self._empty_slots.remove([i, j])  
                except:
                    # Does nothing
                    skip = 'skipping'
                
                i += i_increment
                j += j_increment
                
        elif direction == 'lower left':
            i_increment = -1
            j_increment = 1

            while i>=0 and j<self._y_board_size:
                try:
                    self._empty_slots.remove([i, j])  
                except:
                    # Does nothing
                    skip = 'skipping'

                i += i_increment
                j += j_increment
        elif direction == 'upper right':
            i_increment = 1
            j_increment = -1

            while i<self._x_board_size and j>=0:
                try:
                    self._empty_slots.remove([i, j])  
                except:
                    # Does nothing
                    skip = 'skipping'

                i += i_increment
                j += j_increment
        elif direction == 'lower right':
            i_increment = 1
            j_increment = 1

            while i<self._x_board_size and j<self._y_board_size:
                try:
                    self._empty_slots.remove([i, j])  
                except:
                    # Does nothing
                    skip = 'skipping'

                i += i_increment
                j += j_increment
    
    def _restore_chess_board(self):
        '''Clears chess board'''

        empty_slots = []

        for i in range(0, self._x_board_size):
            for j in range(0, self._y_board_size):
                self._chess_board[i][j].configure(text='')

                empty_slots.append([i, j])
        
        self._empty_slots = empty_slots

        
def main():
    root = Tk()
    app = EightQueensApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()