# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.n_to=None
        self.w_to=None
        self.e_to=None
        self.s_to=None
#initialized to empty rooms

    def __str__(self):
        print(self.name, self.description)

    def list_items(self):
        if not self.items:
            print("Your pets got away")
        else:
            print("Steal the: ")
            for item in self.items:
                print(item.name)
                print(item.description)


        # if items == []:
        #     self.items = []
        # else:
        #     self.items = items