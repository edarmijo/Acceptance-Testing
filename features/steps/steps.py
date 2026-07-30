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


@when('the user lists all products')
def step_list_all_products(context):
    context.products = context.manager.list_products()



@then('the output should contain "{name}"')
def step_output_contains(context, name):
    product_names = [p.name for p in context.products]
    assert name in product_names, (
        f'"{name}" was not found in the product list. Found: {product_names}'
    )

@when('the user updates the quantity of "{name}" to {new_quantity:d}')
def step_update_quantity(context, name, new_quantity):
    context.output = context.manager.update_quantity(name, new_quantity)


@then('the inventory should show product "{name}" with quantity {expected_quantity:d}')
def step_check_product_quantity(context, name, expected_quantity):
    for product in context.manager.list_products():
        if product.name == name:
            assert product.quantity == expected_quantity, (
                f'Expected quantity {expected_quantity} for "{name}" '
                f'but got {product.quantity}'
            )
            return
    assert False, f'Product "{name}" was not found in the inventory'


@when('the user removes the product "{name}"')
def step_remove_product(context, name):
    context.output = context.manager.remove_product(name)




@then('the inventory should not contain "{name}"')
def step_inventory_not_contains(context, name):
    product_names = [p.name for p in context.manager.list_products()]
    assert name not in product_names, (
        f'Product "{name}" was found in the inventory but should have been removed'
    )


@when('the user searches for products with keyword "{keyword}"')
def step_search_products(context, keyword):
    context.search_results = context.manager.search_product(keyword)




@then('the search results should contain {expected_count:d} products')
def step_search_result_count(context, expected_count):
    actual_count = len(context.search_results)
    assert actual_count == expected_count, (
        f'Expected {expected_count} search result(s) but got {actual_count}'
    )




@then('the search results should include "{name}"')
def step_search_results_include(context, name):
    result_names = [p.name for p in context.search_results]
    assert name in result_names, (
        f'"{name}" was not found in search results. Found: {result_names}'
    )
