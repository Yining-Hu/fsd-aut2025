module com.fsd {
    requires javafx.controls;
    requires javafx.fxml;

    opens com.fsd to javafx.fxml;
    exports com.fsd;
    
    opens com.fsd.controller to javafx.fxml;
    exports com.fsd.controller;

    opens com.fsd.model to javafx.fxml;
    exports com.fsd.model;
    
    opens com.fsd.ap.fx to javafx.fxml;
    exports com.fsd.ap.fx;
}
