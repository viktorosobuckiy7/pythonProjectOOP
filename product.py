class Product:
    def __init__(self, price: int | float, color: str, model: str, weight: int | float):
        self.price = price
        self.color = color
        self.weight = weight
        self.model = model

    def __str__(self):
        return f" Модель телефона - {self.model}, цена данного телефона - {self.price} гривен, цвет - {self.color}, вес - {self.weight} грамм"

