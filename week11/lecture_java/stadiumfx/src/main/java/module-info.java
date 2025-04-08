module com {
    requires javafx.controls;
    requires javafx.fxml;
    requires javafx.media;
    requires java.logging;
    opens com to javafx.fxml;
    exports com;
}