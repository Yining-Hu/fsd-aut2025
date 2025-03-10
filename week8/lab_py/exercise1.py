from abc import abstractmethod

class Polygon:
    def __init__(self, type):
        self.type = type
       
    @abstractmethod
    def area(self):
        pass 
    
    def __str__(self) -> str:
        return f'{self.type}'
    
class Square(Polygon):
    def __init__(self, type,side):
        super().__init__(type)
        self.side = side
        
    def area(self):
        return pow(self.side,2)
    
    def __str__(self) -> str:
        return super().__str__()+f' area = {self.area()}'
    
class Triangle(Polygon):
    def __init__(self, type, height, base):
        super().__init__(type)
        self.height = height
        self.base = base
        
    def area(self):
        return self.base*self.height/2
    
    def __str__(self) -> str:
        return super().__str__()+f' area = {self.area()}'
    
class Shapes:
    def load_shapes(self):
        self.shapes.append(Square('Square',5))
        self.shapes.append(Square('Square',5))
        self.shapes.append(Triangle('Triangle',5,3))
        self.shapes.append(Triangle('Triangle',5,5))
        
    def __init__(self):
        self.shapes = []
        self.load_shapes()
        
    def show(self):
        for p in self.shapes:
            print(p)
    
if __name__ == '__main__':
    Shapes().show()