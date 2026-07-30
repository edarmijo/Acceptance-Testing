Feature: Inventory Manager
  The Inventory Manager allows users to add, list, update,
  remove, and search products in their inventory.

  Scenario: Add a product to the inventory
    Given the inventory is empty
    When the user adds a product with ID "P001" named "Coffee" with price 2.50 and quantity 10
    Then the inventory should contain a product named "Coffee"

  Scenario: List all products in the inventory
    Given the inventory contains the following products:
      | ID   | Name   | Price | Quantity |
      | P001 | Coffee | 2.50  | 10       |
      | P002 | Sugar  | 1.20  | 5        |
    When the user lists all products
    Then the output should contain "Coffee"
    And the output should contain "Sugar"
