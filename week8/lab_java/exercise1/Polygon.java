package lecture8;

public abstract class Polygon{
    protected String type;

    public Polygon(String type) {
        this.type = type;
    }

    public abstract double area();
}
