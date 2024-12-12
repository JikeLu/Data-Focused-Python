# The Main Program, imports survey.py and calls result.py
# Project Members: Jike Lu (jikelu), Tanyue Yao (tanyuey), Haowen Weng (hweng), Junxuan Liu (junxuanl), Cecilia Chen (sixuanch)
from tkinter import *
import tkinter as tk
from tkinter import ttk

from survey import *
from survey import score
import time
# show the survey
survey()
s = score()
print(s)

time.sleep(3)


exec(open('result.py').read())