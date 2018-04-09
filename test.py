# Author: Ian Riera Smolinska
import os, sys
from chat2 import *


root = Tk()
root.title("Chat GUI")
root.geometry("400x400")

print("checkpoin 1")

a = ChatInterface(root)

print("checkpoin 2")

a.send_bot_message("Bon dia")

root.mainloop()
