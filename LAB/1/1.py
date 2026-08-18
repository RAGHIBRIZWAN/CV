import cv2
import matplotlib.pyplot as plt

class GroceryManager:

    def __init__(self):
        self.items = []

    def add_item(self, item, quantity, price):
        grocery = {
            "name": item,
            "quantity": quantity,
            "price": price
        }

        self.items.append(grocery)
        print(item, "was added to the list.")

    def remove_item(self, item):
        for grocery in self.items:
            if grocery["name"].lower() == item.lower():
                self.items.remove(grocery)
                print(item, "was removed from the list.")
                return

        print("Sorry,", item, "is not in the list.")

    def view_list(self):
        if len(self.items) == 0:
            print("The grocery list is empty.")
        else:
            print("\nGrocery List:")

            for grocery in self.items:
                print(
                    grocery["name"],
                    "- Quantity:",
                    grocery["quantity"],
                    "- Price: $",
                    grocery["price"]
                )

    def calculate_total(self):
        total = 0

        for grocery in self.items:
            total = total + (grocery["quantity"] * grocery["price"])

        return total


grocery_list = GroceryManager()

grocery_list.add_item("Apples", 2, 3.50)
grocery_list.add_item("Milk", 1, 2.50)
grocery_list.add_item("Bread", 2, 2.00)

grocery_list.view_list()

print("\nTotal cost: $", grocery_list.calculate_total())

grocery_list.remove_item("Milk")

grocery_list.remove_item("Eggs")

grocery_list.view_list()

print("\nFinal total: $", grocery_list.calculate_total())
