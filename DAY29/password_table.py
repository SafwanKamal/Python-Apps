from common_funcs import *
import option_screen


ROW_PADDING = 2

class Table:
     
    def __init__(self,root,data,rows,columns):
        global total_columns, total_rows
        headers = data.columns.values.tolist()

        for j in range(columns): 
            self.e = Entry(root, width=20, fg='black', font=('Arial',16,'bold'), insertbackground='red', bg='white', highlightthickness=1)
                
            self.e.grid(row=1, column=j)
            self.e.insert(END, headers[j])

        # code for creating table
        for i in range(rows):
            for j in range(columns):
                 
                self.e = Entry(root, width=20, fg='black', font=('Arial',16,'normal'), insertbackground='red', bg='white', highlightthickness=1)
                 
                self.e.grid(row=i + ROW_PADDING, column=j)
                self.e.insert(END, data.iat[i, j])
 

def pass_table(scr):
    scr.config(padx=40, pady=40, bg=WHITE)

    canva = Canvas(scr, width=PHOTO_WIDTH, height=PHOTO_HEIGHT, bg=WHITE, highlightthickness=0)

    pass_man_logo = PhotoImage(file="password_manager_logo.png")
    id_img = canva.create_image(PHOTO_WIDTH / 2, PHOTO_HEIGHT / 2, image=pass_man_logo)
    canva.grid(row = 0, column = 0, columnspan=3)

    scroll_bar = Scrollbar(scr) 
    
    scroll_bar.grid(column=4) 

    try:
        data = pd.read_csv("passwords.csv")
    except FileNotFoundError:
        messagebox.showwarning(title='File Does Not Exist!', message="There is no password file yet!")
        clear(scr)
        option_screen.option_screen(scr)
        return

    total_rows = len(data)
    total_columns = len(data.columns)
    t = Table(scr, data, total_rows, total_columns)

    scr.mainloop()

