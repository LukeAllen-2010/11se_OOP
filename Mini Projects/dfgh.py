class HelpMe:
    def __init__(self, name):
        self.name = name

class Ahhhh(HelpMe):
    def __init__(self, name):
        super().__init__(name)
        self.coding_skill = -1000



luke = Ahhhh('luke')

print(luke.name)
print(luke.coding_skill)