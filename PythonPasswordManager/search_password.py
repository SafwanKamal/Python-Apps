from common_funcs import *

def search_password(website, user):
    try:
        data = pd.read_csv('passwords.csv')
    except FileNotFoundError:
        messagebox.showwarning(title='File Does Not Exist!', message="There is no password file yet!")
        return None
    
    if website == '' and user != '':
        return data[data['UserName/Email'] == user]
    elif website != '' and user == '':
        return data[data['Website'] == website]
    elif website != '' and user != '':
        return data[data['Website'] == website][data['UserName/Email'] == user]

    