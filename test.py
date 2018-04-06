import os, sys
from chat2 import *

root = Tk()
root.title("Chat GUI")
root.geometry("400x400")
a = ChatInterface(root)
a.send_bot_message("Bon dia")
root.mainloop()
