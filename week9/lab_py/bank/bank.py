from customer import Customer
from utils import DTF,NOW,initialize,read_from_file,write_to_file

class Bank:
    def __init__(self):
        self.admin = Manager()
        initialize()
        self.customers = read_from_file()
    
    def main(self):
        self.menu()
    
    def read_choice(self):
        print(f'Bank menu (L/A/X): {NOW.strftime(DTF)}: ', end="")
        return input().strip().upper()
    
    def check_customer(self, name):
        customers = read_from_file()
        if customers != []:
            for c in customers:
                if c.match(name):
                    return c
            return None
        else:
            return None
    
    def read_name(self):
        print("Enter Customer Login Name: ", end="")
        return input().strip()
    
    def customer_login(self):
        c = self.check_customer(self.read_name())
        if c:
            c.use()
        else:
            print("Customer does not exist")
    
    def admin_login(self,bank):
        self.admin.use(bank)

    def show(self):
        customer = self.check_customer(self.read_name())
        if (customer != None):
            print(customer)
        else:
            print("Customer does not exist")

    def add(self):
        customers = read_from_file()
        newCustomer = Customer()
        customer = self.check_customer(newCustomer.name)
        if (customer == None): 
            customers.append(newCustomer)
            write_to_file(customers)
        else:
            print("Customer already exists")
    
    def remove(self):
        customers = read_from_file()
        name = self.read_name()
        for c in customers:
            if c.match(name):
                customers.remove(c)
                write_to_file(customers)
                break
            else:
                print("Customer does not exist")
                break
    
    def view(self):
        customers = read_from_file()
        for customer in customers:
            print(customer)
    
    def menu(self):
        choice = self.read_choice()
        while choice!='X':
            match choice:
                case 'L':
                    self.customer_login()
                case 'A':
                    self.admin_login(bank)
                case _:
                    self.help()
            choice = self.read_choice()

    def help(self):
        print("Menu options")
        print("L = Login into customer menu")
        print("A = Login to admin menu")
        print("X = exit")

class Manager:
    def __init__(self):
        self.name = "John Smith"

    def view(self,bank):
        bank.view()

    def show(self,bank):
        bank.show()

    def remove(self,bank):
        bank.remove()

    def add(self,bank):
        bank.add()

    def read_choice(self):
        print("Manager menu (a/r/v/s/x): ", end="")
        return input().strip().lower()
    
    def use(self,bank):
        print(f'{self.name} admin menu: {NOW.strftime(DTF)}')
        c = self.read_choice()
        while c!='x':
            match c:
                case 'a':
                    self.add(bank)
                case 'r':
                    self.remove(bank)
                case 's':
                    self.show(bank)
                case 'v':
                    self.view(bank)
                case _:
                    self.help()
            c = self.read_choice()
        print("Back to Bank menu")

    def help(self):
        print("Menu options")
        print("a = add a customer")
        print("r = remove a customer")
        print("v = view all customers")
        print("s = show the selected customer")
        print("x = exit")

# Running the main function
bank = Bank()
bank.main()