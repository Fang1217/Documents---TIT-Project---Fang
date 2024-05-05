# GUI Library
import tkinter as tk
from tkinter import ttk

# Modernized tkinter library
import customtkinter as ctk

import huffman_coding
# Function when submit button is pressed
def button_action():
    if not len(input_name.get()) == 0:
        table_title.configure(text="Encoding Table for text " + input_name.get())
        df = huffman_coding.huffman_coding(input_name.get())
        calculation.configure(text="Efficiency: " + str(huffman_coding.calculate_efficiency(df)) + "%")
        populate_tree(tree, df)

# App frame
app = ctk.CTk()
app.geometry("720x480")
app.title("Huffman Encoder")

# App Appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# App Grid Layout
app.columnconfigure(0, weight=1, uniform='a')
app.columnconfigure(1, weight=2, uniform='a')
app.rowconfigure((0,1,2,3,4,5,6,7), weight=1, uniform='a')

# Content
title = ctk.CTkLabel(app, text="Input name: ")
title.grid(row=0, column=0, padx=40, sticky="w")

input_name = tk.StringVar()
input_field = ctk.CTkEntry(app, width=350, height=40, textvariable=input_name)
input_field.grid(row=0, column=1, sticky='we', padx=40)

button = ctk.CTkButton(app, text="Generate Encoding Table", command=button_action, width=400)
button.grid(row=1, column=0, columnspan=2)

table_title = ctk.CTkLabel(app, text="")
table_title.grid(row=2, column=0, columnspan=2, padx=40, sticky='w')

calculation = ctk.CTkLabel(app, text="")
calculation.grid(row=6, column=0, columnspan=2, padx=40, sticky='w')


# Populate Treeview with DataFrame data
def populate_tree(tree, dataframe):
    # Delete all previous data
    tree.delete(*tree.get_children()) 
    
    # Insert column headings
    tree['columns'] = list(dataframe.columns)
    for col in dataframe.columns:
        tree.heading(col, text=col)
        tree.column(col, minwidth=0, width=100)

    # Insert data rows
    for i, row in dataframe.iterrows():
        tree.insert('', 'end', values=list(row))

# Create a Treeview widget
tree = ttk.Treeview(app, show='headings')
tree.grid(row=3, column=0, rowspan=3, columnspan=3, padx=100, sticky="NSEW")

# Treeview Modern dark look, taken from https://github.com/TomSchimansky/CustomTkinter/discussions/431
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
    background="#2a2d2e",
    foreground="white",
    rowheight=25,
    fieldbackground="#343638",
    bordercolor="#343638",
    borderwidth=0)
style.map('Treeview', background=[('selected', '#22559b')])
style.configure("Treeview.Heading",
    background="#565b5e",
    foreground="white",
    relief="flat")
style.map("Treeview.Heading",
    background=[('active', '#3484F0')])

# Run app
app.mainloop()