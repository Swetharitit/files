import json

# Inventory class to represent each inventory item
class Inventory:
    def __init__(self, name, quantity, price_per_unit):
        self.name = name  # Name of the inventory item
        self.quantity = quantity  # Quantity of the item
        self.price_per_unit = price_per_unit  # Price per unit of the item

    # Method to calculate total value of the inventory item
    def calculate_total_value(self):
        return self.quantity * self.price_per_unit
    
    # Method to convert the inventory object to JSON format
    def to_json(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price_per_unit": self.price_per_unit,
            "total_value": self.calculate_total_value()
        }

# InventoryFactory class to create inventory objects from JSON
class InventoryFactory:
    @staticmethod
    def create_inventory_from_json(json_data):
        inventories = []
        for item in json_data:
            # Create Inventory object from JSON data
            inventory = Inventory(item["name"], item["quantity"], item["price_per_unit"])
            inventories.append(inventory)
        return inventories

# InventoryManager class to manage the list of inventory objects
class InventoryManager:
    def __init__(self, inventories):
        self.inventories = inventories  # List of Inventory objects

    # Method to calculate the total inventory value
    def calculate_inventory_values(self):
        for inventory in self.inventories:
            print(f"Item: {inventory.name}, Quantity: {inventory.quantity}, "
                  f"Price per Unit: {inventory.price_per_unit}, "
                  f"Total Value: {inventory.calculate_total_value()}")

    # Method to output the entire inventory as a JSON string
    def to_json_string(self):
        json_output = [inventory.to_json() for inventory in self.inventories]
        return json.dumps(json_output, indent=4)

# Main program to read JSON, create inventory objects, and manage them
def main():
    # Read JSON file containing inventory data
    filename = 'inventory.json'  # Input JSON file
    try:
        with open(filename, 'r') as file:
            json_data = json.load(file)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return

    # Create inventory objects from JSON data
    inventories = InventoryFactory.create_inventory_from_json(json_data)

    # Initialize InventoryManager with the list of inventories
    inventory_manager = InventoryManager(inventories)
    
    # Calculate and display each inventory's value
    print("Inventory Report:")
    inventory_manager.calculate_inventory_values()
    
    # Output the inventory data as a JSON string
    print("\nJSON Output:")
    print(inventory_manager.to_json_string())

# Run the main program
if __name__ == "__main__":
    main()
