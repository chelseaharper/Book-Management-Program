# Book Management UI
"""
Program to manage inventory of books.
User should be able to view amount available by title.
Should be able to view all books or see results for individual ones

Info to store:
Title, Author
Year, ISBN
Quantity, Price

User options:
View all Books
View specific book
Add Book
Update Book info
Delete Book
Close Program
"""
from cProfile import label
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#from tkinter import _ScreenUnits
import BookManagement

def clear_display():
    for item in booklist.get_children():
        booklist.delete(item)

def view_command():
    clear_display()
    for row in BookManagement.view():
        booklist.insert(parent="", index=END, iid=row[0], text="", values=row)

def delete_command():
    selected = booklist.focus()
    BookManagement.delete(selected)

def detail_open():
    selected = booklist.focus()
    detail_view(selected)

window = Tk()

window.wm_title("Book Manager")
window.geometry("700x500")

def add_command():
    add_window = Toplevel(window)
    add_window.title("Add New Book")
    add_window.geometry("700x200")

    book_name = Label(add_window, text="Title")
    book_name.grid(row=0, column=0)

    book_author = Label(add_window, text="Author")
    book_author.grid(row=0, column=2)

    book_year = Label(add_window, text="Year")
    book_year.grid(row=0, column=4)

    book_isbn = Label(add_window, text="ISBN Number")
    book_isbn.grid(row=1, column=0)

    book_quantity = Label(add_window, text="Quantity Available")
    book_quantity.grid(row=1, column=2)

    book_price = Label(add_window, text="price")
    book_price.grid(row=1, column=4)

    new_title = StringVar()
    new_title_entry = Entry(add_window, textvariable=new_title)
    new_title_entry.grid(row=0, column=1)

    new_author = StringVar()
    new_author_entry = Entry(add_window, textvariable=new_author)
    new_author_entry.grid(row=0, column=3)

    year_text = IntVar()
    year_entry = Entry(add_window, textvariable=year_text)
    year_entry.grid(row=0, column=5)

    isbn_text = IntVar()
    isbn_entry = Entry(add_window, textvariable=isbn_text)
    isbn_entry.grid(row=1, column=1)

    new_quantity = IntVar()
    new_quantity_entry = Entry(add_window, textvariable=new_quantity)
    new_quantity_entry.grid(row=1, column=3)

    price_text = DoubleVar()
    price_entry = Entry(add_window, textvariable=price_text)
    price_entry.grid(row=1, column=5)

    def insert():
        price = int(float(price_entry.get()) * 100)
        BookManagement.insert(
            new_title.get(),
            new_author.get(),
            year_text.get(),
            isbn_text.get(),
            new_quantity.get(),
            0,
            0,
            0,
            price,
            0.00
        )
        new_title_entry.delete(0, END)
        new_author_entry.delete(0, END)
        year_entry.delete(0, END)
        isbn_entry.delete(0, END)
        new_quantity_entry.delete(0, END)
        price_entry.delete(0, END)
        
        add_window.destroy()
    
    exit = Button(add_window, text="Cancel", width=8, command=add_window.destroy)
    exit.grid(row=3, column=3, padx=5)

    submit = Button(add_window, text="Submit", width=12, command=insert)
    submit.grid(row=3, column=2, padx=5)

    

def detail_view(item):
    entry = BookManagement.search(item)
    header = entry[0][1] + " publication information"
    detail_frame = LabelFrame(display_pane, text=header, padx=5, pady=5)

    def close_frame():
        display_pane.remove(detail_frame)
        display_pane.add(display_frame)
    
    def update_quantity():
        update_q = Toplevel(window)
        update_q.title("Update Quantity Information")
        update_q.geometry("500x150")

        quant1 = Label(update_q, text="Ordered Quantity: ", font="TimesNewRoman 10 bold")
        quant1.grid(row=0, column=0)
        quant3 = Label(update_q, text="Damaged Quantity: ", font="TimesNewRoman 10 bold")
        quant3.grid(row=0, column=2)
        quant5 = Label(update_q, text="Donated Quantity: ", font="TimesNewRoman 10 bold")
        quant5.grid(row=2, column=0)
        quant7 = Label(update_q, text="Available Quantity: ", font="TimesNewRoman 10 bold")
        quant7.grid(row=2, column=2)

        ord_var = IntVar()
        ord_var.set(entry[0][5])
        quant2 = Entry(update_q, textvariable=ord_var)
        quant2.grid(row=0, column=1)
        dam_var = IntVar()
        dam_var.set(entry[0][7])
        quant4 = Entry(update_q, textvariable=dam_var)
        quant4.grid(row=0, column=3)
        don_var = IntVar()
        don_var.set(entry[0][8])
        quant6 = Entry(update_q, textvariable=don_var)
        quant6.grid(row=2, column=1)
        q_avail = ord_var.get() - dam_var.get() - don_var.get()

        quant8 = Label(update_q, text=q_avail, font="TimesNewRoman 10 bold")
        quant8.grid(row=2, column=3)
        
        def quant_sub():
            BookManagement.update(
                entry[0][0],
                entry[0][1],
                entry[0][2],
                entry[0][3],
                entry[0][4],
                ord_var.get(),
                q_avail,
                dam_var.get(),
                don_var.get(),
                entry[0][9],
                entry[0][10])
            update_q.destroy()

        submit = Button(update_q, text="Submit", width=15, command=quant_sub)
        submit.grid(row=4, column=0)
        cancel = Button(update_q, text="Cancel", width=15, command=update_q.destroy)
        cancel.grid(row=4, column=2)

    def update_pub_info():
        update_pub = Toplevel(window)
        update_pub.title("Update Publicaton Information")
        update_pub.geometry("500x150")

        pub1 = Label(update_pub, text="Title: ", font="TimesNewRoman 10 bold")
        pub1.grid(row=0, column=0)
        pub3 = Label(update_pub, text="Author: ", font="TimesNewRoman 10 bold")
        pub3.grid(row=0, column=2)
        pub5 = Label(update_pub, text="Release Year: ", font="TimesNewRoman 10 bold")
        pub5.grid(row=2, column=0)
        pub7 = Label(update_pub, text="ISBN Number: ", font="TimesNewRoman 10 bold")
        pub7.grid(row=2, column=2)

        title_var = StringVar()
        title_var.set(entry[0][1])
        pub2 = Entry(update_pub, textvariable=title_var)
        pub2.grid(row=0, column=1)
        author_var = StringVar()
        author_var.set(entry[0][2])
        pub4 = Entry(update_pub, textvariable=author_var)
        pub4.grid(row=0, column=3)
        year_var = StringVar()
        year_var.set(entry[0][3])
        pub6 = Entry(update_pub, textvariable=year_var)
        pub6.grid(row=2, column=1)
        isbn_var = StringVar()
        isbn_var.set(entry[0][4])
        pub8 = Entry(update_pub, textvariable=isbn_var)
        pub8.grid(row=2, column=3)

        def pub_sub():
            BookManagement.update(
                entry[0][0],
                title_var.get(),
                author_var.get(),
                year_var.get(),
                isbn_var.get(),
                entry[0][5],
                entry[0][6],
                entry[0][7],
                entry[0][8],
                entry[0][9],
                entry[0][10])
            update_pub.destroy()

        submit = Button(update_pub, text="Submit", width=15, command=pub_sub)
        submit.grid(row=4, column=0)
        cancel = Button(update_pub, text="Cancel", width=15, command=update_pub.destroy)
        cancel.grid(row=4, column=2)

    def update_price_info():
        update_price = Toplevel(window)
        update_price.title("Update Quantity Information")
        update_price.geometry("500x150")

        price1 = Label(update_price, text="Sale Price: ", font="TimesNewRoman 10 bold")
        price1.grid(row=0, column=0)
        price3 = Label(update_price, text="Production Cost: ", font="TimesNewRoman 10 bold")
        price3.grid(row=0, column=2)

        price_var = DoubleVar()
        sale_price = float(entry[0][9])/100
        price_var.set(sale_price)
        price2 = Entry(update_price, textvariable=price_var)
        price2.grid(row=0, column=1)
        cost_var = DoubleVar()
        cost = float(entry[0][10])/100
        cost_var.set(cost)
        price4 = Entry(update_price, textvariable=cost_var)
        price4.grid(row=0, column=3)

        def price_sub():
            new_price = int(price_var.get() * 100)
            new_cost = int(cost_var.get() * 100)
            BookManagement.update(
                entry[0][0],
                entry[0][1],
                entry[0][2],
                entry[0][3],
                entry[0][4],
                entry[0][5],
                entry[0][6],
                entry[0][7],
                entry[0][8],
                new_price,
                new_cost)
            update_price.destroy()

        submit = Button(update_price, text="Submit", width=15, command=price_sub)
        submit.grid(row=4, column=0)
        cancel = Button(update_price, text="Cancel", width=15, command=update_price.destroy)
        cancel.grid(row=4, column=2)

    display_pane.remove(display_frame)
    display_pane.add(detail_frame)
    pub_frame = LabelFrame(detail_frame, text="Publication Information", padx=5, pady=5)
    quantity_frame = LabelFrame(detail_frame, text="Quantity Information", padx=5, pady=5)
    price_frame = LabelFrame(detail_frame, text="Pricing Information", padx=5, pady=5)

    pub_frame.pack(side="top", fill="both", expand=TRUE)
    quantity_frame.pack(fill="both", expand=TRUE)
    price_frame.pack(side="bottom", fill="both", expand=TRUE)

#Publication Frame Content
    pub1 = Label(pub_frame, text="Title: ", font="TimesNewRoman 10 bold")
    pub1.grid(row=0, column=0)
    pub2 = Label(pub_frame, text=entry[0][1])
    pub2.grid(row=0, column=1)
    pub3 = Label(pub_frame, text="Author: ", font="TimesNewRoman 10 bold")
    pub3.grid(row=0, column=2)
    pub4 = Label(pub_frame, text=entry[0][2])
    pub4.grid(row=0, column=3)
    pub5 = Label(pub_frame, text="Release Year: ", font="TimesNewRoman 10 bold")
    pub5.grid(row=2, column=0)
    pub6 = Label(pub_frame, text=entry[0][3])
    pub6.grid(row=2, column=1)
    pub7 = Label(pub_frame, text="ISBN Number: ", font="TimesNewRoman 10 bold")
    pub7.grid(row=2, column=2)
    pub8 = Label(pub_frame, text=entry[0][4])
    pub8.grid(row=2, column=3)
    pub9 = Label(pub_frame, text="")
    pub9.grid(row=3, column=3)

    update_pub_button = Button(pub_frame, text="Update Info", width=15, command=update_pub_info)
    update_pub_button.grid(row=4, column=0)

#Quantity Frame Content
    q_avail = entry[0][5]-entry[0][7]-entry[0][8]
    q1 = Label(quantity_frame, text="Ordered Quantity: ", font="TimesNewRoman 10 bold")
    q1.grid(row=0, column=0)
    q2 = Label(quantity_frame, text=entry[0][5])
    q2.grid(row=0, column=1)
    q3 = Label(quantity_frame, text="Damaged Quantity: ", font="TimesNewRoman 10 bold")
    q3.grid(row=0, column=2)
    q4 = Label(quantity_frame, text=entry[0][7])
    q4.grid(row=0, column=3)
    q5 = Label(quantity_frame, text="Donated Quantity: ", font="TimesNewRoman 10 bold")
    q5.grid(row=1, column=0)
    q6 = Label(quantity_frame, text=entry[0][8])
    q6.grid(row=1, column=1)
    q7 = Label(quantity_frame, text="Available Quantity: ", font="TimesNewRoman 10 bold")
    q7.grid(row=1, column=2)
    q8 = Label(quantity_frame, text=q_avail)
    q8.grid(row=1, column=3)
    q9 = Label(quantity_frame, text="")
    q9.grid(row=2, column=3)
    
    update_q_button = Button(quantity_frame, text="Update Quantities", width=15, command=update_quantity)
    update_q_button.grid(row=3, column=0)

# Pricing Frame Content
    p1 = Label(price_frame, text="Sale Price: ", font="TimesNewRoman 10 bold")
    p1.grid(row=0, column=0)
    sale_price = float(entry[0][9])/100
    p2 = Label(price_frame, text=str(sale_price))
    p2.grid(row=0, column=1)
    p3 = Label(price_frame, text="Production Cost: ", font="TimesNewRoman 10 bold")
    p3.grid(row=0, column=2)
    prod_cost = float(entry[0][10])/100
    p4 = Label(price_frame, text=str(prod_cost))
    p4.grid(row=0, column=3)
    p5 = Label(price_frame, text="")
    p5.grid(row=1, column=3)

    update_price_button = Button(price_frame, text="Update Pricing", width=15, command=update_price_info)
    update_price_button.grid(row=2, column=0)
    close_detail = Button(price_frame, text="Close View", width=15, command=close_frame)
    close_detail.grid(row=2, column=2)


base_pane = PanedWindow(bd=4, relief="raised")
base_pane.pack(fill=BOTH, expand=1)

display_pane = PanedWindow(base_pane, orient=VERTICAL, bd=4, relief="sunken", width=575, height=475)
base_pane.add(display_pane)

entry_frame = LabelFrame(display_pane, text="", padx=5, pady=5)
display_frame = LabelFrame(display_pane, text="", padx=5, pady=5)
button_frame = LabelFrame(base_pane, text="", padx=5, pady=5)


base_pane.add(button_frame)
display_pane.add(entry_frame)
display_pane.add(display_frame)

l1 = Label(entry_frame, text="Title")
l1.grid(row=0, column=0)

l2 = Label(entry_frame, text="Author")
l2.grid(row=0, column=2)

l3 = Label(entry_frame, text="Quantity")
l3.grid(row=0, column=4)

entry_frame.columnconfigure(0, weight=0)
entry_frame.columnconfigure(1, weight=3)
entry_frame.columnconfigure(2, weight=0)
entry_frame.columnconfigure(3, weight=2)
entry_frame.columnconfigure(4, weight=0)
entry_frame.columnconfigure(5, weight=1)
button_frame.columnconfigure(1, weight=1)

title_text = StringVar()
e1 = Entry(entry_frame, textvariable=title_text, width=10)
e1.grid(row=0, column=1, sticky=EW)

author_text = StringVar()
e2 = Entry(entry_frame, textvariable=author_text, width=10)
e2.grid(row=0, column=3, sticky=EW)

quantity_text = StringVar()
e3 = Entry(entry_frame, textvariable=quantity_text, width=5)
e3.grid(row=0, column=5, sticky=EW)

books_font = ("Times", "12")
columns = ("ID", "Title", "Author", "Quantity")
style = ttk.Style()
style.configure("myStyle.Treeview", bd=0, font=books_font)
style.configure("myStyle.Treeview.Heading", font=books_font)
style.layout("myStyle.Treeview", [("myStyle.Treeview.treearea",{"sticky": "nswe"})])

booklist = ttk.Treeview(display_frame, style="myStyle.Treeview", columns=columns, show="headings")
booklist.column("#0", width=0, stretch=NO)
booklist.column("ID", anchor=W, width=40, minwidth=25)
booklist.column("Title", anchor=W, width=180, minwidth=25)
booklist.column("Author", anchor=W, width=120, minwidth=25)
booklist.column("Quantity", anchor=W, width=40, minwidth=25)
booklist.heading("#0", text="", anchor=W)
booklist.heading("ID", text="ID", anchor=W)
booklist.heading("Title", text="Title", anchor=W)
booklist.heading("Author", text="Author", anchor=W)
booklist.heading("Quantity", text="Quantity", anchor=W)
booklist.pack(side="left", fill="both", expand=TRUE)
booklist["selectmode"] = "browse"

scroller = Scrollbar(display_frame, orient="vertical")
scroller.pack(side="right", fill="y")

booklist.configure(yscrollcommand=scroller.set)
scroller.configure(command=booklist.yview)

b1 = Button(button_frame, text="View books", width=12, command=view_command)
b1.grid(row=2, column=1, padx=5, sticky=EW)

b2 = Button(button_frame, text="Detail View", width=12, command=detail_open)
b2.grid(row=3, column=1, padx=5, sticky=EW)

b3 = Button(button_frame, text="Add book", width=12, command=add_command)
b3.grid(row=4, column=1, padx=5, sticky=EW)

b5 = Button(button_frame, text="Delete book", width=12, command=delete_command)
b5.grid(row=6, column=1, padx=5, sticky=EW)

b7 = Button(button_frame, text="Close program", width=12, command=window.destroy)
b7.grid(row=8, column=1, padx=5, sticky=EW)

window.mainloop()