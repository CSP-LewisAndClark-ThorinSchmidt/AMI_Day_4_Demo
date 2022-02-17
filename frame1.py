# Frame1.py
# Luke Patton & Jacob Kiefer
# 02/17/22

'''
Frame Example
'''

import tkinter as tk

class Frame1(tk.Frame):
  """ A GUI Frame """

  def __init__(self, master):
    """ Initialize the Frame. """
    
    super(Frame1, self).__init__(master)

    self.master = master
    self.create_widgets()

  def create_widgets(self):
    """ Create a label, and a button that changes the frame. """
    
    # create the label
    msg = "Enter your Login!"
    self.lblOne = tk.Label(self, text = msg)
    self.lblOne.pack()
    self.lbl2 = tk.Entry(self, text = msg)
    self.lbl2.pack()
    self.btnOne = tk.Button(self, text = "Login",  command = self.master.change_to_2)
    self.btnOne.pack()
    rightpassword = "pa$$word"
    if self.lbl2 == rightpassword :
      command = self.master.change_to_2.get
    else:
      print("wrong passsword")