from project.product import Product
from typing import List, Optional


class ProductRepository:

    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Optional[Product]:
        return next((a for a in self.products if a.name == product_name), None)

    def remove(self, product_name: str) -> None:
        curr_product = self.find(product_name)
        if curr_product:
            self.products.remove(curr_product)

    def __repr__(self) -> str:
        return '\n'.join([f"{p.name}: {p.quantity}" for p in self.products])
