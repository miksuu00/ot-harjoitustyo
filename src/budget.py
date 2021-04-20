

class Budget:
    def __init__(self):
        self.budjet = []

    def add_cost(self, cost:str, amount:str):
        self.budjet.append(cost+";"+amount)
    
    def return_items(self):
        return self.budjet