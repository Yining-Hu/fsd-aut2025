package lab8.exercise2;

import java.util.ArrayList;
import java.util.List;
import utils.In;

public class Farm {
    private List<Animal> animals = new ArrayList<>();

    public Farm() {
        this.populate(); 
    }
    
    private void populate() {
        animals.add(new Dog());
        animals.add(new Cat());
    }

    private void walk() {
        animals.forEach(a -> a.walk());
    }

    private void show() {
        animals.forEach(Animal::show);
    }

    private char readChoice() {
        System.out.print("Choice(w/s/x): ");
        return In.nextChar();
    }

    private void help() {
        System.out.println("w - walk");
        System.out.println("s - show");
        System.out.println("x - exit");
    }

    private void use() {
        char choice;

        while ((choice = readChoice()) != 'x') {
            switch (choice) {
                case 'w':
                    walk();
                    break;
                case 's':
                    show();
                    break;
                default:
                    help();
                    break;
            }
        }
        System.out.println("Goodbye!");
    }

    public static void main(String[] args) {
        new Farm().use();
    }
}
