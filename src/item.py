class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # def __str__(self):
    #     return f"{self.name} \n{self.description}"

    def on_take(self, player):
        player.items.append(self)
        player.current_room.items.remove(self)
        print(f"You pet a {self.name}")

    def on_drop(self, player):
        player.items.remove(self)
        player.current_room.items.append(self)
        print(f"You gently put down your {self.name}")

