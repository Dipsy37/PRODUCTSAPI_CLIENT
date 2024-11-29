import requests

BASE_URL = "http://127.0.0.1:8000/api/products/"

# Add a new product
def add_product():
    print("Attempting to add product...")  # Debugging print statement
    product = {
        "name": "Iphone 12 Pro Max",
        "description": " Apple iPhone 12 Pro Max smartphone. Announced Oct 2020. Features 6.7″ display, Apple A14 Bionic chipset, 3687 mAh battery, 512 GB storage, 6 GB RAM, Scratch-resistant ceramic glass.",
        "price": 80000.00
    }
    response = requests.post(BASE_URL + "create/", json=product)
    if response.status_code == 201:
        print("Product created successfully:", response.json())
    else:
        print("Failed to create product:", response.json())

# Retrieve all products
def get_products():
    print("Attempting to retrieve products...")  # Debugging print statement
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Products:", response.json())
    else:
        print("Failed to retrieve products:", response.status_code)

if __name__ == "__main__":
    print("Running client script...")
    add_product()
    get_products()