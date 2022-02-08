class Transaction:
    def __init__(self, merchant, amount, currency="EUR") -> None:
        self.merchant = merchant
        self.amount = amount
        self.currency = currency

users = {
    "pepe": "password",
    "other": "otherpassword"
}

transactions = {
    "pepe": [
        Transaction("IE Cafeteria", 1.5),
        Transaction("IE Cafeteria", 5),
        Transaction("Book shop", 30),
        Transaction("Restaurant", 23),
    ],
    "other": [
        Transaction("Dog Food Inc.", 15),
        Transaction("United Cat Food Coop", 5),
        Transaction("Apple", 3000),
    ],
}