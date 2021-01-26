# Importing modules

import pygame as p
from tkinter import *
from PIL import ImageTk

# Class to manage the movements and points of the teams
class GamePos():
    def __init__(self):
        '''Initializes necessary variables'''

        # Board of CHESSOPOLY
        self.board = [
            ['BL1', 'BP1', 'BR', 'BH', 'BP2', 'BL2'],
            ['BS1', 'BS2', 'BS3', 'BS4', 'BS5', 'BS6'],
            ['__', '__', '__', '__', '__', '__'],
            ['Sp', '__', 'Sp', '__', 'Sp', '__'],
            ['__', 'Sp', '__', 'Sp', '__', 'Sp'],
            ['__', 'Sp', '__', 'Sp', '__', 'Sp'],
            ['Sp', '__', 'Sp', '__', 'Sp', '__'],
            ['__', '__', '__', '__', '__', '__'],
            ['CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6'],
            ['CL1', 'CP1', 'CR', 'CH', 'CP2', 'CL2']
            ]

        # Assets of every character
        self.prop = {
            'BL1':[200, 100, 'Lab 1'],
            'BL2':[200, 100, 'Lab 2'],
            'CL1':[200, 100, 'Lab 3'],
            'CL2':[200, 100, 'Lab 4'],
            'BP1':[400, 200, 'Office 412'],
            'BP2':[400, 200, 'Office 420'],
            'CP1':[400, 200, 'Office 408'],
            'CP2':[400, 200, 'Office 405'],
            'BR':[800, 1000, 'NUST'],
            'CR':[800, 1000, 'NUST'],
            'BH':[600, 400, 'SEECS'],
            'CH':[600, 400, 'NBS'],
            'BS1':[80],
            'BS2':[80],
            'BS3':[80],
            'BS4':[80],
            'BS5':[80],
            'BS6':[80],
            'CS1':[80],
            'CS2':[80],
            'CS3':[80],
            'CS4':[80],
            'CS5':[80],
            'CS6':[80]
            }

        # Character names
        self.char_name = {
            'L':'Lab Engineer',
            'P':'Professor',
            'R':'Rector',
            'H':'HOD',
            'S':'Student'
            }

        # For alternate turns
        self.black_turn = True

        # For the end
        self.result = False

        # For undo move
        self.turns_record = []



    def your_turn(self, turn):
        '''Moves the characters to the possible places.
            Takes the object of 'Turn' Class as an argument'''

        # Assigning the object to a variable
        self.turn = turn

        # Rectangles where shops exist
        shop_spots = [(0, 3), (2, 3), (4, 3), (1, 4), (3, 4), (5, 4), (1, 5), (3, 5), (5, 5), (0, 6), (2, 6), (4, 6)]

        for spot in shop_spots:

            # If character stands on a shop
            if (turn.first_row, turn.first_col) == spot:
                self.board[turn.first_col][turn.first_row] = 'Sp'
                break

        else:
            self.board[turn.first_col][turn.first_row] = '__'

        # If second click's on a shop
        if self.board[turn.sec_col][turn.sec_row] == 'Sp':

            # If it's first time of this character on a shop
            if len(self.prop[turn.turn_from]) == 3:

                # Used in decide_menu()
                self.shop = True
                
                self.decide_menu()

        # Opposite team's variable
        if self.black_turn:
            oppo_team = 'C'
        else:
            oppo_team = 'B'

        # If second click's on opposite team character
        if self.board[turn.sec_col][turn.sec_row][0] == oppo_team:

            # Used in decide_menu()
            self.shop = False

            self.decide_menu()

        # Replacing second click with first to move characters
        self.board[turn.sec_col][turn.sec_row] = turn.turn_from

        # To undo moves later
        self.turns_record.append(turn)

        # Alternate turns
        self.black_turn = not self.black_turn



    def undo_turn(self):
        '''To undo turns. Also used to toggle between the teams at the start of the game.
            Note: It does not undo the properties & assets traded between the characters or with the shops.'''

        if len(self.turns_record) != 0:

            # Pop out the last move
            turn = self.turns_record.pop()

            # Switch places to according to last move
            self.board[turn.first_col][turn.first_row] = turn.turn_from
            self.board[turn.sec_col][turn.sec_row] = turn.turn_to

        # Alternate Turns
        self.black_turn = not self.black_turn



    def the_end(self):
        '''Adds the points of all characters of a team in one variable.
            Returns 2 variables each with a team's total points.'''
        
        black_team = 0
        cyan_team = 0

        # To visit every single rectangle on board
        for col in range(len(self.board)):

            for row in range(len(self.board[col])):

                char = self.board[col][row]

                # If team black's character
                if char[0] == 'B':

                    # if still holding a property
                    if len(self.prop[char]) == 3:
                        char_points = self.prop[char][0] + self.prop[char][1]

                    else:
                        char_points = self.prop[char][0]
                    
                    black_team += char_points

                # If team cyan's character
                elif char[0] == 'C':
                
                    # if still holding a property
                    if len(self.prop[char]) == 3:
                        char_points = self.prop[char][0] + self.prop[char][1]

                    else:
                        char_points = self.prop[char][0]

                    cyan_team += char_points

        return black_team, cyan_team



    def if_end(self):
        '''Returns True if the Rector was captured in the last move.'''
        
        return self.result



    def decide_menu(self):
        '''Displays a window to select options either when clicked on shop or when capturing a character.
            Depends on self.shop'''

        # Specifying window's details
        self.decide = Tk()
        self.decide.title('Decide - CHESSOPOLY')
        self.decide.geometry('404x254')
        self.decide.resizable(False, False)
        self.decide.iconbitmap('images\\icon.ico')

        # Background image
        self.bg = ImageTk.PhotoImage(file='images\\decide.png')
        self.bg_img = Label(self.decide, image = self.bg)
        self.bg_img.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        # True means a shop was clicked
        if self.shop:

            # Question
            self.question = f'''
Welcome to the Shop, {self.char_name[self.turn.turn_from[1]]}!
You own "{self.prop[self.turn.turn_from][2]}".
Will you accept {self.prop[self.turn.turn_from][1]} points for this property?
'''

            # Coordinates for question in decide window
            x_pos = 25
            y_pos = 40

            # Buttons to Accept OR Ignore
            self.agree_btn = Button(self.decide, text = 'Accept', command = self.agree, bg = '#7e6b26', fg = '#e7d789', font = ('Brush Script Std', 17))
            self.agree_btn.place(x = 227, y = 180)
        
            self.ignore_btn = Button(self.decide, text = 'Ignore', command = self.destroyed, bg = '#7e6b26', fg = '#e7d789', font = ('Brush Script Std', 17))
            self.ignore_btn.place(x = 87, y = 180)

        # False means opponent team member was clicked
        else:

            # If holding a property while being captured
            if len(self.prop[self.turn.turn_to]) == 3:

                self.worth = self.prop[self.turn.turn_to][0] + self.prop[self.turn.turn_to][1]


            # If not holding any property
            elif len(self.prop[self.turn.turn_to]) >= 1:

                self.worth = self.prop[self.turn.turn_to][0]

            # Question
            self.question = f'''
Hey {self.char_name[self.turn.turn_from[1]]}!
{self.char_name[self.turn.turn_to[1]]}'s Worth: {self.worth} Points.
Do you want to capture it?
OR
Will you take {self.prop[self.turn.turn_to][0]} Points and switch places with it?
What do you say?
'''

            # Coordinates for question in decide window
            x_pos = 20
            y_pos = 22

            # Buttons to either take assets or capture
            self.agree_btn = Button(self.decide, text = 'Take & Switch', command = self.take_switch, bg = '#7e6b26', fg = '#e7d789', font = ('Brush Script Std', 14))
            self.agree_btn.place(x = 59, y = 190)
        
            self.capture_btn = Button(self.decide, text = 'Capture', command = self.capture_take, bg = '#7e6b26', fg = '#e7d789', font = ('Brush Script Std', 14))
            self.capture_btn.place(x = 259, y = 190)
            
        # Text Box to show the question
        self.txt_box = Label(self.decide, text = self.question, bg = '#e7d789', fg = '#7e6b26', font = ('Brush Script Std', 13))
        self.txt_box.place(x = x_pos, y = y_pos)

        self.decide.mainloop()



    def take_switch(self):
        '''Command to be executed when button 'Take & Switch' is chosen.'''

        # Adding the points of second character to first
        self.prop[self.turn.turn_from][0] += self.prop[self.turn.turn_to][0]

        # Updating second character's points
        self.prop[self.turn.turn_to][0] = 0

        # Switching places
        self.board[self.turn.first_col][self.turn.first_row] = self.turn.turn_to

        # Closing decide window
        self.decide.destroy()



    def capture_take(self):
        '''Command to be executed when button 'Capture' is chosen.'''

        # If Rector is captured
        if self.turn.turn_to[1] == 'R':
            self.result = True

        # Deleting captured one's properties
        del self.prop[self.turn.turn_to]

        self.decide.destroy()



    def destroyed(self):
        '''Closes the shops message window'''
        self.decide.destroy()

    def agree(self):
        '''Updates the property details of the character'''

        # Updating property list of certain character
        self.prop[self.turn.turn_from] = [self.prop[self.turn.turn_from][0]+self.prop[self.turn.turn_from][1],
                                          self.prop[self.turn.turn_from][2]]
        
        self.decide.destroy()

    def allowed_turns(self):
        '''Creates a list of possible turns.'''
        
        turns = []
        
        for col in range(len(self.board)):
            for row in range(len(self.board[col])):

                # First letter of character's name
                team = self.board[col][row][0]
                
                if (team == 'C' and (not self.black_turn)) or (team == 'B' and self.black_turn):

                    # Second letter of character's name
                    char = self.board[col][row][1]
                    
                    if char == 'S':
                        self.students_turns(col, row, turns)

                    elif char == 'L':
                        self.lab_eng_turns(col, row, turns)

                    elif char == 'P':
                        self.prof_turns(col, row, turns)

                    elif char == 'R':
                        self.rector_turns(col, row, turns)

                    elif char == 'H':
                        self.hod_turns(col, row, turns)
                        
        return turns



    def students_turns(self, col, row, turns):
        '''Creates a list of possible turns of Students'''

        if self.black_turn:
            # Checking if the move's on board
            if col+1 < 10:

                # Checking if second click's a shop or empty space
                if self.board[col+1][row] == '__' or self.board[col+1][row] == 'Sp':
                    
                    turns.append(Turn((row, col), (row, col+1), self.board))

                    # Move 2 columns if on starting position
                    if col == 1 and (self.board[col+2][row] == '__' or self.board[col+2][row] == 'Sp'):
                        turns.append(Turn((row, col), (row, col+2), self.board))

                # Generating turns to capture diagonally
                
                if row-1 >= 0:
                    if self.board[col+1][row-1][0] == 'C':
                        turns.append(Turn((row, col), (row-1, col+1), self.board))

                if row+1 < 6:
                    if self.board[col+1][row+1][0] == 'C':
                        turns.append(Turn((row, col), (row+1, col+1), self.board))
                        
        else:
            # Again Checking same things for Cyan Team
            if col-1 >= 0:
                
                if self.board[col-1][row] == '__' or self.board[col-1][row] == 'Sp':
                    turns.append(Turn((row, col), (row, col-1), self.board))
                    
                    if col == 8 and (self.board[col-2][row] == '__' or self.board[col-2][row] == 'Sp'):
                        turns.append(Turn((row, col), (row, col-2), self.board))

                # Generating moves to kill diagonally
                if row-1 >= 0:
                    if self.board[col-1][row-1][0] == 'B':
                        turns.append(Turn((row, col), (row-1, col-1), self.board))

                if row+1 < 6:
                    if self.board[col-1][row+1][0] == 'B':
                        turns.append(Turn((row, col), (row+1, col-1), self.board))



    def lab_eng_turns(self, col, row, turns):
        '''Creates a list of possible turns of Lab Engineers'''

        # Possible spots for Lab Engineer
        lab_eng_spots = [(row-2, col+1), (row-1, col+2), (row+1, col+2), (row+2, col+1),
                         (row+2, col-1), (row+1, col-2), (row-1, col-2), (row-2, col-1)]
        
        if self.black_turn:
            same_team = 'B'
        else:
            same_team = 'C'

        
        for spot in lab_eng_spots:
            
            # Dividing spot into row & column
            sec_row = spot[0]
            sec_col = spot[1]
            
            if 0 <= sec_row < 6 and 0 <= sec_col < 10:
                # Character on that position
                sec_char = self.board[sec_col][sec_row]

                # If opposite team's character
                if sec_char[0] != same_team:
                    turns.append(Turn((row, col), (sec_row, sec_col), self.board))



    def prof_turns(self, col, row, turns):
        '''Creates a list of possible turns of Professors'''

        # Possible directions for Professor
        prof_spots = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
        
        if self.black_turn:
            oppo_team = 'C'
        else:
            oppo_team = 'B'

        for spot in prof_spots:

            # Validating moves in a direction
            for i in range(1, 6):
                sec_row = (spot[0] * i) + row
                sec_col = (spot[1] * i) + col

                # Does not move out of board
                if 0 <= sec_row < 6 and 0 <= sec_col < 10:
                    
                    sec_char = self.board[sec_col][sec_row]

                    # If empty or shops, keep going in this direction
                    if sec_char == '__' or sec_char == 'Sp':
                        turns.append(Turn((row, col), (sec_row, sec_col), self.board))

                    elif sec_char[0] == oppo_team:
                        turns.append(Turn((row, col), (sec_row, sec_col), self.board))
                        # If opposite team character, stop at that point
                        break

                    # Same team character
                    else:
                        break

                else:
                    break


        
    def rector_turns(self, col, row, turns):
        '''Creates a list of possible turns of Rector'''

        # Combination of Professor's move & some other moves
        self.prof_turns(col, row, turns)

        # Possible Directions for Rector
        rector_spots = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        if self.black_turn:
            oppo_team = 'C'
        else:
            oppo_team = 'B'

        for spot in rector_spots:

            # Generating moves for 5 steps in a direction
            for i in range(1, 6):
                
                sec_row = (spot[0] * i) + row
                sec_col = (spot[1] * i) + col

                # Checking if not out of board
                if 0 <= sec_row < 6 and 0 <= sec_col < 10:
                    
                    sec_char = self.board[sec_col][sec_row]
                    
                    if sec_char == '__' or sec_char == 'Sp':
                        turns.append(Turn((row, col), (sec_row, sec_col), self.board))
                        
                    # If opponent encountered, stop checking in this direction
                    elif sec_char[0] == oppo_team:
                        turns.append(Turn((row, col), (sec_row, sec_col), self.board))
                        break

                    # Same team member
                    else:
                        break

                else:
                    break



    def hod_turns(self, col, row, turns):
        '''Creates a list of possible turns of HODs'''

        # Possible spots for HOD
        hod_spots = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        
        if self.black_turn:
            same_team = 'B'
        else:
            same_team = 'C'
            
        for spot in hod_spots:
            
            sec_row = spot[0] + row
            sec_col = spot[1] + col

            # Checking to see if move is out of board
            if 0 <= sec_row < 6 and 0 <= sec_col < 10:
                sec_char = self.board[sec_col][sec_row]

                # Dont move if same team member standing
                if sec_char[0] != same_team:
                    turns.append(Turn((row, col), (sec_row, sec_col), self.board))



# Class to generate the possible turns & turn IDs.
class Turn():
    def __init__(self, first_rec, sec_rec, board):
        '''Initializes variables & defines places on board for characters'''

        # First Click's coordinates
        self.first_row = first_rec[0]
        self.first_col = first_rec[1]

        # Second Click's coordinates
        self.sec_row = sec_rec[0]
        self.sec_col = sec_rec[1]

        # Spot from where character moves
        self.turn_from = board[self.first_col][self.first_row]

        # Spot where character lands after turn
        self.turn_to = board[self.sec_col][self.sec_row]

        # Unique turn ID of every move
        self.turn_ID = str(self.first_row) + str(self.first_col) + str(self.sec_row) + str(self.sec_col)
        
    def __eq__(self, other):
        '''Returns True if the turn ID is an instance of this class.
            Returns False otherwise.'''
        
        if isinstance(other, Turn):
            return self.turn_ID == other.turn_ID
        return False


        
