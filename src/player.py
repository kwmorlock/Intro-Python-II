# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
        # if inventory == []:
        #     self.inventory = []
        # else:
        #     self.inventory = inventory

    def move(self, direction):
            if getattr(self.current_room, f"{direction}_to") is not None:
                self.current_room = getattr(self.current_room, f"{direction}_to")
            else:
                print("Stop trying to walk into a wall!")
                #getattr a method to get attribute, we are getting attribute from line 6, the if is no longer set to none, if the direction doesnt work its then else


    def on_take(self, item):
        self.inventory.append(item)

    def on_drop(self, item):
        self.inventory.remove(item)