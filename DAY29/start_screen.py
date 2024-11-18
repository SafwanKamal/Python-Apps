from password_manager import *
from option_screen import *
from common_funcs import *


file = open("master_password.txt", 'r')
master_password = file.read()
file.close()


def submit_button_clicked(start_scr, master_password_inpt, wrong_pass_label):
    user_inpt = master_password_inpt.get()
    master_password_inpt.delete(0, END)

    if user_inpt != master_password:
        wrong_pass_label.config(text = "WRONG PASSWORD", fg='red')
    else:
        clear(start_scr)
        option_screen(start_scr)





start_scr = Tk()
start_scr.config(bg=WHITE, padx= PADX, pady= PADY)
start_scr.title("Password Manager")



canva = Canvas(start_scr, width=PHOTO_WIDTH, height=PHOTO_HEIGHT, bg=WHITE, highlightthickness=0)

pass_man_logo = PhotoImage(file="password_manager_logo.png")
id_img = canva.create_image(PHOTO_WIDTH / 2, PHOTO_HEIGHT / 2, image=pass_man_logo)
canva.grid(row = 0, column = 0, columnspan=3)

master_password_label = Label(start_scr, text="PASSWORD : ", bg=WHITE, highlightthickness=0, highlightbackground=WHITE, fg=BLACK,  font=(FONT_NAME, FONT_SIZE, "normal"))
master_password_label.grid(row=1, column=0, columnspan=1)

master_password_inpt = Entry(start_scr, width=35, bg=YELLOW, fg=BLACK, highlightthickness=0, insertbackground='red')
master_password_inpt.grid(row=1, column=1,columnspan=2, sticky='ew')

wrong_pass_label = Label(start_scr, text="", bg=WHITE, highlightthickness=0, highlightbackground=WHITE, fg=BLACK,  font=(FONT_NAME, FONT_SIZE, "normal"))
wrong_pass_label.grid(row=2, column=1, columnspan=1)

submit_button = Button(start_scr, text="Submit", bg=YELLOW, highlightbackground=WHITE, highlightthickness=0, command=lambda: submit_button_clicked(start_scr, master_password_inpt, wrong_pass_label))
submit_button.grid(row=3, column=1, columnspan=1, sticky='ew')

start_scr.mainloop()