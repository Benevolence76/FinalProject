from tkinter import *
import sqlite3
import hashlib

def create_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
    conn.commit()
    conn.close()

def register_success():
    lbl_register_status.config(text="Registration successful", fg="#007F00")  # Dark green color
    login_window.deiconify()  # Show the login window after registration

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

    register_success()


# Main application window
root = Tk()
root.title("User Registration")
root.geometry("400x300")
root.config(bg="#121212")  # Dark gray background

# Create users table if it doesn't exist
create_table()

lbl_new_username = Label(root, text="New Username:", bg="#292929", fg="#FFFFFF")  # White text
lbl_new_username.pack()
entry_new_username = Entry(root)
entry_new_username.pack()

lbl_new_password = Label(root, text="New Password:", bg="#292929", fg="#FFFFFF")  # White text
lbl_new_password.pack()
entry_new_password = Entry(root, show="*")
entry_new_password.pack()

btn_register = Button(root, text="Register", command=register, bg="#F9A602", fg="#FFFFFF")  # Orange button
btn_register.pack()

lbl_register_status = Label(root, text="", bg="#292929", fg="#007F00")  # Dark green text
lbl_register_status.pack()

# Login window


# Your login interface components go here, similar to the original code

# Start the main event loop
root.mainloop()
