# Clase con el profe:

class Vector:
    def __init__(self,data) -> None:
        self.data = data

    def __str__(self) -> str:
        return f"El valor de este vector es: {self.data}"
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, position):
        return self.data[position]
    
    def __setitem__(self, position, value):
        self.data[position] = value

vector = Vector([1,2,3,4])
print(vector)

vector.__setitem__(0,10)

print(vector)

