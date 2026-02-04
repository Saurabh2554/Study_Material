package ElevatorSystemLLD;

public class InternalButton {
    InternalButtonDispatcher iBDispatcher = new InternalButtonDispatcher();

    int[] availableButtons = {1,2,3,4,5,6,7,8,9};
    int selectedButton;
    
    void pressButton(int destination, ElevatorCar elevatorCar){
        iBDispatcher.submitInternalRequest(destination,elevatorCar);
    }
}
