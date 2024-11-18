from tkinter import *
from tkinter import messagebox

import os
import pandas as pd
import pyperclip

YELLOW = "#f7f5dd"
WHITE = "#ffffff"
BLACK = "#000000"


FONT_NAME = "Arial"
FONT_SIZE = 17
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
MIN_WINDOW_WIDTH = 600
MIN_WINDOW_HEIGHT = 450
PADX = 50
PADY = 50

PHOTO_WIDTH = 200
PHOTO_HEIGHT = 200



def clear(scr):
    list = scr.grid_slaves()
    for l in list:
        l.destroy()