from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import bcrypt
import subprocess

# Initialize the SQLite database
conn = sqlite3.connect('user.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS USERS(username TEXT NOT NULL, password TEXT NOT NULL)')

# Initialize the main window
window = Tk()
window.title("Sign up and Login")
window.geometry('1300x700+100+100')

# Initialize position for the frame
x = 100

# Define the function to move the top frame to the left
def move_left():
    global x
    if x > 100:
        x -= 10  # Adjust movement speed as desired
        topframe.place(x=x, y=10)
        topframe.after(50, move_left)
    headinglabel.configure(text='Sign Up')
    signintopframebutton.configure(text='Sign Up')

# Define the function to move the top frame to the right
def move_right():

    global x
    if x < 700:
        x += 10  # Adjust movement speed as desired
        topframe.place(x=x, y=10)
        topframe.after(50, move_right)
    headinglabel.configure(text='Login')
    signintopframebutton.configure(text='Login', command=login_user)

def login_user():
    if username.get() == '' or password.get() == '':
        messagebox.showwarning('Warning', 'Please fill all fields')
    else:
        cursor.execute('SELECT password FROM USERS WHERE username=?', (username.get(),))
        result_password = cursor.fetchone()

        if result_password:
            hashed_password = result_password[0]

            print("Hashed password retrieved:", hashed_password)


            if isinstance(hashed_password, str):
                hashed_password = hashed_password.encode('utf-8')


            print("Checking password...")
            if bcrypt.checkpw(password.get().encode('utf-8'), hashed_password):
                messagebox.showinfo('Success', 'Login Successful')
                window.destroy()
                subprocess.run(["python", "gamebasic.py"])  # Adjusted to correct script name
            else:
                messagebox.showerror('Error', 'Invalid Password')
        else:
            messagebox.showerror('Error', 'Invalid Username')

def reg_click():
    if username.get() == '' or password.get() == '':
        messagebox.showwarning('Warning', 'Please fill all fields')
    else:
        cursor.execute('SELECT username FROM USERS WHERE username=?', (username.get(),))
        if cursor.fetchone() is not None:  # Check if username exists
            messagebox.showwarning('Warning', 'Username already exists')
            print(f"Invalid username: {username.get()}")  # Print invalid username message
        else:
            encode_password = password.get().encode('utf-8')  # Encode the plain password
            hash_password = bcrypt.hashpw(encode_password, bcrypt.gensalt())  # Hash it
            cursor.execute('INSERT INTO USERS(username, password) VALUES(?, ?)', (username.get(), hash_password))
            conn.commit()
            messagebox.showinfo('Success', 'Registration is Successful')
            move_right()
            username.delete(0, END)
            password.delete(0, END)
            window.focus()

# Main frame
mainframe = Frame(window, bg='black', width=1300, height=630)
mainframe.grid(row=0, column=0, padx=40, pady=40)

# Login button
loginbutton = Button(mainframe, text='Login', bg='black', font=('Arial', 20, 'bold'),
                     fg='white', bd=1, activebackground='#E0115f', command=move_right)
loginbutton.place(x=1000, y=500)

# SignUp button
signinbutton = Button(mainframe, text='Sign Up', bg='black', font=('Arial', 20, 'bold'),
                      fg='white', bd=1, activebackground='#E0115f', command=move_left)
signinbutton.place(x=200, y=500)

# Top frame
topframe = Frame(window, bg='white', width=500, height=590)
topframe.place(x=x, y=10)

# Load and display the image
image = Image.open('icon.png')  # Make sure 'icon.png' is in the correct path
image = image.resize((100, 100))
image = ImageTk.PhotoImage(image)
Label(topframe, image=image, border=0, bg='white').place(x=190, y=50)

# Heading label
headinglabel = Label(topframe, text='Sign Up', font=('Arial', 24, 'bold'), bg='white', fg='blue4')
headinglabel.place(x=180, y=180)

# Username entry field
username_label = Label(topframe, text='Username', font=('Arial', 18, 'bold'), bg='white', fg='blue4')
username_label.place(x=60, y=290)

username = Entry(topframe, font=('Arial', 18), width=20)
username.place(x=200, y=290)

password_label = Label(topframe, text='Password', font=('Arial', 18, 'bold'), bg='white', fg='blue4')
password_label.place(x=60, y=380)

password = Entry(topframe, font=('Arial', 18), width=20, show='*')
password.place(x=200, y=380)

# Sign Up button inside the top frame
signintopframebutton = Button(topframe, text='Sign Up', bg='blue4', font=('Arial', 20, 'bold'),
                              fg='white', bd=1, command=reg_click)
signintopframebutton.place(x=200, y=450)

# Run the application
window.mainloop()

# Close the database connection when the application closes
conn.close()
