package ElevatorSystemLLD;
import java.util.ArrayList;
import java.util.List;

public class ExternalButtonDispatcher {

    List<ElevatorController> ElevatorControllerList = ElevatorCreator.elevatorControllerList;

    public void submitRequest(int floor,Direction dir){
       //for simplicity, i am following even odd,
       for(ElevatorController elevatorController : ElevatorControllerList) {

        int elevatorID = elevatorController.carObj.id;
        if (elevatorID%2==1 && floor%2==1){
            elevatorController.submitExternalRequest(floor,dir);
        } else if(elevatorID%2==0 && floor%2==0){
            elevatorController.submitExternalRequest(floor,dir);

        }
     }

    }
}
