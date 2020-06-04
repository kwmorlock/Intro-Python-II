# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        if inventory == []:
            self.inventory = []
        else:
            self.inventory = inventory

    def on_take(self, item):
        self.inventory.append(item)

    def on_drop(self, item):
        self.inventory.remove(item)