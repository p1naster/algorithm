class Person:
    def __init__(self, name, hand, chest):
        self.name = name
        self.hand = hand
        self.chest = chest

    def attribute(self):
        print(self.name, "has", self.hand)
        print(self.name, "has", self.chest)

Keson = Person("Keson", "strong hand", "middle chest")
Maxue = Person("Maxue", "thin hand", "big chest")

Keson.attribute()
Maxue.attribute()