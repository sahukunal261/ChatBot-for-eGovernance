from tkinter import *
from tkinter import filedialog
from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import webbrowser
import os


"""  
    
 *****Developer Info ****
 Name :     Kunal Sahu
 Email :    sahukunal261@gmail.com
 contact :  8819008039
 Date :     13/4/2019


"""



# Start of Program


# Designing window for registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("450x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="green").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


# Designing window for login
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("450x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button
def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("550x250")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
    root = Tk()
    root.configure(background="white")


    # setting title for the window
    root.title("    ChatterBot    ")


    # creating a text label
    Label(root, text="ChatBot", font=("times new roman", 20), fg="white", bg="maroon", height=2).grid(row=0, rowspan=2, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

    # creating bottom button
    Button(root, text="Government Schemes/Policies", font=("times new roman", 20), bg="#0D47A1", fg='white', command=chat).grid(row=3,columnspan=2,sticky=N + E + W + S,padx=5,pady=5)


    # creating top button
    Button(root, text="About", font=("times new roman", 20), bg="#0D47A1", fg='white', command=about).grid(row=4,columnspan=2,sticky=N + E + W + S,padx=5,pady=5)


    # creating bottom button
    Button(root, text="Developer", font=("times new roman", 20), bg="#0D47A1", fg='white', command=developer).grid(row=5,columnspan=2,sticky=N + E + W + S,padx=5,pady=5)

    
    
    # creating a text label
    Label(root, text="Developed by CodePirates_6 2019", font=("times new roman", 20), fg="white", bg="black", height=2).grid(row=6, rowspan=2, columnspan=2, sticky=W + E + N + S, padx=5, pady=5)





# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global decsuccess
    decsuccess = Toplevel(login_screen)
    decsuccess.title("Success")
    decsuccess.geometry("150x100")
    Label(decsuccess, text="User Not Found").pack()
    Button(decsuccess, text="OK", command=delete_user_not_found_screen).pack()



# script to open about section

def about():
    webbrowser.open('#')

# script to open github link

def developer():
    webbrowser.open('https://github.com/sahukunal261')





def chat():
    bot= ChatBot('Bot')
    trainer = ChatterBotCorpusTrainer(bot)

    corpus_path = 'C:\pro\chatterbot-corpus-master\chatterbot_corpus\data\english/'

    for file in os.listdir(corpus_path):
        trainer.train(corpus_path + file)
    print("Hello sir,How can i help.........")
    while True:
   
#    label .end
        message = input('You:')
        print(message)
        if message.strip() == 'Bye' or message.strip()=='bye':
            print('ChatBot: Bye')
            break
        elif message =='':
            print('ChatBot: Please ask any question...')
 #          goto .end
        elif message == 'date' or message == 'time':
            from datetime import datetime


            now = datetime.now()
            print("now =", now)

    # dd/mm/YY H:M:S
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("date and time =", dt_string)
        else:
            reply = bot.get_response(message)
            print('ChatBot:', reply)
        





# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    decsuccess.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("720x640")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="green", width="50", height="5", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="5", width="50", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="5", width="50", command=register).pack()
    Label(text="Developed by CodePirates_6 2019",height="2",width="50").pack()
    main_screen.mainloop()
    # creating a text label
    

main_account_screen()

# End of Program

