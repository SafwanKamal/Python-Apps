from password_generator import *
from search_password import *
from common_funcs import *



def pass_gen_info_button_clicked(pass_inpt, pass_gen_wn, len_inpt, restrict_symbols_inpt):
    try:
        length = int(len_inpt)
        pass_gen_wn.destroy()
    except:
        pass_gen_wn.destroy()
        gen_pass_button_clicked(pass_inpt)
        return


    
    password = password_generator(length=length, restrict_symbols=restrict_symbols_inpt)
    pyperclip.copy(password)
    pass_inpt.delete(0, END)
    pass_inpt.insert(0, password)

    pass_gen_wn.destroy()


def gen_pass_button_clicked(pass_inpt, length = 10):

    pass_gen_info_wn = Toplevel()
    pass_gen_info_wn.wm_title("Password Generator")
    pass_gen_info_wn.config(bg=WHITE, padx=PADX, pady=PADY)

    pass_len = Label(pass_gen_info_wn, text="Password Length: ", bg=WHITE, fg=BLACK)
    pass_len.grid(row=0, column=0)

    pass_len_inpt = Entry(pass_gen_info_wn, width=10, bg=YELLOW, fg=BLACK, highlightthickness=0)
    pass_len_inpt.grid(row=0, column=1)

    restrict_symbols = Label(pass_gen_info_wn, text="Restricted Symbols: ", bg=WHITE, fg=BLACK)
    restrict_symbols.grid(row=1, column=0)

    restrict_symbols_inpt = Entry(pass_gen_info_wn, width=10, bg=YELLOW, fg=BLACK, highlightthickness=0)
    restrict_symbols_inpt.grid(row=1, column=1)

    ok_button = Button(pass_gen_info_wn, text="Okay", command=lambda: pass_gen_info_button_clicked(pass_inpt, pass_gen_info_wn, pass_len_inpt.get(), restrict_symbols_inpt.get()), bg=YELLOW, highlightbackground=WHITE, highlightthickness=0)
    ok_button.grid(row=2, column=0, columnspan=2)


def add_button_clicked(web_inpt, email_user_inpt, pass_inpt, default_user):
    web = web_inpt.get()
    user = email_user_inpt.get()
    password = pass_inpt.get()

    if len(web) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(message="Please fill in all the fields!", title="Warning!")
        return


    new_row = pd.DataFrame({'Website': [web], 'UserName/Email': [user], 'Password': [password]})

    file_path = "passwords.csv"

    if os.path.exists(file_path):
        new_row.to_csv('passwords.csv', mode='a', index = False, header=False)
    else:
        new_row.to_csv('passwords.csv', mode='a', index = False)

    messagebox.showinfo(title="Success!", message="Password Added!")

    pass_inpt.delete(0, END)
    web_inpt.delete(0, END)
    email_user_inpt.delete(0, END)
    email_user_inpt.insert(0, default_user)

def search_button_clicked(web_inpt, email_user_inpt):
    website = web_inpt.get()
    user = email_user_inpt.get()
    if website == '' and user == '':
        messagebox.showwarning(title="Enter Something!", message="Website and User field empty for password!")
    else:        
        search_result = search_password(web_inpt.get(), email_user_inpt.get())
        if type(search_result) != pd.DataFrame:
            return
        
        if search_result.empty:
            messagebox.showinfo(title="Not Found!", message="No password found under the given username and/or website!")
        else:
            message = ''
            for (index, item) in search_result.iterrows():
                message += f'Website: {item.Website} \n User: {item['UserName/Email']} \n Password: {item.Password} \n\n'
            messagebox.showinfo(title="Found!", message=message)


def password_manager(scr):
    default_user = ""
    with open('default_user.txt', 'r') as default_file:
        default_user = default_file.read()
    
    wn = scr 
    wn.config(bg=WHITE, padx= PADX, pady= PADY)
    wn.title("Password Manager")

    canva = Canvas(wn, width=PHOTO_WIDTH, height=PHOTO_HEIGHT, bg=WHITE, highlightthickness=0)

    pass_man_logo = PhotoImage(file="password_manager_logo.png")
    id_img = canva.create_image(PHOTO_WIDTH / 2, PHOTO_HEIGHT / 2, image=pass_man_logo)
    canva.grid(row = 0, column = 0, columnspan=3)


    web_label = Label(wn, text="Website : ", bg=WHITE, highlightthickness=0, highlightbackground=WHITE, fg=BLACK,  font=(FONT_NAME, FONT_SIZE, "normal"))
    web_label.grid(row=1, column=0, columnspan=1)

    web_inpt = Entry(wn, width=21, bg=YELLOW, fg=BLACK, highlightthickness=0, insertbackground='red')
    web_inpt.grid(row=1, column=1,columnspan=1, sticky='ew')

    search_button = Button(wn, text="Search", bg=YELLOW, highlightbackground=WHITE, highlightthickness=0)
    search_button.grid(row=1, column=2, columnspan=1, sticky='ew')
    search_button.config(command=lambda: search_button_clicked(web_inpt, email_user_inpt))

    email_user_label = Label(wn, text="UserName/Email : ", bg=WHITE, highlightthickness=0, highlightbackground=WHITE, fg=BLACK,  font=(FONT_NAME, FONT_SIZE, "normal"))
    email_user_label.grid(row=2, column=0, columnspan=1)

    email_user_inpt = Entry(wn, width=35, bg=YELLOW, fg=BLACK, highlightthickness=0, insertbackground='red')
    email_user_inpt.grid(row=2, column=1, columnspan=2, sticky='ew')
    email_user_inpt.insert(0, default_user)

    pass_label = Label(wn, text="Password : ", bg=WHITE, highlightthickness=0, highlightbackground=WHITE, fg=BLACK,  font=(FONT_NAME, FONT_SIZE, "normal"))
    pass_label.grid(row=3, column=0, columnspan=1)

    pass_inpt = Entry(wn, width=21, bg=YELLOW, fg=BLACK, highlightthickness=0, insertbackground='red')
    pass_inpt.grid(row=3, column=1, columnspan=1, sticky='ew')


    gen_pass_button = Button(wn, text="Generate Password", bg=YELLOW, highlightbackground=WHITE, highlightthickness=0)
    gen_pass_button.grid(row=3, column=2, columnspan=1, sticky='ew')
    gen_pass_button.config(command=lambda: gen_pass_button_clicked(pass_inpt=pass_inpt))

    add_button = Button(wn, text="Add", bg=YELLOW, highlightbackground=WHITE, highlightthickness=0)
    add_button.grid(row=4, column=1, columnspan=2, sticky='ew')
    add_button.config(command=lambda: add_button_clicked(web_inpt, email_user_inpt, pass_inpt, default_user))


    wn.mainloop()
