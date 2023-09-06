from tkinter import *
import sqlite3
import hashlib
import subprocess  # Import the subprocess module
from tkinter import messagebox

# Create a custom color palette
background_color = "#121212"
main_color = "#00A86B"
accent_color = "#F9A602"
text_color = "#FFFFFF"
success_color = "#007F00"
error_color = "#FF0000"

def create_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
    conn.commit()
    conn.close()

def register():
    username = entry_new_username.get()
    password = entry_new_password.get()

    # Hash the password before storing it in the database
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()

    lbl_register_status.config(text="Registration successful", fg="#007F00")  # Dark green color

def login():
    
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        stored_password = result[0]
        if hashlib.sha256(password.encode()).hexdigest() == stored_password:
            lbl_login_status.config(text="Login successful", fg="#007F00")  # Dark green color
            # Open the new interface using subprocess
            subprocess.run(["python", "main.py"])
            
        else:
            lbl_login_status.config(text="Invalid credentials", fg="#FF0000")  # Dark red color
    else:
        lbl_login_status.config(text="User not found", fg="#FF0000")  # Dark red color
    
root = Tk()
root.title("User Registration and Login")
root.geometry("400x300")
root.config(bg="#121212")  # Dark gray background

# Create users table if it doesn't exist
create_table()

root.configure(bg="#292929")  # Slightly lighter gray

# Create a styled frame for the login section
login_frame = Frame(root, bg=background_color)
login_frame.pack(pady=20)


lbl_username = Label(login_frame, text="Username:", bg=background_color, fg=text_color)
lbl_username.grid(row=0, column=0, padx=10, pady=5)
entry_username = Entry(login_frame)
entry_username.grid(row=0, column=1, padx=10, pady=5)

lbl_password = Label(login_frame, text="Password:", bg=background_color, fg=text_color)
lbl_password.grid(row=1, column=0, padx=10, pady=5)
entry_password = Entry(login_frame, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

btn_login = Button(login_frame, text="Login", command=login, bg=main_color, fg=text_color)
btn_login.grid(row=2, columnspan=2, pady=10)

lbl_login_status = Label(root, text="", bg=background_color, fg=error_color)
lbl_login_status.pack()

# Create a styled frame for the registration section
register_frame = Frame(root, bg=background_color)
register_frame.pack(pady=20)

lbl_new_username = Label(register_frame, text="New Username:", bg=background_color, fg=text_color)
lbl_new_username.grid(row=0, column=0, padx=10, pady=5)
entry_new_username = Entry(register_frame)
entry_new_username.grid(row=0, column=1, padx=10, pady=5)

lbl_new_password = Label(register_frame, text="New Password:", bg=background_color, fg=text_color)
lbl_new_password.grid(row=1, column=0, padx=10, pady=5)
entry_new_password = Entry(register_frame, show="*")
entry_new_password.grid(row=1, column=1, padx=10, pady=5)

btn_register = Button(register_frame, text="Register", command=register, bg=accent_color, fg=text_color)
btn_register.grid(row=2, columnspan=2, pady=10)

lbl_register_status = Label(root, text="", bg=background_color, fg=success_color)
lbl_register_status.pack()

root.mainloop()