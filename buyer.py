class Buyer:
    def __init__(self, last_name: str, first_name: str, middle_name: str, phone_num: str):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone_num = phone_num

    def __str__(self):
        return f"Фамилия - {self.last_name}, Имя - {self.first_name},Отчество - {self.middle_name}, номер телефона - {self.phone_num} "


b_1 = Buyer("Семеренко", "Иван", "Степанович", "07312572591")

print(b_1)