# Author: Ian Riera Smolinska
# Graphic interface based on a project from Jorge Soderberg
from tkinter import *
from app import *
import time
import re
import os
import string

user_name = ["Ian"]
default_window_size = "400x400"

brain = brain()

class ChatInterface(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

		# sets default bg for top level windows
        self.tl_bg = "#EEEEEE"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"
        self.font = "Calibri 12"

        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5)
# Menu bar

    # File
        file = Menu(menu, tearoff=0)
        menu.add_cascade(label="Arxiu", menu=file)
        file.add_command(label="Esborrar chat", command=self.clear_chat)
        file.add_separator()
        file.add_command(label="Sortir", command=self.client_exit)
            
    # Chat interface
        # frame containing text box with messages and scrollbar
        self.text_frame = Frame(self.master, bd=6)
        self.text_frame.pack(expand=True, fill=BOTH)

        # scrollbar for text box
        self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

        # contains messages
        self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Calibri 12", relief=GROOVE,
                             width=10, height=1)
        self.text_box.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar.config(command=self.text_box.yview)

        # frame containing user entry field
        self.entry_frame = Frame(self.master, bd=1)
        self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # entry field
        self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT)
        self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)
        # self.users_message = self.entry_field.get()

        # frame containing send button and emoji button
        self.send_button_frame = Frame(self.master, bd=0)
        self.send_button_frame.pack(side=RIGHT,fill=BOTH)

        # send button
        self.send_button = Button(self.send_button_frame, text="Send", width=5, relief=GROOVE, bg='grey',
                                  bd=1, command=lambda: self.send_message(None), activebackground="#FFFFFF",
                                  activeforeground="#000000")
        self.send_button.pack(side=LEFT, ipady=2)
        self.master.bind("<Return>", self.send_message_event)

        
        self.last_sent_label(date="No s'han enviat missatges")

		
        # indicates last sent message time
    def last_sent_label(self, date):

        try:
            self.sent_label.destroy()
        except AttributeError:
            pass

        self.sent_label = Label(self.entry_frame, font="Calibri 9", text=date, bg=self.tl_bg2, fg=self.tl_fg)
        self.sent_label.pack(side=LEFT, fill=X, padx=3)

# File functions
    def client_exit(self):
        exit()

    # clears chat
    def clear_chat(self):
        self.text_box.config(state=NORMAL)
        self.last_sent_label(date="No messages sent.")
        self.text_box.delete(1.0, END)
        self.text_box.delete(1.0, END)
        self.text_box.config(state=DISABLED)

# Send Message
      
    # allows "enter" key for sending msg
    def send_message_event(self, event):
        self.send_message(user_name[-1])

    # joins username with message into publishable format
    def send_message(self, username):

        user_input = self.entry_field.get()
        username = user_name[-1] + ": "
        message = (username, user_input)
        readable_msg = ''.join(message)
        readable_msg.strip('{')
        readable_msg.strip('}')

        # clears entry field, passes formatted msg to send_message_insert
        if user_input != '':
            self.entry_field.delete(0, END)
            self.send_message_insert(readable_msg)
            print(user_input)
            response=brain.get_response(user_input)
            self.send_bot_message(response)


        # joins username with message into publishable format
    def send_bot_message(self, message):

        bot_answer = message
        print(bot_answer)
        username = "Amanda: "
        message = (username, bot_answer)
        print(message)
        readable_msg = ''.join(message)
        readable_msg.strip('{')
        readable_msg.strip('}')

        # clears entry field, passes formatted msg to send_message_insert
        if bot_answer != '':
            self.entry_field.delete(0, END)
            self.send_message_insert(readable_msg)


    # inserts user input into text box
    def send_message_insert(self, message):
        # tries to close emoji window if its open. If not, passes
        try:
            self.close_emoji()

        except AttributeError:
            pass

        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, message + '\n')
        self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
        self.text_box.see(END)
        self.text_box.configure(state=DISABLED)
