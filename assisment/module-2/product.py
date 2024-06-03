import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="ProductManagement"
    )

def register_customer(name, contact, email, gender, city, state):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = "INSERT INTO Customers (name, contact, email, gender, city, state) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (name, contact, email, gender, city, state))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", "Customer registered successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

def on_register():
    name = entry_name.get()
    contact = entry_contact.get()
    email = entry_email.get()
    gender = gender_var.get()
    city = entry_city.get()
    state = entry_state.get()

    if not (name and contact and email and gender and city and state):
        messagebox.showerror("Error", "All fields are required!")
        return

    register_customer(name, contact, email, gender, city, state)

# Tkinter GUI
app = tk.Tk()
app.title("Registration Form")

tk.Label(app, text="Name").grid(row=0, column=0)
tk.Label(app, text="Contact").grid(row=1, column=0)
tk.Label(app, text="Email").grid(row=2, column=0)
tk.Label(app, text="Gender").grid(row=3, column=0)
tk.Label(app, text="City").grid(row=4, column=0)
tk.Label(app, text="State").grid(row=5, column=0)

entry_name = tk.Entry(app)
entry_contact = tk.Entry(app)
entry_email = tk.Entry(app)

gender_var = tk.StringVar()
tk.Radiobutton(app, text="Male", variable=gender_var, value="Male").grid(row=3, column=1)
tk.Radiobutton(app, text="Female", variable=gender_var, value="Female").grid(row=3, column=2)

entry_city = tk.Entry(app)
entry_state = tk.Entry(app)

entry_name.grid(row=0, column=1)
entry_contact.grid(row=1, column=1)
entry_email.grid(row=2, column=1)
entry_city.grid(row=4, column=1)
entry_state.grid(row=5, column=1)

tk.Button(app, text="Register", command=on_register).grid(row=6, columnspan=3)

app.mainloop()
