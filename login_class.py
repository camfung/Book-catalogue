from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkfont
from stringmanip import split
from create_user import Create_User
from tkinter import messagebox

class LoginScreen:
    def __init__(self):

        self.allow_login = False
        self.window = Tk()
        self.window.configure(bg="#275296")
        self.window.geometry("400x150")
        self.window.title("Book Catalogue Login")

        self.username_frame = Label(self.window, bg="#275296")
        self.username_label = Label(self.username_frame, text="Username:   ", bg="#275296")
        self.username_entry = Entry(self.username_frame)

        self.create_user_Frame = Frame(self.window, bg="#275296")
        self.create_user_Button = Button(self.create_user_Frame, borderwidth=0,
                                         text="Create new account", bg="#275296", fg="white",
                                         command=self.new_user)
        self.f = tkfont.Font(self.create_user_Button, self.create_user_Button.cget("font"))
        self.f.configure(underline=True)
        self.create_user_Button.configure(font=self.f)

        self.title_frame = Frame(self.window)
        self.title_label = Label(self.title_frame,
                                 text="Type in a username and pass word\n to log into the catalogue", bg="#275296")

        self.buttons_Frame = Frame(self.window, bg="#275296")
        self.ok_button = Button(self.buttons_Frame, bg="#275296", text="OK", width=8, command=self.check_login)
        self.cancel_button = Button(self.buttons_Frame, bg="#275296", text="Cancel",
                                    command=self.window.destroy,  width=8, height=1)

        self.password_frame = Frame(self.window, bg="#275296")
        self.password_Label = Label(self.password_frame, text="Password:    ", bg="#275296")
        self.password_entry = Entry(self.password_frame, show="*")

        self.login_image = Image.open("images/loginimg.png")
        self.resize_login = self.login_image.resize((80, 80))
        self.login_img = ImageTk.PhotoImage(self.resize_login)
        self.login = Label(self.window, image=self.login_img, bg="#275296")

        self.username_label.pack(side=LEFT)
        self.username_entry.pack(side=LEFT)

        self.password_Label.pack(side=LEFT)
        self.password_entry.pack(side=LEFT)

        self.login.place(x=20, y=20)
        self.title_label.pack()

        self.title_frame.place(x=111, y=15)
        self.username_frame.place(x=110, y=50)
        self.password_frame.place(x=112, y=80)

        self.create_user_Button.pack()
        self.create_user_Frame.place(x=195, y=110)

        self.ok_button.pack(pady=6)
        self.cancel_button.pack()
        self.buttons_Frame.place(x=330, y=40)


        mainloop()

    def new_user(self):
        x = Create_User()

    def check_login(self):
        self.user = self.username_entry.get()
        self.password = self.password_entry.get()
        input1 = open("catlogue_database/userAndPass.txt", 'r')
        for i in input1:
            i.rstrip()
            i = split(i, '-')
            if self.user == i[0] and self.password+'\n' == i[1]:
                self.allow_login = True
                self.window.destroy()
                return 0
        messagebox.showinfo("Error", "Error Username or Password are incorrect")
        self.password_entry.delete(0, END)
        self.username_entry.delete(0, END)
        return 0


