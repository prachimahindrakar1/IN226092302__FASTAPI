from fastapi import FastAPI

app = FastAPI()

# Product List
products = [
    {
        "id": 1,
        "name": "Pen",
        "price": 20,
        "category": "Stationery",
        "in_stock": True
    },
    {
        "id": 2,
        "name": "Notebook",
        "price": 80,
        "category": "Stationery",
        "in_stock": True
    },
    {
        "id": 3,
        "name": "Wireless Mouse",
        "price": 799,
        "category": "Electronics",
        "in_stock": True
    },
    {
        "id": 4,
        "name": "Desk Lamp",
        "price": 999,
        "category": "Electronics",
        "in_stock": False
    },
    {
        "id": 5,
        "name": "Laptop Stand",
        "price": 1299,
        "category": "Electronics",
        "in_stock": True
    },
    {
        "id": 6,
        "name": "Mechanical Keyboard",
        "price": 2499,
        "category": "Electronics",
        "in_stock": True
    },
    {
        "id": 7,
        "name": "Webcam",
        "price": 1899,
        "category": "Electronics",
        "in_stock": False
    }
]

# Root Endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Assignment"}

# Get all products
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }

# Get products by category
@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]

    if not result:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": result,
        "total": len(result)
    }

# Get only in-stock products
@app.get("/products/instock")
def get_instock():
    available = [p for p in products if p["in_stock"] == True]

    return {
        "in_stock_products": available,
        "count": len(available)
    }

# Store summary
@app.get("/store/summary")
def store_summary():
    in_stock_count = len([p for p in products if p["in_stock"]])
    out_stock_count = len(products) - in_stock_count
    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": len(products),
        "in_stock": in_stock_count,
        "out_of_stock": out_stock_count,
        "categories": categories
    }

# Search products
@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    results = [
        p for p in products
        if keyword.lower() in p["name"].lower()
    ]

    if not results:
        return {"message": "No products matched your search"}

    return {
        "matches": results,
        "total": len(results)
    }
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):

    result = [p for p in products if p["category"] == category_name]

    if not result:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": result,
        "total": len(result)
    }
@app.get("/products/instock")
def get_instock_products():

    available_products = [p for p in products if p["in_stock"] == True]

    return {
        "in_stock_products": available_products,
        "count": len(available_products)
    }
@app.get("/store/summary")
def store_summary():

    in_stock_count = len([p for p in products if p["in_stock"]])
    out_of_stock_count = len(products) - in_stock_count
    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": len(products),
        "in_stock_products": in_stock_count,
        "out_of_stock_products": out_of_stock_count,
        "categories": categories
    }
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    results = [
        p for p in products
        if keyword.lower() in p["name"].lower()
    ]

    if not results:
        return {"message": "No products matched your search"}

    return {
        "matches": results,
        "total_matches": len(results)
    }