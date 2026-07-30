import sys
import os


# Ensure the project root is importable (inventory.py lives there)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from behave import given, when, then
from inventory import InventoryManager


@given('the inventory is empty')
def step_inventory_empty(context):
    """Shared by: Scenario 1"""
    context.manager = InventoryManager()




@given('the inventory contains the following products:')
def step_inventory_with_products(context):
    """Shared by: Scenarios 2, 3, 4, 5"""
    context.manager = InventoryManager()
    for row in context.table:
        context.manager.add_product(
            row['ID'],
            row['Name'],
            float(row['Price']),
            int(row['Quantity']),
        )

@when('the user adds a product with ID "{product_id}" named "{name}" with price {price:f} and quantity {quantity:d}')
def step_add_product(context, product_id, name, price, quantity):
    context.output = context.manager.add_product(product_id, name, price, quantity)




@then('the inventory should contain a product named "{name}"')
def step_inventory_contains_product(context, name):
    product_names = [p.name for p in context.manager.list_products()]
    assert name in product_names, (
        f'Product "{name}" was not found in the inventory. Found: {product_names}'
    )


