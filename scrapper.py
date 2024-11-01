# scraper.py
import requests
import pandas as pd

# Using JSONPlaceholder as the base URL for this example
BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_data(endpoint):
    """Fetch data from a specified endpoint."""
    response = requests.get(f"{BASE_URL}/{endpoint}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {endpoint}. Status code: {response.status_code}")
        return []

def save_to_csv(data, filename):
    """Save list of dictionaries to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(f"data/{filename}.csv", index=False)
    print(f"Data saved to data/{filename}.csv")

# Update functions to use relevant endpoint names
def scrape_users():
    users = fetch_data("users")  # JSONPlaceholder provides a /users endpoint
    save_to_csv(users, "users")

def scrape_products():
    products = fetch_data("posts")  # Using /posts as a stand-in for products
    save_to_csv(products, "products")

def scrape_orders():
    orders = fetch_data("comments")  # Using /comments as a stand-in for orders
    save_to_csv(orders, "orders")
