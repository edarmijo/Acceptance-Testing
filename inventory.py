
class Product:
    def __init__(self, product_id: str, name: str, price: float, quantity: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"ID: {self.product_id} | Name: {self.name} | Price: ${self.price:.2f} | Quantity: {self.quantity}"

class InventoryManager:
    def __init__(self):
        self.inventory = {}

    #First Requirement
    def add_product(self, product_id: str, name: str, price: float, quantity: int) -> str:
        """Requirement 1: Add a new product to the inventory"""
        if product_id in self.inventory:
            return f"Error: Product with ID '{product_id}' already exists."
        
        for item in self.inventory.values():
            if item.name.lower() == name.lower():
                return f"Error: Product '{name}' already exists."

        self.inventory[product_id] = Product(product_id, name, price, quantity)
        return f"Product '{name}' added successfully."

    def list_products(self) -> list:
            """Requirement 2: List all the products in the inventory"""
            return list(self.inventory.values())

    def update_quantity(self, name_or_id: str, new_quantity: int) -> str:
        """Requirement 3: Update the quantity of a product"""
        product = self._find_product(name_or_id)
        if product:
            product.quantity = new_quantity
            return f"Updated quantity for '{product.name}' to {new_quantity}."
        return f"Product '{name_or_id}' was not found."

    def remove_product(self, name_or_id: str) -> str:
        """Requirement 4: Remove a product from the inventory"""
        product = self._find_product(name_or_id)
        if product:
            del self.inventory[product.product_id]
            return f"Product '{product.name}' was removed."
        return f"Product '{name_or_id}' was not found."
    
    def search_product(self, name_query: str) -> list:
        """Requirement 5 (Added Feature): Search product by name keyword"""
        results = [
            prod for prod in self.inventory.values() 
            if name_query.lower() in prod.name.lower()
        ]
        return results

    def _find_product(self, name_or_id: str):
        """Helper function to look up products by ID or Name"""
        if name_or_id in self.inventory:
            return self.inventory[name_or_id]
        for product in self.inventory.values():
            if product.name.lower() == name_or_id.lower():
                return product
        return None
