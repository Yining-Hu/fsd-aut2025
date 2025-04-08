package com;

// import java.text.*;

public class Stadium {
    private Group group;

    public Stadium() {
        group = new Group("front", 300, 400.0);
    }

    public final Group getGroup() {
        return group;
    }
}
