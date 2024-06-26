from typing import Dict


class Shop:
    def __init__(self, name: str, type: str, capacity: int) -> None:
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items: Dict[str: int] = {}

    @classmethod
    def small_shop(cls, name: str, type: str):
        return cls(name, type, 10)

    def add_item(self, item_name: str) -> str:
        if sum(self.items.values()) >= self.capacity:
            return "Not enough capacity in the shop"
        else:
            if item_name in self.items.keys():
                self.items[item_name] += 1
            else:
                self.items[item_name] = 1

            return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int) -> str:
        if item_name in self.items.keys():
            if self.items[item_name] > amount:
                self.items[item_name] -= amount
                return f"{amount} {item_name} removed from the shop"
        # TODO not sure
            elif self.items[item_name] == amount:
                self.items.pop(item_name)
                return f"{item_name} removed from the shop"

        return f"Cannot remove {amount} {item_name}"

    def __repr__(self) -> str:
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)
