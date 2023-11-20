from tkinter import *
from PIL import Image, ImageTk
from stringmanip import split
from tkinter import messagebox

class Create_User:
    def __init__(self):
        self.window = Tk()
        self.window.configure(bg="#275296")
        self.window.geometry("400x150")
        self.window.title("Create New User")

        self.username_frame = Label(self.window, bg="#275296")
        self.username_label = Label(self.username_frame, text="Username:   ", bg="#275296")
        self.username_entry = Entry(self.username_frame)

        self.title_frame = Frame(self.window)
        self.title_label = Label(self.title_frame,
                                 text="Type in a new username and pass word\n to create an account", bg="#275296")

        self.buttons_Frame = Frame(self.window, bg="#275296")
        self.ok_button = Button(self.buttons_Frame, bg="#275296", text="OK", width=8, command=self.user_enter)
        self.cancel_button = Button(self.buttons_Frame, bg="#275296", text="Cancel",
                                    command=self.window.destroy,  width=8, height=1)

        self.password_frame = Frame(self.window, bg="#275296")
        self.password_Label = Label(self.password_frame, text="Password:    ", bg="#275296")
        self.password_entry = Entry(self.password_frame, show="*")

        self.login_image = Image.open("images/loginimg.png")
        self.resize_login = self.login_image.resize((80, 80))
        self.login_img = ImageTk.PhotoImage(self.resize_login)
        # login = Label(window, image=login_img, bg="#275296")

        self.username_label.pack(side=LEFT)
        self.username_entry.pack(side=LEFT)

        self.password_Label.pack(side=LEFT)
        self.password_entry.pack(side=LEFT)

        # login.place(x=20, y=20)
        self.title_label.pack()

        self.title_frame.place(x=111, y=15)
        self.username_frame.place(x=110, y=50)
        self.password_frame.place(x=112, y=80)

        self.ok_button.pack(pady=6)
        self.cancel_button.pack()
        self.buttons_Frame.place(x=330, y=20)
        mainloop()

    def user_enter(self):
        username = self.username_entry.get()
        new_pass = self.password_entry.get()
        input1 = open("catlogue_database/userAndPass.txt", 'r')
        for line in input1:
            line = split(line, '-')
            if line[0] == username:
                messagebox.showinfo("Error", "UserName already taken. \nTry again")
                input1.close()
                return 0

        input1.close()
        if username != "" and new_pass != "" and len(username) > 5 and len(new_pass) > 5:
            output = open("catlogue_database/userAndPass.txt", 'a')
            output2 = open("catlogue_database/" + username + ".txt", "w")
            output2.close()
            output.write(username + "-" + new_pass + '\n')
            output.close()
            messagebox.showinfo("", "Account Created!")
            self.window.destroy()
        else:
            messagebox.showinfo("", "Error: Username and pass must be longer than 5 characters long")
            return 0
