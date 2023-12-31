from tkinter import *

app = Tk()
app.resizable(False, False)
app.title("Main Window")
app['bg'] = '#23232b'
app.geometry("600x400")

text_var = StringVar()

def function():
	lbl1["text"] = ent.get()

def clear_func():
	ent.delete(0, END)
	lbl1["text"] = ""

# App Name
lbl = Label(app, text='Simple Python App', bg='#23232b', fg='#ffffff', pady='8', font=('Montserrat Bold', 25))
lbl.pack()

# Input Text
ent = Entry(app, text='', font=('Montserrat Bold', 20))
ent.pack(pady='8')

# Display Text
btn = Button(app, text='Display Text', width='15', height='2', command=function, font=('Montserrat Bold', 15))
btn.pack(pady='8')

# Clear Text
btn1 = Button(app, text='Clear', width='10', height='1', command=clear_func, font=('Montserrat Bold', 15))
btn1.pack(pady='8')

# Display Text
lbl1 = Label(app, text='', bg='#23232b', fg='#ffffff', font=('Montserrat Bold', 20))
lbl1.pack(pady='8')

app.mainloop()

