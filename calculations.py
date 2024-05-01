class Cal:
    def __init__(self, X: int | float, Y: int | float) -> None:
        self.X = X
        self.Y = Y
    
    def Add(self) -> (int | float):
        return self.X + self.Y
    
    def Sub(self) -> (int | float):
        return self.X - self.Y
    
    def Multi(self) -> (int | float):
        return self.X * self.Y
    
    def Divide(self) -> (int | float):
        return self.X / self.Y