package com;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.application.*;
import javafx.stage.*;
import javafx.scene.*;
// import javafx.scene.control.*;
// import javafx.scene.layout.*;
// import javafx.scene.text.*;
// import javafx.geometry.*;
import javafx.fxml.*;
public class StadiumApplication extends Application {
	public static void main(String[] args) { launch(args); }
	@Override
	public void start(Stage stage) {
            try {
                FXMLLoader loader = new FXMLLoader(getClass().getResource("/fxml/stadium.fxml"));
                Parent root = loader.load();
                stage.setTitle("Stadium");
                stage.setScene(new Scene(root));
                stage.sizeToScene();
                stage.show();
            } catch (IOException ex) {
                Logger.getLogger(StadiumApplication.class.getName()).log(Level.SEVERE, null, ex);
            }
	}
}
