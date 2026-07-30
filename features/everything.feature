Feature: Inventory Manager
  The Inventory Manager allows users to add, list, update,
  remove, and search products in their inventory.

  Scenario: Add a product to the inventory
    Given the inventory is empty
    When the user adds a product with ID "P001" named "Coffee" with price 2.50 and quantity 10
    Then the inventory should contain a product named "Coffee"

