import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import pandas as pd
from tkinter import ttk, filedialog
from tkinter import messagebox
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

App = customtkinter.CTk()
App.title('Conversion App')
App.geometry('500x210')
App.iconbitmap("img\\logo.ico")
App.resizable(True, True)
scales = ['Celsius', 'Fahrenheit', 'Miles', 'Kilometres', 'Stones', 'Kilograms', 'Litres', 'Pints', 'Acres', 'Hectares', 'Euro', 'USD', 'GBP']



def open():
    global dic
    dic = customtkinter.CTkToplevel()
    dic.title('Python Dictionary')
    dic.geometry('1040x600')
    dic.iconbitmap("img\\logo.ico")
    dic.resizable(True, True)

    
    lbl1 = customtkinter.CTkLabel(dic, text='Python Dictionary').pack()

    my_frame = customtkinter.CTkFrame(dic)
    my_frame.pack(fill=BOTH, expand=1) 
    
    tree_scroll = Scrollbar(my_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(my_frame, yscrollcommand=tree_scroll.set, selectmode='extended')
    tree_scroll.config(command=my_tree.yview)


    def file_open():
        filename = filedialog.askopenfilename(
            initialdir='C:\\Users\\%USERPROFILE%\\Desktop',
            title='Open A File',
            filetype=(("xlsx files", "*.xlsx"), ("All Files","*.*"))
        )

        if filename: 
            try:
                filename = r"{}".format(filename)
                df = pd.read_excel(filename)
            except ValueError:
                my_label.config(text="File Not Supported")
            except FileNotFoundError:
                my_label.config(text="File Not Found")


        clear_tree()

        my_tree['column'] = list(df.columns)
        my_tree['show'] = 'headings'

        for column in my_tree['column']:
            my_tree.heading(column, text=column)

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            my_tree.insert('', 'end', values=row)
        
        my_tree.pack()


    def clear_tree():
        my_tree.delete(*my_tree.get_children())
        



    my_menu = Menu(dic)
    dic.config(menu=my_menu)

    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label='Import Spreadsheet', menu=file_menu)
    file_menu.add_command(label='Open', command=file_open)

    button_quit2 = customtkinter.CTkButton(dic, text="Exit Window", command=dic.destroy)
    button_quit2.pack()


    my_label = customtkinter.CTkLabel(dic, text="")
    my_label.pack(pady=20)

dic = customtkinter.CTkButton(App, text='Python Dictionary', command=open)
dic.grid(row=10, column=0)


button_quit = customtkinter.CTkButton(App, text="Exit Program", command=App.destroy)
button_quit.grid(row=5, column=4, pady=5, sticky="nsew")

_from = StringVar()
_from.set(scales[0])
from_menu = OptionMenu(App, _from, *scales)
from_menu.grid(row=0, column=0, pady=5, sticky="nsew")
from_menu.config(bg="black", fg="white")
from_menu["menu"].config(bg="silver")


lbl = customtkinter.CTkLabel(App, text=' convert to ', text_color ="white")
lbl.grid(row=0, column=1, pady=5, sticky="nsew")

to_ = StringVar()
to_.set(scales[0])
to_menu = OptionMenu(App, to_, *scales)
to_menu.grid(row=0, column=2, pady=5, sticky="nsew")
to_menu.config(bg="black", fg="white")
to_menu["menu"].config(bg="silver")


enterL = customtkinter.CTkLabel(App, text='Enter your Value')
enterL.grid(row=1, column=0, columnspan=2, pady=5, sticky="nsew")

numE = customtkinter.CTkEntry(App)
numE.grid(row=1, column=2, columnspan=2, pady=5, sticky="nsew")


def converter():
    From = _from.get()
    To = to_.get()
    num = int(numE.get())

    if From == 'Celsius' and To == 'Fahrenheit':
        conv_num = 9.0 / 5.0 * num + 32
    elif From == 'Fahrenheit' and To == 'Celsius':
        conv_num = (num - 32.0) * 5.0 / 9.0
    elif From == 'Miles' and To == 'Kilometres':
        conv_num = num * 1.60934
    elif From == 'Kilometres' and To == 'Miles':
        conv_num = num * 0.621371
    elif From == 'Stones' and To == 'Kilograms':
        conv_num = num * 6.35029
    elif From == 'Kilograms' and To == 'Stones':
        conv_num = num * 0.157473
    elif From == 'Litres' and To == 'Pints':
        conv_num = num * 1.75975
    elif From == 'Pints' and To == 'Litres':
        conv_num = num * 0.568261
    elif From == 'Acres' and To == 'Hectares':
        conv_num = num * 0.404686
    elif From == 'Hectares' and To == 'Acres':
        conv_num = num * 2.47105
    elif From == 'Euro' and To == 'USD':
        conv_num = num * 1.1319052 
    elif From == 'USD' and To == 'Euro':
        conv_num = num * 0.883521
    elif From == 'Euro' and To == 'GBP':
        conv_num = num * 0.85315557
    elif From == 'GBP' and To == 'Euro':
        conv_num = num * 1.17211
    elif From == 'USD' and To == 'GBP':
        conv_num = num * 0.75392194
    elif From == 'GBP' and To == 'USD':
        conv_num = num * 0.75392194
    else:
        conv_num = 0
    

    numL = customtkinter.CTkLabel(App, text=round(conv_num,2), width=10)
    numL.grid(row=1, column=4, pady=5)


conB = customtkinter.CTkButton(App, text='Convert', command=converter)
conB.grid(row=2, column=0, padx=10, pady=5, columnspan=2)

App.mainloop()
