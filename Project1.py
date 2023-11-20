from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from datetime import datetime
from tkinter import ttk
from stringmanip import split, cap_First_Letter
from time import strftime

class BookCatalogue:
    def __init__(self):
        # creating the window
        self.wn = Tk()
        self.wn.title("Book Catalogue")
        self.wn.geometry("500x400")
        self.wn.configure(bg="#3c64a3")
        self.frame1 = Frame(self.wn, bg="#3c64a3")

        self.user

        self.big_frame3 = Frame(self.wn, bg="#3c64a3")
        self.frame8 = Frame(self.big_frame3, bg="#3c64a3")
        self.frame9 = Frame(self.big_frame3, bg="#3c64a3")
        self.frame10 = Frame(self.big_frame3, bg="#3c64a3")

        self.count_frame = Frame(self.wn, bg="#3c64a3")
        self.enter_frame = Frame(self.wn, bg="#3c64a3")
        self.search_date_frame = Frame(self.wn, bg="#3c64a3")
        self.search_frame = Frame(self.wn, bg="#3c64a3")
        self.display_frame = Frame(self.wn, bg="#3c64a3")


        self.search_frame.place(x=10,y=10)
        self.enter_frame.place(x=10, y=90)
        self.search_date_frame.place(x=10, y=185)
        self.display_frame.place(x=10, y=275)
        self.count_frame.place(x=90, y=10)


        # check buttons
        self.var1 = IntVar()
        self.var2 = IntVar()

        # scale
        self.x = IntVar()
        self.x2 = IntVar()

        # images
        self.search_image = Image.open("images/search_img.png")
        self.resize_search = self.search_image.resize((20, 20))
        self.search_img = ImageTk.PhotoImage(self.resize_search)

        self.display_image = Image.open("images/display.png")
        self.resize_display = self.display_image.resize((50, 50))
        self.display_img = ImageTk.PhotoImage(self.resize_display)

        self.count_image = Image.open("images/count.png")
        self.resize_count = self.count_image.resize((40, 40))
        self.count_img = ImageTk.PhotoImage(self.resize_count)

        self.searcho_image = Image.open("images/search.png")
        self.resize_searcho = self.searcho_image.resize((53, 53))
        self.searcho_img = ImageTk.PhotoImage(self.resize_searcho)

        self.entery_image = Image.open("images/enter.png")
        self.resize_entery = self.entery_image.resize((50, 50))
        self.entery_img = ImageTk.PhotoImage(self.resize_entery)

        self.date_image = Image.open("images/date.png")
        self.resize_date = self.date_image.resize((50, 50))
        self.date_img = ImageTk.PhotoImage(self.resize_date)

        self.bar_image = Image.open("images/bottombar.png")
        self.resize_bar = self.bar_image.resize((500, 30))
        self.bar_img = ImageTk.PhotoImage(self.resize_bar)

        self.logo_image = Image.open("images/logo.png")
        self.logo_bar = self.logo_image.resize((200, 173))
        self.logo_img = ImageTk.PhotoImage(self.logo_bar)

        self.logo = Label(self.wn, image=self.logo_img, bg="#3c64a3")
        self.logo.place(x=200, y=110)


        # radio buttons
        self.v = IntVar()
        self.v.set(1)

        self.bottom_bar = Label(self.wn, image=self.bar_img).place(x=0, y=365)

        # main window big frame 1
        self.search_button_mw = Button(self.search_frame, image=self.searcho_img, command=self.new_window_search,
                                       borderwidth=0, bg="#3c64a3").pack()
        self.enter_label = Label(self.search_frame, text="Search", font=("MS Sans Serif", 10), bg="#3c64a3").pack()

        self.enter_button_mw = Button(self.enter_frame, image=self.entery_img, command=self.new_window_enter,
                                      borderwidth=0, bg="#3c64a3").pack()
        self.search_label = Label(self.enter_frame, bg="#3c64a3", text="Enter a\nnew book",
                                  font=("MS Sans Serif", 10)).pack()

        self.date_search_button_mw = Button(self.search_date_frame, image=self.date_img,
                                            command=self.new_window_search_by_date, bg="#3c64a3", borderwidth=0).pack()
        self.search_date_label = Label(self.search_date_frame, text="Search\n by date", font=("MS Sans Serif", 10),
                                       bg="#3c64a3").pack()

        # frame 8
        self.count_button = Button(self.count_frame, text="Go", fg="black", command=self.count_list
                                   , image=self.count_img, bg="#3c64a3", borderwidth=0).pack()
        self.count_label = Label(self.count_frame, text="Count\ncatalogue", bg="#3c64a3", fg="black",
                                 font=("MS Sans Serif", 10)).pack()

        self.display_button = Button(self.display_frame, text="Go", fg="black", command=self.new_window_dispay
                                     , image=self.display_img, bg="#3c64a3", borderwidth=0).pack()
        self.display_label = Label(self.display_frame, text="Display\n catalogue", bg="#3c64a3", fg="black",
                                   font=("MS Sans Serif", 10)).pack()

        # clock
        def time():
            string = strftime('%H:%M')
            self.clock.config(text=string)
            self.clock.after(1000, time)
        self.clock = Label(self.wn, font=("ariel", 10), bg='#C0C0C0', fg='black')
        self.clock.place(x=450, y=370)
        time()

        self.wn.mainloop()

    def search_date(self):
        file_input = open("catlogue_database/" + self.user + ".txt", "r")
        key_year = self.x.get()
        key_month = self.x2.get()
        line = []
        title_list = []
        for i in file_input:
            line = i.split("-")
            year = line[3]
            month = line[4]
            if int(year) == int(key_year) and int(month) == int(key_month):
                title_list.append(line[0])

        return title_list

    def search_date_command(self):
        result = self.search_date()
        if result != []:
            display = "The books that were entered in this month and year are:"
            for i in result:
                display += " " + cap_First_Letter(i) + '\n'
            messagebox.showinfo("Search by date", display)
        else:
            messagebox.showinfo("Search by date", "No title in catalogue with that date")


    def search(self):
        file_input = open("catlogue_database/" + self.user + ".txt", "r")
        key = self.search_entry.get()
        key = key.upper()
        books = []
        line = []
        for i in file_input:
            line = i.split("-")
            author = line[2]
            aborb = line[1]
            title = line[0]
            if key == title:
                return author, title, aborb
            elif key == author:
                books.append(title)
        if len(books) == 0:
            return "search not found", "", ""
        else:
            return key, books, aborb

    def search_button_command(self):
        aOrT = int(self.v.get())  # search by author is 1 and search by title is 2
        author, title, book = self.search()
        if aOrT == 1 and title != "":
            display = cap_First_Letter(author) + " wrote: \n"
            for i in title:
                display += cap_First_Letter(i) + '\n'
            messagebox.showinfo("", display)
        elif aOrT == 2 and title != "":
            display = "The author of " + cap_First_Letter(title) + " is " + cap_First_Letter(author)
            messagebox.showinfo("", display)
        else:
            messagebox.showinfo("", author)

    def enter_books(self):
        entry_list = []
        author = self.enter_entry2.get()
        title = self.enter_entry1.get()
        book = self.var1.get()
        ab = self.var2.get()
        date = str(datetime.today().strftime('%Y-%m-%d'))
        date = split(date, '-')
        if author == "":
            messagebox.showinfo("Enter book", "ERROR! Must enter an author.")
            return 0
        if title == "":
            messagebox.showinfo("Enter book", "ERROR! Must enter a title.")
            return 0
        output = open("catlogue_database/" + self.user + ".txt", "a")

        if book == 0 and ab == 0:
            messagebox.showinfo("Enter book", " ERROR! Must select at least one of the 2 choices.")
            return 0
        elif ab == 1 and book == 1:
            entry_list.append(title.upper() + "-" "AUDIOBOOK/BOOK" "-" + author.upper()
                              + "-" + date[0] + "-" + date[1] + '\n')
            # adding the new book
        elif ab == 1 and book == 0:
            entry_list.append(
                title.upper() + "-" "AUDIOBOOK" + "-" + author.upper() + "-" + date[0] + "-" + date[1] + '\n')
        elif ab == 0 and book == 1:
            entry_list.append(title.upper() + "-" "BOOK" + "-" + author.upper() + "-" + date[0] + "-" + date[1] + '\n')

        messagebox.showinfo("Enter book", "This book has been added to the file.")
        for i in entry_list:
            # done this way in order to enter multiple books at once without the
            # need to restart the gui each time the user wants to enter a new book
            output.write(i)
        output.close()

    def count_list(self):
        input1 = open("catlogue_database/" + self.user + ".txt")
        count = 0
        for i in input1:
            count += 1
        input1.close()
        if count == 1:
            display = "There is only 1 book in the catalogue"
        else:
            display = "There are " + str(count) + " books in the catalogue"
        messagebox.showinfo("books in list", display)

    def new_window_dispay(self):
        window = Toplevel()
        window.geometry('1000x400')
        window.configure(bg="#3c64a3")
        display_label = Label(window, text="Books in Catalogue", bg="#3c64a3")
        display_label.pack()

        myscroll = ttk.Scrollbar(window)
        myscroll.pack(side=RIGHT, fill=BOTH)
        file = open("catlogue_database/" + self.user + ".txt")
        text = Text(window, width=15, height=15, wrap=CHAR, yscrollcommand=myscroll.set)
        for i in file:
            line = i.split("-")
            text.insert(END,line)
        text.pack(side=TOP, fill=X)

        myscroll.config(command=text.yview)

    def new_window_search(self):
        window = Toplevel()
        window.configure(bg="#3c64a3")
        window.geometry('250x250')
        big_frame1 = Frame(window, bg="#3c64a3")

        frame1 = Frame(big_frame1, bg="#3c64a3")
        frame2 = Frame(big_frame1, bg="#3c64a3")
        frame3 = Frame(big_frame1, bg="#3c64a3")

        # frame1
        search_label = Label( frame1, text="Search", bg="#3c64a3", fg="black", font=("ariel", 18))
        self.search_entry = Entry(frame1, bg="white", fg="black")

        # frame2
        author_box = Radiobutton( frame2, text="search by title", fg="black", variable=self.v,
                                      value=2, indicatoron=False, bg="#3c64a3", width=13)
        title_box = Radiobutton( frame2, text="search by author", fg="black", variable=self.v,
                                     value=1, indicatoron=False, bg="#3c64a3", width=13)
        # frame3
        search_button = Button( frame3, text="ENTER", fg="black",
                                    command=self.search_button_command, image=self.search_img,
                                bg="#3c64a3", width=20)

        search_label.pack()
        self.search_entry.pack(side="left")
        author_box.pack(side="left")
        title_box.pack(side="left")
        search_button.pack()

        frame1.pack()
        frame2.pack()
        frame3.pack()

        big_frame1.pack(side="left")

    def new_window_enter(self):
        enter_window = Toplevel()
        enter_window.configure(bg="#3c64a3")
        enter_window.geometry('250x250')
        self.big_frame2 = Frame(enter_window, bg="#3c64a3")
        self.big_frame2.pack(side="left")
        self.frame11 = Frame(self.big_frame2, bg="#3c64a3")
        self.frame4 = Frame(self.big_frame2, bg="#3c64a3")
        self.frame5 = Frame(self.big_frame2, bg="#3c64a3")
        self.frame6 = Frame(self.big_frame2, bg="#3c64a3")
        self.frame7 = Frame(self.big_frame2, bg="#3c64a3")

        self.entry_author_label = Label(self.frame4, text="Author:  ", bg="#3c64a3", fg="black", )
        self.enter_entry2 = Entry(self.frame4, text="", bg="white", fg="black")

        self.entry_Title_label = Label(self.frame5, text="Title:       ", bg="#3c64a3", fg="black")
        self.enter_entry1 = Entry(self.frame5, text="", bg="white", fg="black")

        self.aborb_label1 = Label(self.frame6, text="AudioBook:   ", bg="#3c64a3", fg="black")
        self.aborb_label2 = Label(self.frame6, text="Book:    ", bg="#3c64a3", fg="black")
        self.audio_box = Checkbutton(self.frame6, bg="#3c64a3", fg="black", variable=self.var1)
        self.book_box = Checkbutton(self.frame6, bg="#3c64a3", fg="black", variable=self.var2)
        self.enter_button = Button(self.frame7, text="ENTER", fg="black",
                                   command=self.enter_books, bg="#3c64a3", width=8)
        self.enter_label = Label(self.frame11, text="Enter new book", font=("ariel", 18), bg="#3c64a3")
        self.frame11.pack()
        self.frame5.pack()
        self.frame4.pack()
        self.frame6.pack()
        self.frame7.pack()

        self.enter_label.pack(side="left")
        self.entry_author_label.pack(side="left")
        self.entry_Title_label.pack(side="left")
        self.enter_entry1.pack(side="left")
        self.enter_entry2.pack(side="left")
        self.aborb_label2.pack(side="left")
        self.audio_box.pack(side="left")
        self.aborb_label1.pack(side="left")
        self.book_box.pack(side="left")
        self.enter_button.pack()

    def new_window_search_by_date(self):
        date_search_window = Toplevel()
        date_search_window.configure(bg="#3c64a3")
        date_search_window.geometry('250x250')

        self.big_frame4 = Frame(date_search_window, bg="#3c64a3")
        self.big_frame5 = Frame(date_search_window, bg='#3c64a3')

        self.frame12 = Frame(self.big_frame4, bg="#3c64a3")
        self.frame13 = Frame(self.big_frame4, bg="#3c64a3", pady=20)
        self.frame14 = Frame(self.big_frame4, bg="#3c64a3")
        self.frame15 = Frame(self.big_frame4, bg="#3c64a3")
        self.frame16 = Frame(self.big_frame5, bg="#3c64a3")

        # sliders Frame 12
        self.year_label = Label(self.frame12, text="Year:   ", bg="#3c64a3", padx=17)
        self.year_scale = Scale(self.frame12, orient="horizontal", bg="white", variable=self.x,
                                to=2021, from_=1980)

        self.month_label = Label(self.frame13, text="Month:   ", bg="#3c64a3", padx=11)
        self.month_scale = Scale(self.frame13, orient="horizontal", bg="white", variable=self.x2, to=12, from_=1)
        self.search_button_date = Button(self.frame15, text="ENTER", fg="black",
                                         command=self.search_date_command, image=self.search_img,
                                         bg="#3c64a3", width=50)

        self.date_title_frame = Frame(date_search_window, bg="#3c64a3")
        self.date_title_label = Label(self.date_title_frame, bg="#3c64a3", text="Enter date:",
                                      font=("MS Sans Serif", 30))


        self.date_title_frame.pack()
        self.date_title_label.pack()
        self.year_label.pack(side="left")
        self.year_scale.pack(side="left")
        self.month_label.pack(side="left")
        self.month_scale.pack(side="left")
        self.search_button_date.pack(side="left")

        self.frame14.pack()
        self.frame12.pack()
        self.frame13.pack()
        self.frame15.pack()
        self.frame16.pack()

        self.big_frame4.pack(side="left")
        self.big_frame5.pack(side="left")