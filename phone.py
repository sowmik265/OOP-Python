from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones = 0):
        #call to super function to have access to all attributes/methods
        super().__init__(
            name, price, quantity
        )
        # validation to the received arguments
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to zero"

        # assign to self object
        self.broken_phones = broken_phones