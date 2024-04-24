# GUI Library
import tkinter as tk
from tkinter import ttk

# Modernized tkinter libraries
import customtkinter as ctk
from CTkTable import *

# Function when submit button is pressed
def button_action():
    print("Hello World!")

# App frame
app = ctk.CTk()
app.geometry("720x480")
app.title("Test")

# App Appearance
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

# App Grid Layout
app.columnconfigure(0, weight=1, uniform='a')
app.columnconfigure(1, weight=2, uniform='a')
app.rowconfigure((0,1,2,3,4,5,6,7,8), weight=1, uniform='a')

# Content
title = ctk.CTkLabel(app, text="Input name: ", width = 200)
title.grid(row=0, column=0)

input_name = tk.StringVar()
input_field = ctk.CTkEntry(app, width=350, height=40, textvariable=input_name)
input_field.grid(row=0, column=1, sticky='w')

button = ctk.CTkButton(app, text="Generate Encoding Table", command=button_action)
button.grid(row=1, column=0, columnspan=2)


# Encoding table
huffman_table_headers = [['Symbol', 'Probability', 'Codeword', 'Length']]
huffman_table = CTkTable(app, row=1, column=4, values=huffman_table_headers)
#huffman_table.pack()
test = [[1, 2, 3, 4], [1, 2, 3, 4]]


'''
huffman_table = ttk.Treeview(app, columns=('symbol', 'probability', 'codeword', 'length'), show='headings' )
huffman_table.heading('symbol', text="Symbol")
huffman_table.heading('probability', text="Probability")
huffman_table.heading('codeword', text="Codeword")
huffman_table.heading('length', text="Length")
huffman_table.pack()
'''
# Run app
app.mainloop()