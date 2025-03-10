import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Bank {
    static DateTimeFormatter DTF = DateTimeFormatter.ofPattern("dd/MM/uuuu - HH:mm:ss");
    static LocalDateTime NOW = LocalDateTime.now();
    private List<Customer> customers;
    private Manager admin;
    private Scanner in = new Scanner(System.in);
    
    public static void main(String[] args) {
        (new Bank()).menu();
    }

    public Bank() {
        admin = new Manager();
        customers = new ArrayList<>();
        addCustomers();
    }

    private void addCustomers() {
        for (int i = 0; i < 3; i++) {
            this.customers.add(new Customer());
        }
    }

    private char readChoice(){
        System.out.print("Please select (L/A/X): ");
        return in.next().charAt(0);
    }
    
    private Customer customer(String name){        
        for(Customer c:customers)
            if(c.match(name))
                return c;
        return null;
    }

    private String readName() {
        System.out.print("Enter Customer Name: ");
        return in.next();
    }

    public void show() {
        Customer customer = customer(readName());
        if (customer != null)
            System.out.println(customer);
        else
            System.out.println("Customer does not exist");
    }
    
    public void view() {
        customers.forEach(System.out::println);
    }

    public void add(){        
        String name = readName();
        Customer customer = customer(name);
        if (customer == null) {            
            customers.add(new Customer(name));
        }else{
            System.out.println("Customer already exists");
        }
    }
    
    public void remove(){
        Customer customer = customer(readName());
        if (customer != null){
            customers.remove(customer);
        }else
            System.out.println("Customer does not exist");
    }
    
    private void customerLogin() {
        Customer c = customer(readName());
        if (c != null)
            c.use();
        else
            System.out.println("Customer does not exist");
    }

    private void adminLogin(Bank bank) {
        admin.use(bank);
    }
        
    public void menu() {
        System.out.println("Bank menu: "+DTF.format(NOW));
        char c;
        while((c = readChoice()) != 'X'){
            switch(c){
                case 'L': customerLogin(); break;
                case 'A': adminLogin(this); break;
                default: help(); break;
            }
        }
        System.out.println("Done");
    }
    
    private void help() {
        System.out.println("Menu options");
        System.out.println("L = Login into customer menu");
        System.out.println("A = Login to admin menu");
        System.out.println("X = exit");
    }
}

