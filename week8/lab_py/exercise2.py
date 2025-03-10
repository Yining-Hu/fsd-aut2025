from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, position, type):
        self.position = position
        self.type = type
        
    @abstractmethod
    def walk(self):
        pass
    
    def show(self):
        print(f'{self.type} is at position {self.position}')

class Cat(Animal):
    def __init__(self):
        super().__init__(0, "Cat")
        
    def walk(self):
        self.position += 2

class Dog(Animal):
    def __init__(self):
        super().__init__(0, "Dog")
        
    def walk(self):
        self.position += 4

class Farm:
    def __init__(self):
        self.animals = []
        self.populate()
        
    def populate(self):
        self.animals.append(Dog())
        self.animals.append(Cat())
        
    def walk(self):
        for animal in self.animals:
            animal.walk()
            
    def show(self):
        for animal in self.animals:
            animal.show()
            
    def read_choice(self):
        return input("Choice(w/s/x): ").strip()
    
    def help(self):
        print("w - walk")
        print("s - show")
        print("x - exit")
        
    def use(self):
        choice = ''
        
        while choice != 'x':
            choice = self.read_choice()
            if choice == 'w':
                self.walk()
            elif choice == 's':
                self.show()
            else:
                self.help()
                
        print("Goodbye!")

if __name__ == "__main__":
    Farm().use()