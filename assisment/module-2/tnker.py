import sqlite3
import tkinter as tk
from tkinter import messagebox

# Initialize the SQLite database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the customers and managers tables if they do not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        contact TEXT,
        email TEXT,
        gender TEXT,
        city TEXT,
        state TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS managers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        contact TEXT,
        email TEXT,
        gender TEXT,
        city TEXT,
        state TEXT
    )
''')

# Create the products table if it does not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL
    )
''')

# Insert sample products
sample_products = [
    ('Product 1', 'Description for product 1', 9.99),
    ('Product 2', 'Description for product 2', 19.99),
    ('Product 3', 'Description for product 3', 29.99)
]

# Check if the products table is empty before inserting
cursor.execute("SELECT COUNT(*) FROM products")
if cursor.fetchone()[0] == 0:
    cursor.executemany('''
        INSERT INTO products (name, description, price)
        VALUES (?, ?, ?)
    ''', sample_products)

conn.commit()

# Function to register a new user
def register():
    def submit_registration():
        username = entry_username.get()
        password = entry_password.get()
        contact = entry_contact.get()
        email = entry_email.get()
        gender = entry_gender.get()
        city = entry_city.get()
        state = entry_state.get()

        if role == "customer":
            cursor.execute("SELECT * FROM customers WHERE username = ?", (username,))
            if cursor.fetchone():
                messagebox.showerror("Username Exists", "Username already exists! Try a different username.")
                return
            
            cursor.execute("INSERT INTO customers (username, password, contact, email, gender, city, state) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (username, password, contact, email, gender, city, state))
        elif role == "manager":
            cursor.execute("SELECT * FROM managers WHERE username = ?", (username,))
            if cursor.fetchone():
                messagebox.showerror("Username Exists", "Username already exists! Try a different username.")
                return
            
            cursor.execute("INSERT INTO managers (username, password, contact, email, gender, city, state) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (username, password, contact, email, gender, city, state))
        
        conn.commit()
        messagebox.showinfo("Registration Successful", "Registration successful!")
        register_window.destroy()

    register_window = tk.Toplevel(root)
    register_window.title("Register")

    tk.Label(register_window, text="Username").grid(row=0, column=0)
    entry_username = tk.Entry(register_window)
    entry_username.grid(row=0, column=1)

    tk.Label(register_window, text="Password").grid(row=1, column=0)
    entry_password = tk.Entry(register_window, show='*')
    entry_password.grid(row=1, column=1)

    tk.Label(register_window, text="Contact").grid(row=2, column=0)
    entry_contact = tk.Entry(register_window)
    entry_contact.grid(row=2, column=1)

    tk.Label(register_window, text="Email").grid(row=3, column=0)
    entry_email = tk.Entry(register_window)
    entry_email.grid(row=3, column=1)

    tk.Label(register_window, text="Gender").grid(row=4, column=0)
    entry_gender = tk.Entry(register_window)
    entry_gender.grid(row=4, column=1)

    tk.Label(register_window, text="City").grid(row=5, column=0)
    entry_city = tk.Entry(register_window)
    entry_city.grid(row=5, column=1)

    tk.Label(register_window, text="State").grid(row=6, column=0)
    entry_state = tk.Entry(register_window)
    entry_state.grid(row=6, column=1)

    tk.Button(register_window, text="Submit", command=submit_registration).grid(row=7, columnspan=2)

# Function to login a user
def login():
    def submit_login():
        username = entry_username.get()
        password = entry_password.get()

        if role == "customer":
            cursor.execute("SELECT * FROM customers WHERE username = ?", (username,))
        elif role == "manager":
            cursor.execute("SELECT * FROM managers WHERE username = ?", (username,))

        user = cursor.fetchone()
        if not user:
            messagebox.showerror("Error", "Username not found! Please register first.")
            return
        if password == user[2]:
            messagebox.showinfo("Login Successful", "Login successful!")
            login_window.destroy()
            if role == 'customer':
                customer_menu(user)
            elif role == 'manager':
                manager_menu(user)
        else:
            messagebox.showerror("Error", "Incorrect password!")

    login_window = tk.Toplevel(root)
    login_window.title("Login")

    tk.Label(login_window, text="Username").grid(row=0, column=0)
    entry_username = tk.Entry(login_window)
    entry_username.grid(row=0, column=1)

    tk.Label(login_window, text="Password").grid(row=1, column=0)
    entry_password = tk.Entry(login_window, show='*')
    entry_password.grid(row=1, column=1)

    tk.Button(login_window, text="Submit", command=submit_login).grid(row=2, columnspan=2)

# Function to view all products
def view_products():
    cursor.execute("SELECT name, description, price FROM products")
    products = cursor.fetchall()

    products_window = tk.Toplevel(root)
    products_window.title("Products")

    tk.Label(products_window, text="Name").grid(row=0, column=0)
    tk.Label(products_window, text="Description").grid(row=0, column=1)
    tk.Label(products_window, text="Price").grid(row=0, column=2)

    for i, product in enumerate(products, start=1):
        tk.Label(products_window, text=product[0]).grid(row=i, column=0)
        tk.Label(products_window, text=product[1]).grid(row=i, column=1)
        tk.Label(products_window, text=f"${product[2]:.2f}").grid(row=i, column=2)

# Function to add a new product (Manager only)
def add_product():
    def submit_product():
        name = entry_name.get()
        description = entry_description.get()
        price = entry_price.get()

        try:
            price = float(price)
            cursor.execute("INSERT INTO products (name, description, price) VALUES (?, ?, ?)",
                           (name, description, price))
            conn.commit()
            messagebox.showinfo("Product Added", "Product added successfully!")
            add_product_window.destroy()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid price.")

    add_product_window = tk.Toplevel(root)
    add_product_window.title("Add Product")

    tk.Label(add_product_window, text="Name").grid(row=0, column=0)
    entry_name = tk.Entry(add_product_window)
    entry_name.grid(row=0, column=1)

    tk.Label(add_product_window, text="Description").grid(row=1, column=0)
    entry_description = tk.Entry(add_product_window)
    entry_description.grid(row=1, column=1)

    tk.Label(add_product_window, text="Price").grid(row=2, column=0)
    entry_price = tk.Entry(add_product_window)
    entry_price.grid(row=2, column=1)

    tk.Button(add_product_window, text="Submit", command=submit_product).grid(row=3, columnspan=2)

# Customer menu
def customer_menu(user):
    customer_window = tk.Toplevel(root)
    customer_window.title("Customer Menu")
    tk.Label(customer_window, text=f"Welcome {user[1]}!").pack()
    tk.Label(customer_window, text=f"Contact: {user[3]}").pack()
    tk.Label(customer_window, text=f"Email: {user[4]}").pack()
    tk.Label(customer_window, text=f"Gender: {user[5]}").pack()
    tk.Label(customer_window, text=f"City: {user[6]}").pack()
    tk.Label(customer_window, text=f"State: {user[7]}").pack()
    tk.Button(customer_window, text="View Products", command=view_products).pack()

# Manager menu
def manager_menu(user):
    manager_window = tk.Toplevel(root)
    manager_window.title("Manager Menu")
    tk.Label(manager_window, text=f"Welcome {user[1]}!").pack()
    tk.Label(manager_window, text=f"Contact: {user[3]}").pack()
    tk.Label(manager_window, text=f"Email: {user[4]}").pack()
    tk.Label(manager_window, text=f"Gender: {user[5]}").pack()
    tk.Label(manager_window, text=f"City: {user[6]}").pack()
    tk.Label(manager_window, text=f"State: {user[7]}").pack()
    tk.Button(manager_window, text="View Products", command=view_products).pack()
    tk.Button(manager_window, text="Add Product", command=add_product).pack()

# Main window
root = tk.Tk()
root.title("User Authentication System")

def choose_role():
    def set_role_customer():
        global role
        role = "customer"
        role_window.destroy()
        tk.Button(root, text="Register", command=register).pack()
        tk.Button(root, text="Login", command=login).pack()

    def set_role_manager():
        global role
        role = "manager"
        role_window.destroy()
        tk.Button(root, text="Register", command=register).pack()
        tk.Button(root, text="Login", command=login).pack()

    role_window = tk.Toplevel(root)
    role_window.title("Choose Role")
    tk.Button(role_window, text="Customer", command=set_role_customer).pack()
    tk.Button(role_window, text="Manager", command=set_role_manager).pack()

tk.Button(root, text="Choose Role", command=choose_role).pack()
tk.Button(root, text="Exit", command=root.quit).pack()

root.mainloop()

conn.close()  # Close the database connection
