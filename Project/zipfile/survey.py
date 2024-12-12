# The survey and its GUI code, imported by main.py and data_model.py
# Project Members: Jike Lu (jikelu), Tanyue Yao (tanyuey), Haowen Weng (hweng), Junxuan Liu (junxuanl), Cecilia Chen (sixuanch)

from tkinter import *
import tkinter as tk
from tkinter import ttk
root = tk.Tk()

# list of points of each answer:
point = {1: [4, 3, 2, 0],
         2: [0, 2, 3, 4],
         3: [1, 2, 3, 4],
         4: [0, 2, 4],
         5: [0, 2, 4],
         6: [0, 2, 3, 4],
         7: [0, 2, 4],
         8: [1, 2, 3, 4],
         9: [0, 4],
         10: [4, 0],
         11: [0, 2, 3, 4],
         12: [0, 1, 3, 4],
         13: [0, 2, 3, 4],
         14: [0, 1, 2, 3, 4, 4],
         15: [0, 1, 2, 3, 4],
         16: [0, 1, 2, 3, 4],
         17: [2, 4, 0],
         18: [0, 1, 2, 3, 4],
         19: [4, 3, 2, 0, 0, 0],
         20: [0, 4, 0, 0]}

# dictionary of options:
question_choice = {1: ['A real gambler',
                       'Willing to take risks after completing adequate research',
                       'Cautious',
                       'A real risk avoider'],
                   2: ["$1,000 in cash",
                       "A 50% chance at winning $5,000",
                       "A 25% chance at winning $10,000",
                       "A 5% chance at winning $100,000"],
                   3: ["Cancel the vacation",
                       "Take a much more modest vacation",
                       "Go as scheduled, reasoning that you need the time to prepare for a job search",
                       "Extend your vacation, because this might be your last chance to go first-class"],
                   4: ["Deposit it in a bank account, money market account, or an insured CD",
                       "Invest it in safe high quality bonds or bond mutual funds",
                       "Invest it in stocks or stock mutual funds"],
                   5: ["Not at all comfortable", "Somewhat comfortable", "Very comfortable"],
                   6: ["Loss", "Uncertainty", "Opportunity", "Thrill"],
                   7: ["Hold the bonds",
                       "Sell the bonds, put half the proceeds into money market accounts, and the other halfinto hard assets",
                       "Sell the bonds and put the total proceeds into hard assetsSell the bonds, \
put all the money into hard assets, and borrow additional money to buy more"],
                   8: ["$200 gain best case; $0 gain/loss worst case",
                       "$800 gain best case; $200 loss worst case",
                       "$2,600 gain best case; $800 loss worst case",
                       "$4,800 gain best case; $2,400 loss worst case"],
                   9: ["A sure gain of $500",
                       "A 50% chance to gain $1,000 and a 50% chance to gain nothing"],
                   10: ["A sure loss of $500",
                        "A 50% chance to lose $1,000 and a 50% chance to lose nothing"],
                   11: ["A savings account or money market mutual fund",
                        "A mutual fund that owns stocks and bonds",
                        "A portfolio of 15 common stocks",
                        "Commodities like gold, silver, and oil"],
                   12: ["Low risk is the best",
                       "60% in low-risk investments 30% in medium risk investments 10% in high risk investments",
                        "30% in low-risk investments 40% in medium risk investments 30% in high risk investments",
                        "YOLO everything on medium and high risk investments"],
                   13: ["Nothing",
                        "One-Three month's salary",
                        "Three-Six month's salary",
                        "I'm gonna put everything in it"],
                   14: ['Some high school or less',
                        'High school graduate',
                        'Some college/trade/vocational training',
                        'Associate degree',
                        'Bachelors degree',
                        'Graduate or professional degree'],
                   15: ['Less than $25,000',
                        '$25,000-$49,999',
                        '$50,000-$74,999',
                        '$75,000-$99,999',
                        '$100,000 or greater'],
                   16: ['Very inexperienced',
                        'Somewhat inexperienced',
                        'Experienced',
                        'Very experienced',
                        'I\'m a gambling god'],
                   17: ['I, and/or someone in my household, make these decisions',
                        'I rely on the advise of a professional (e.g., broker, financial planner, or other consultant)',
                        'I currently have no investment assets'],
                   18: ['1', '2', '3', '4', '5'],
                   19: ['I can buy a house',
                       'More than $102',
                        'Exactly $102',
                        'Less than $102',
                        'Do not know',
                        'Refuse to answer'],
                   20: ['True', 'False', 'Do not know', 'Refuse to answer']
                   }

# list of questions
question = {1: "1. In general,how would your best friend describe you as a risk taker?",
            2: "2. You are on a TV game show and can choose one of the following. Which would you take?",
            3: "3. You have just finished saving for a \"once-in-a-lifetime\" vacation. Three weeks before you plan to leave, you lose your job. You would: ",
            4: "4. If you unexpectedly received $20,000 to invest, what would you do?",
            5: "5. In terms of experience, how comfortable are you investing in stocks or stock mutual funds?",
            6: "6. When you think of the word \"risk\" which of the following words comes to mind first?",
            7: "7. Some experts are predicting prices of assets such as gold, jewels, collectibles, and real estate (hard assets) \
to increase in value; bond prices may fall, however, experts tend to agree that government bonds are relatively safe. Most of \
your investment assets are now in high-interest government bonds. What would you do?",
            8: "8. Given the best- and worst-case returns of the four investment choices below, which would you prefer?",
            9: "9. In addition to whatever you own, you have been given $1,000. You are now asked to choose between:",
            10: "10. In addition to whatever you own, you have been given $2,000. You are now asked to choose between:",
            11: "11. Suppose a relative left you an inheritance of $100,000, stipulating in the will that you invest ALL the money \
in ONE of the following choices. Which one would you select?",
            12: "12. If you had to invest $20,000, which of the following investment choices would you find most appealing?",
            13: "13. Your trusted friend and neighbor, an experienced geologist, is putting together a group of investors to \
fund an exploratory gold mining venture. The venture could pay back 50 to 100 times the investment if successful. If the \
mine is a bust, the entire investment is worthless. Your friend estimates the chance of success is only 20%. If you had \
the money, how much would you invest?",
            14: "14. What is the highest level of education you have completed?",
            15: "15. What is your household's approximate annual gross income before taxes?",
            16: "16. When it comes to investing in stock or bond mutual funds or ETFs - or individual stocks or bonds - I would describe myself as",
            17: "17. Who is responsible for investment allocation decisions in your household?",
            18: "18. On a scale from one to five (where 0 is lowest and 4 is highest), how would you rate your overall \
understanding of personal-finance and money-management concepts and practices?",
            19: "19. Suppose you had $100 in a savings account and the interest rate was 2% per year. After 5 years, \
how much do you think you would have in the account if you left the money to grow?",
            20: "20. Please tell us whether this is true or false. \"Buying a single company\'s stock usually provides a safer return than a stock mutual fund"}

selection_value = {}
def survey():
    global root
    global question_choice
    global question
    global selection_value

    # create a main frame
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH,
                    expand=1)
    # create a canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT,
                   fill=BOTH,
                   expand=1)
    # add a scrollbar to the canvas
    my_scrollbar = tk.Scrollbar(main_frame,
                                orient=VERTICAL,
                                command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,
                      fill=Y)
    # configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',
                   lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    # create another frame inside the canvas
    second_frame = Frame(my_canvas)
    # add that new frame to a window in the canvas
    my_canvas.create_window((0, 0),
                            window=second_frame,
                            anchor="nw")

    root.geometry("700x700")
    root.title("Risk Tolerance Assessment")

    # number of questions
    k = 20

    # list storing selection value
    # Variable to keep track of the option
    # selected in OptionMenu


    for count in range(1, k + 1):
        key = count
        value = tk.StringVar(root)
        value.set("Select an Option")
        selection_value[key] = value


    # generate all questions and selection menus
    for count in range(1, k + 1):
        label = tk.Label(second_frame,
                         text=question[count],
                         wraplength=600,
                         justify="left",
                         anchor="w")
        label.pack(anchor="w", padx=30)
        question_menu = tk.OptionMenu(second_frame, selection_value[count], *question_choice[count])
        question_menu.pack()

    submit_button = tk.Button(root,
                                  text='Submit',
                                  command=print_answers,
                                  pady=20,
                                  padx=30)
    submit_button.pack()

        # function called by submit button that print the selections
    root.mainloop()



def print_answers():
    global selection_value
    for key in selection_value:
        if selection_value[key].get() == "Select an Option":
            popupmsg()
            #exit()

    pop_result(score())


    # pop up when there is question not answered


def popupmsg():
    popup = tk.Tk()
    popup.wm_title("")
    label = tk.Label(popup, text="Please answer all questions!")
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


# calculate ressult:
def score():
    global point
    global question_choice
    global selection_value
    s = 0
    for key in selection_value:
        s = s + point[key][question_choice[key].index(selection_value[key].get())]
    s = s * 1.25
    return s


def pop_result(s):
    global root
    root.destroy()
    popup = tk.Tk()
    popup.geometry("500x300")
    popup.wm_title("")
    label_score = tk.Label(popup, text="Your score is: " + str(s),
                           font=('Arial', 20),
                           justify=LEFT,
                           anchor='w')
    if s >= 90:
        label1 = tk.Label(popup, text="You have a high tolerance for risk.",
                          wraplength=400,
                          justify=LEFT,
                          anchor='w',
                          font=('Arial', 20)
                          )
        label2 = tk.Label(popup, text="You are highly knowledgeable users with "
                                      "a strong capacity for investment.Preferred "
                                      "assets include high-risk stocks, leveraged instruments,"
                                      " and speculative investments. You are well-versed in "
                                      "financial markets and are comfortable with significant "
                                      "market volatility.",
                          wraplength=400,
                          justify=LEFT,
                          font=('Arial', 20)
                          )
    elif (s < 90) & (s >= 70):
        label1 = tk.Label(popup, text="You have an above-average tolerance for risk.",
                          wraplength=400,
                          justify=LEFT,
                          anchor='w',
                          font=('Arial', 20)
                          )
        label2 = tk.Label(popup, text="You have good financial knowledge, willing to "
                                      "take on higher risks for higher returns. Preferred"
                                      " assets are growth stocks, international equities, "
                                      "and more aggressive investment strategies.",
                          wraplength=400,
                          justify=LEFT,
                          font=('Arial', 20))
    elif (s < 70) & (s >= 50):
        label1 = tk.Label(popup, text="You have an average/moderate tolerance for risk.")
        label2 = tk.Label(popup, text="You have moderate financial knowledge and a desire"
                                      " for balanced growth. Preferred assets include a "
                                      "diversified mix of stocks, bonds, and potentially "
                                      "some alternative investments.",
                          wraplength=400,
                          justify=LEFT,
                          font=('Arial', 20))
    elif (s < 50) & (s >= 20):
        label1 = tk.Label(popup, text="You have a below-average tolerance for risk.",
                          wraplength=400,
                          justify=LEFT,
                          anchor='w',
                          font=('Arial', 20))
        label2 = tk.Label(popup, text="You seek modest growth with controlled risk. Preferred assets are a balanced "
                                      "mix of bonds and large-cap stocks.",
                          wraplength=400,
                          justify=LEFT,
                          font=('Arial', 20))
    else:
        label1 = tk.Label(popup, text="You have a low tolerance for risk.",
                          wraplength=400,
                          justify=LEFT,
                          anchor='w',
                          font=('Arial', 20))
        label2 = tk.Label(popup, text="You prefer stability over high returns. "
                                      "Preferred assets for you include government "
                                      "bonds, fixed deposits, and money market funds. "
                                      "Limited financial knowledge is required, with a "
                                      "focus on preserving capital.",
                          wraplength=400,
                          justify=LEFT,
                          font=('Arial', 20))
    label_score.pack(side="top", fill="x", pady=5, padx=50)
    label1.pack(side="top", fill="x", pady=5, padx=50)
    label2.pack(side="top", fill="x", pady=5, padx=50)
    B1 = tk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()

    # Submit button
    # Whenever we click the submit button, our submitted
    # option is printed ---Testing purpose



