

class UnitBuilder:
    def __init__(self,unit_size,unit_state):
        self.unit_size = unit_size
        self.unit_state = unit_state
    
    def Return_unit_size(self):
        return self.unit_size

    def Return_unit_state(self):
        return self.unit_state
    


hopper = UnitBuilder(10,"ready")

print(hopper.Return_unit_size())
print(hopper.Return_unit_state())