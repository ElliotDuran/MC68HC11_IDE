# !/usr/bin/env python


from tkinter import Tk, Menu, messagebox, filedialog


root = Tk()
root.title('IDE MC68HC11')
root.iconbitmap('app_icon.ico')

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New File",
                      accelerator='Ctrl+N')
file_menu.add_command(label="Open File",
                      accelerator='Ctrl+O')
file_menu.add_separator()
file_menu.add_command(label="Save",
                      accelerator='Ctrl+S')
file_menu.add_command(label="Save As",
                      accelerator='Ctrl+Shift+N')
file_menu.add_separator()
file_menu.add_command(label="Exit")

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo",
                      accelerator='Ctrl+Z')
edit_menu.add_command(label="Redo",
                      accelerator='Ctrl+Y')
edit_menu.add_separator()
edit_menu.add_command(label="Cut",
                      accelerator='Ctrl+X')
edit_menu.add_command(label="Copy",
                      accelerator='Ctrl+C')
edit_menu.add_command(label="Paste",
                      accelerator='Ctrl+V')
edit_menu.add_separator()
edit_menu.add_command(label="Find",
                      accelerator='Ctrl+F')
edit_menu.add_command(label="Replace",
                      accelerator='Ctrl+H')
edit_menu.add_separator()
edit_menu.add_command(label="Select All",
                      accelerator='Ctrl+A')

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
help_menu.add_command(label="Help")

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="About", menu=help_menu)
root.config(menu=menu_bar)

root.mainloop()
