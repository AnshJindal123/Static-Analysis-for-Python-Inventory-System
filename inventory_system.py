"""
A simple inventory management system with functionality to add, remove,
and track stock levels for items while allowing report generation.
"""

import json
from datetime import datetime


class InventorySystem:
    """Manages stock data, logging, and persistence for inventory items."""

    def __init__(self):
        """Initialize an empty inventory and log list."""
        self.stock_data = {}
        self.logs = []

    def add_item(self, item="default", qty=0):
        """
        Add a specified quantity of an item to the inventory.
        Ignores invalid types.
        """
        if not isinstance(item, str) or not isinstance(qty, int):
            return
        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        timestamp = datetime.now()
        self.logs.append(f"{timestamp}: Added {qty} of {item}")

    def remove_item(self, item, qty):
        """
        Remove a quantity of an item if it exists.
        Deletes the item entry if quantity falls to zero or below.
        """
        if item not in self.stock_data or not isinstance(qty, int):
            return
        self.stock_data[item] -= qty
        if self.stock_data[item] <= 0:
            del self.stock_data[item]

    def get_qty(self, item):
        """
        Return the current quantity of a given item.
        Returns 0 if item is not found.
        """
        return self.stock_data.get(item, 0)

    def load_data(self, file="inventory.json"):
        """
        Load inventory data from a JSON file.
        Creates a new empty inventory if the file does not exist.
        """
        try:
            with open(file, "r", encoding="utf-8") as f:
                self.stock_data = json.load(f)
        except FileNotFoundError:
            self.stock_data = {}

    def save_data(self, file="inventory.json"):
        """Save current inventory data to a JSON file."""
        with open(file, "w", encoding="utf-8") as f:
            json.dump(self.stock_data, f, indent=4)

    def print_data(self):
        """Print a formatted report of all inventory items."""
        print("Items Report")
        for item, qty in self.stock_data.items():
            print(f"{item} -> {qty}")

    def check_low_items(self, threshold=5):
        """Return a list of items having stock below a given threshold."""
        return [
            item for item, qty in self.stock_data.items()
            if qty < threshold
        ]


def main():
    """Run a sample inventory demo with test operations."""
    inventory = InventorySystem()
    inventory.add_item("apple", 10)
    inventory.add_item("banana", 3)
    inventory.remove_item("apple", 3)

    print("Apple stock:", inventory.get_qty("apple"))
    print("Low items:", inventory.check_low_items())

    inventory.save_data()
    inventory.load_data()
    inventory.print_data()


if __name__ == "__main__":
    main()
