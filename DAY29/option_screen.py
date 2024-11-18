from common_funcs import *
import password_manager
import password_table


def table_button_clicked(scr):
    clear(scr)
    password_table.pass_table(scr)

def pass_man_button_clicked(scr):
    clear(scr)
    password_manager.password_manager(scr)


def option_screen(scr):
    scr = scr
    scr.config(bg=WHITE, padx= PADX, pady= PADY)
    scr.title("Password Manager")


    canva = Canvas(scr, width=PHOTO_WIDTH, height=PHOTO_HEIGHT, bg=WHITE, highlightthickness=0)

    pass_man_logo = PhotoImage(file="password_manager_logo.png")
    id_img = canva.create_image(PHOTO_WIDTH / 2, PHOTO_HEIGHT / 2, image=pass_man_logo)
    canva.grid(row = 0, column = 0, columnspan=3)


    table_button = Button(scr, text="Password Table", bg=YELLOW, highlightbackground=WHITE, highlightthickness=0, command=lambda: table_button_clicked(scr))
    table_button.grid(row=1, column=1, columnspan=1, sticky='ew')

    pass_man_button = Button(scr, text="Password Manager", bg=YELLOW, highlightbackground=WHITE, highlightthickness=0, command=lambda: pass_man_button_clicked(scr))
    pass_man_button.grid(row=2, column=1, columnspan=1, sticky='ew')


    scr.mainloop()

