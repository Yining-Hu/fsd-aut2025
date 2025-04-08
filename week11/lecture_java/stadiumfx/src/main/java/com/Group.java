package com;

import java.text.DecimalFormat;
import javafx.beans.property.*;

public class Group {
    private String name;
    private int capacity;
    private double price;
    // observable properties
    private IntegerProperty sold = new SimpleIntegerProperty();
    private DoubleProperty income = new SimpleDoubleProperty();
    private IntegerProperty left = new SimpleIntegerProperty();

    public Group(String name, int capacity, double price) {
        this.name = name;
        this.capacity = capacity;
        this.price = price;
        sold.set(0);
        income.bind(sold.multiply(price));
        left.bind(sold.subtract(capacity).multiply(-1));
    }

    public final String getName() { return name; }
    public final int getCapacity() { return capacity; }
    public final double getPrice() { return price; }
    
    // returns the sold property
    public ReadOnlyIntegerProperty soldProperty() {
        return sold;
    }

    // returns the sold value
    public final int getSold() {
        return sold.get();
    }
    
    public ReadOnlyIntegerProperty leftProperty() {
        return left;
    }

    public final int getLeft() {
        return left.get();
    }

    public ReadOnlyDoubleProperty incomeProperty() {
        return income;
    }

    public final double getIncome() {
        return income.get();
    }

    public boolean canSell(int number) {
        return number <= capacity;
    }

    public void sell(int number) {
        sold.set(sold.get()+number);
    }

    @Override
    public String toString() {
        return getLeft()+" " + name + " seats @ $" + formatted(price);
    }

    private String formatted(double money) {
        return new DecimalFormat("###,##0.00").format(money);
    }
}
