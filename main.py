# main.py
# Thorin Schmidt
# 02/01/22

'''
My Awesome App

Simple program to demonstrate how to create a login screen and switch frames in a single app.
'''

import tkinter as tk
from frame1 import Frame1 
from frame2 import Frame2

class Root(tk.Tk):
  """Root class"""

  def __init__(self):
    super(Root, self).__init__()
    self.title("My Awesome App")
    self.geometry("300x150")

  def change_to_1(self):
    first_frame.pack(fill = 'both', expand = 1)
    second_frame.forget()
  
  
  def change_to_2(self):
    second_frame.pack(fill = 'both', expand = 1)
    first_frame.forget()
  
# main
root = Root()

first_frame = Frame1(root) 
second_frame = Frame2(root) 

first_frame.pack(fill = 'both', expand = 1)


root.mainloop()