package ElevatorSystemLLD;

import java.util.ArrayList;
import java.util.List;

public class ElevatorCreator {
     static List<ElevatorController>elevatorControllerList = new ArrayList<>();
     

     public static void CreateElevator(int numElevator){

        for(int i=0;i<numElevator;i++){
            ElevatorCar car = new ElevatorCar(i+1);
            ElevatorController contrller = new ElevatorController(car);
            elevatorControllerList.add(contrller);
        }   
     }
}
