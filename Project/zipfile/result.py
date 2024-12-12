# The result GUI file, called by main.py and imports data_model.py
# Project Members: Jike Lu (jikelu), Tanyue Yao (tanyuey), Haowen Weng (hweng), Junxuan Liu (junxuanl), Cecilia Chen (sixuanch)

import sys
from tkinter import *

import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

import matplotlib


matplotlib.use("TkAgg")
from matplotlib import pyplot as pet

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from data_model import Pie_chart_of_weights, bar_chart, show_description, stock_search


# , stock_search


# print expected value
# print bar plot
# print pie chart
# print instruction
# search for a specific stock id
def plot_pie():
    # Create a Figure containing the pie chart
    fig = Pie_chart_of_weights()

    # Create the Matplotlib FigureCanvasTkAgg object,
    # which defines a Tkinter canvas.
    canvas = FigureCanvasTkAgg(fig, master=second_frame)

    # Draw the canvas and place it on the Tkinter window
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def plot_bar():
    # Create a Figure containing the pie chart

    fig = bar_chart()

    # Create the Matplotlib FigureCanvasTkAgg object,
    # which defines a Tkinter canvas.
    canvas = FigureCanvasTkAgg(fig, master=second_frame)

    # Draw the canvas and place it on the Tkinter window
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# def plot_search_result():
#     user_input = entry_stock_id.get()
#     days = entry_days.get()
#     stock_search(user_input,days)

root = tk.Tk()
# create a main fram
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)
# create a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
# add a scrollbar to the canvas
my_scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
# configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
# create another frame inside the canvas
second_frame = Frame(my_canvas)
# add that new frame to a window in the canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# setting the title  
root.title('Plotting in Tkinter')

# dimensions of the main window 
root.geometry("1200x1000")

# MODIFIED
from data_model import portfolio_return
from data_model import portfolio_beta
# plot the expected value:
label_expected_value = tk.Label(second_frame,
                 text="Expected portfolio return: "+str(portfolio_return),
                                font=('Arial', 20))
label_expected_value.pack()
label_beta = tk.Label(second_frame,
                 text="Expected Portfolio beta: " + str(portfolio_beta),
                      font=('Arial', 20))
label_beta.pack()
# button that displays the plot
plot_button = Button(master=second_frame,
                     command=plot_pie(),  # the function executed
                     height=2,
                     width=10,
                     text="Plot")

# place the button  
# in main window 


plot_button_2 = Button(master=second_frame,
                       command=plot_bar(),  # the function executed
                       height=2,
                       width=10,
                       text="Plot")
# plot_button_2.pack()

# print description
description = show_description()
for count in range(0, len(description)):
    label = tk.Label(second_frame,
                     text=description[count])
    label.pack(anchor="w", padx=30)

# Initialize a Label to display the User Input
label_search_stock = Label(second_frame, text="Searching a specific stock here!")
label_search_stock.pack()


def display_text():
    global entry_stock_id
    global entry_days
    input_stock_id = entry_stock_id.get()
    input_days = int(entry_days.get())
    if (input_stock_id == 'QUIT') & (input_days == ''):
        root.destroy()
        exit()
    stock_search(input_stock_id, input_days)


    # search_result_window = tk.Tk()
    # frame = Frame(search_result_window)
    #
    # # Create a Figure containing the pie chart
    # fig = stock_search(input_stock_id,input_days)
    #
    # # Create the Matplotlib FigureCanvasTkAgg object,
    # # which defines a Tkinter canvas.
    # canvas = FigureCanvasTkAgg(fig, master=second_frame)
    #
    # # Draw the canvas and place it on the Tkinter window
    # canvas.draw()
    # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)





search_output_id = tk.Label(second_frame,
                            text="ID here")
search_output_id.pack()

# Create an Entry widget to accept User Input
entry_stock_id = Entry(second_frame, width=40)
entry_stock_id.focus_set()
entry_stock_id.pack()

search_output_days = tk.Label(second_frame,
                              text="days here")
search_output_days.pack()
# to accept days
entry_days = Entry(second_frame, width=40)
entry_days.focus_set()
entry_days.pack()

# Create a Button to validate Entry Widget
search_button = tk.Button(second_frame,
                          text="Search!",
                          width=20,
                          command=display_text)
search_button.pack(pady=20)

quit_button = tk.Button(second_frame,
                          text="QUIT!",
                          width=20,
                          command=sys.exit)
quit_button.pack(pady=20)

# run the gui
second_frame.mainloop()
