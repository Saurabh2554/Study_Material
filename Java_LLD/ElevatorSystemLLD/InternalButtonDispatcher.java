package ElevatorSystemLLD;
import java.util.List;

public class InternalButtonDispatcher {
    List<ElevatorController> elevatorControllerList = ElevatorCreator.elevatorControllerList;

   public void submitInternalRequest(int destinaton,ElevatorCar carObj){
    
     
    for(ElevatorController controller: elevatorControllerList){
        if(controller.equals(carObj)){
            controller.submitExternalRequest(destinaton, null);
        }
    }
   }

}
