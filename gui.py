# gui.py
import tkinter as tk
from scraper import scrape_users, scrape_products, scrape_orders

def run_scraper(scrape_function, label):
    """Run a scraper function and update label."""
    scrape_function()
    label.config(text="Data Scraped Successfully")

def setup_gui():
    root = tk.Tk()
    root.title("Web Scraper")

    # Labels and buttons
    tk.Label(root, text="Select Data to Scrape:").pack(pady=10)

    users_label = tk.Label(root, text="")
    users_button = tk.Button(root, text="Scrape Users", 
                             command=lambda: run_scraper(scrape_users, users_label))
    users_button.pack(pady=5)
    users_label.pack()

    products_label = tk.Label(root, text="")
    products_button = tk.Button(root, text="Scrape Products", 
                                command=lambda: run_scraper(scrape_products, products_label))
    products_button.pack(pady=5)
    products_label.pack()

    orders_label = tk.Label(root, text="")
    orders_button = tk.Button(root, text="Scrape Orders", 
                              command=lambda: run_scraper(scrape_orders, orders_label))
    orders_button.pack(pady=5)
    orders_label.pack()

    root.mainloop()
