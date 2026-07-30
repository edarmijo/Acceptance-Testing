
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

