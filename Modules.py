# Importing built-in modules
from tkinter import *
from PIL import ImageTk
import pygame as p
import sys

# Importing self-defined modules
from Chessopoly import *
import Engine

p.init()

# BACKGROUND MUSICS

def win_music():
      '''Plays victpry.mp3 on victory of a team'''
    
      p.mixer.init()

      # Loading Music
      p.mixer.music.load("audio\\victory.mp3") 
      p.mixer.music.set_volume(0.6)

      # Playing Music
      p.mixer.music.play()


    
def loop_music():
      '''Plays loop.mp3 on loop until game stops.'''
    
      p.mixer.init()

      # Loading Music
      p.mixer.music.load("audio\\loop.mp3") 
      p.mixer.music.set_volume(0.3)

      # Playing Music
      p.mixer.music.play()



def load_images(rec_width, rec_height):
      '''Loads images in a dictionary.'''
    
      global images
      images = {}

      # All available characters
      characters = ['BL1', 'BP1', 'BL2', 'BP2', 'BR', 'BH',
                    'BS1', 'BS2', 'BS3', 'BS4', 'BS5', 'BS6',
                    'CL1', 'CP1', 'CL2', 'CP2', 'CR', 'CH',
                    'CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6', 'Sp']
      
      for character in characters:

            # Loading Images
            load_img = p.image.load(f'images\\{character}.png')
            images[character] = p.transform.scale(load_img, (rec_width, rec_height))



def draw_board_characs(screen, gs, rec_width, rec_height, rows, columns):
      '''Draws the characters, board and lines on the board.'''

      # For the board
      draw_board(screen, rec_width, rec_height, rows, columns)

      # For the characters
      draw_characs(screen, gs.board, rec_width, rec_height, rows, columns)

      # For grid on board
      draw_lines(screen, rec_width, rec_height, rows, columns)



def draw_board(screen, rec_width, rec_height, rows, columns):
      '''Draws the board on the screen'''

      # RGB Value of Light Golden
      color = (249, 221, 100)
      
      for row in range(rows):
            for col in range(columns):

                  # To draw rectangles on board
                  p.draw.rect(screen, color, p.Rect(col*rec_width, row*rec_height, rec_width, rec_height))



def draw_characs(screen, board, rec_width, rec_height, rows, columns):
      '''Draws the characters on the board'''
      
      for col in range(columns):
            for row in range(rows):

                  # Character's name
                  character = board[col][row]

                  if character != '__':

                        # Displaying characters
                        screen.blit(images[character], p.Rect(col*rec_width, row*rec_height, rec_width, rec_height))



def draw_lines(screen, rec_width, rec_height, rows, columns):
      '''Draws the lines on the board'''

      # Color of lines
      color = p.Color('Black')
      
      for row in range(rows):
            for col in range(columns):
                  # Line under a rectangle
                  p.draw.line(screen, color, (0, (row+1)*rec_height), ((col+1)*rec_width, (row+1)*rec_height), 2)

                  # Line on the right side of rectangle
                  p.draw.line(screen, color, ((col+1)*rec_width, 0), ((col+1)*rec_width, (row+1)*rec_height), 2)



def turn_of(screen, turn_black):
      '''Draws the turn indicator on the board. Tells which team is up for next turn.'''
      p.init()
      p.font.init()
      # Initializing & Defining font
      font = p.font.SysFont("Brush Script MD", 30)

      
      if turn_black:
            txt = font.render(('Turn: Team Black'), True, (0, 0, 0), '#ffffff')
      else:
            txt = font.render(('Turn: Team Cyan '), True, (0, 0, 0), '#ffffff')

      # Draws the text
      try:
            screen.blit(txt, (50, 620))
            p.display.flip()
            
      except:
            pass
  


def result(team1, team2):
      '''Compares the teams & Displays the winners of both the teams.'''
    
      global win_window

      # Closing the main board
      p.quit()

      # Specifying details of the Result Window
      win_window = Tk()
      win_music()
      win_window.title('Results - CHESSOPOLY')
      win_window.geometry('880x614')
      win_window.resizable(False, False)
      win_window.iconbitmap('images\\icon.ico')

      # Background Music
      win = ImageTk.PhotoImage(file = 'images\\result.png')
      win_bg = Label(win_window, image = win)
      win_bg.place(x = 0, y = 0, relwidth = 1, relheight = 1)

      # If Black Teams wins
      if team1 > team2:
            txt = f'''Team Black: {team1} Points.
Team Cyan: {team2} Points.

TEAM BLACK wins the CHESSOPOLY!

Congratulations!'''

      # If Cyan Team wins
      elif team1 < team2:
            txt = f'''Team Black: {team1} Points.
Team Cyan: {team2} Points.

TEAM CYAN wins the CHESSOPOLY!

Congratulations!'''

      # If there's a tie.
      else:
            txt = f'''Team Black: {team1} Points.
Team Cyan: {team2} Points.

There was a tie between the two teams.'''

      # Displaying message & Back to Menu Button
      lbl = Label(win_window, text = txt, bg = '#a28938', fg = '#88001b', font = ('Brush Script MD', 16))
      lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

      menu_btn = Button(win_window, text = 'Menu', command = destroyed, bg = '#7e6b26', fg = '#e7d789', font = ('Brush Script MD', 16))
      menu_btn.place(relx = 0.5, rely = 0.8, anchor = CENTER)

      win_window.mainloop()



def destroyed():
      '''Closes the results window & goes back to main menu.'''
      
      p.mixer.quit()
      win_window.destroy()
      menu_func()
      
def rules1():
      '''Shows a window with rules of the game.'''
      
      global rules

      # Specifying Rules window details
      rules = Tk()
      rules.title('Rules - CHESSOPOLY')
      rules.geometry('880x613')
      rules.resizable(False, False)
      rules.iconbitmap('images\\icon.ico')

      # Background Image
      bgd=ImageTk.PhotoImage(file='images\\rules.png')
      bgd_img=Label(rules, image=bgd).place(x=0, y=0)

      # Basic Rules
      rules_hd='Rules:'
      rules_txt='''Every character has some property in the beginning of the game.
When rector gets captured, total assets of both the teams are compared.
The team with higher number of assets will be the winner of the game.
For more detail, read 'README' file.
'''

      # Property Details
      prop_hd='Properties:'
      prop_txt='''Rector --- NUST
HODs --- SEECS & NBS
Professors --- Office # 412, 405, 420, 408
Lab Engineers ---  Labs 1, 2, 3, 4
Students --- No property.'''

      # Moves' Details
      move_hd='Moves:'
      move_txt='''Rector can 5 steps in any direction
HOD can move only one step in any direction
Professor can move 5 steps diagonally
Lab Engineer mmakes an L on board when moved
Student can move 2 steps forward on first move,
1 step on other moves & captures diagonally'''

      # LABELS FOR EACH HEADING & PARAGRAPH

      # Rules
      label1 = Label(rules, text = rules_txt, bg = '#a28938', fg = 'black', font = ('Brush Script MD', 11))
      label1.place(relx = 0.5, rely = 0.42, anchor = CENTER)

      label2 = Label(rules, text = rules_hd, bg = '#a28938', fg = 'black', font = ('Brush Script MD', 14, 'bold'))
      label2.place(relx = 0.33, rely = 0.32, anchor = CENTER)

      # Properties
      label3 = Label(rules, text = prop_txt, bg = '#a28938', fg = 'black', font = ('Brush Script MD', 12))
      label3.place(relx = 0.53, rely = 0.58, anchor = CENTER)

      label4 = Label(rules, text = prop_hd, bg = '#a28938', fg = 'black', font = ('Brush Script MD', 14, 'bold'))
      label4.place(relx = 0.3, rely = 0.5, anchor = CENTER)

      # Moves
      label5 = Label(rules, text = move_txt, bg = '#a28938', fg = 'black', font = ('Brush Script MD', 12))
      label5.place(relx = 0.5, rely = 0.79, anchor = CENTER)

      label6 = Label(rules, text = move_hd, bg = '#a28938', fg = 'black', font = ('Brush Script MD', 14, 'bold'))
      label6.place(relx = 0.29, rely = 0.7, anchor = CENTER)

      # Back to menu
      back_btn=Button(rules, text = 'BACK', command = back_to_menu, bg = '#7e6b26', fg = 'black', font = ('Brush Script MD', 16, 'bold'))
      back_btn.place(relx = 0.5, rely = 0.91, relwidth = 0.1, relheight = 0.05, anchor = CENTER)

      rules.mainloop()

def back_to_menu():
      '''Closes the Rules window & goes back to main menu'''
      rules.destroy()
      menu_func()


