package ElevatorSystemLLD;

import java.util.HashMap;
import java.util.Map;

public class ExternalButton {
    ExternalButtonDispatcher exDisp;

    private static Map<Integer, ExternalButton> buttonRegistry = new HashMap<>();
     private ExternalButton(){
       
        exDisp = new ExternalButtonDispatcher();
     }

     public static ExternalButton getInstance(int floorId) {
       
         return buttonRegistry.computeIfAbsent(floorId, id -> new ExternalButton());
        
    }
    public void pressButton(int floorId,Direction dir){
       exDisp.submitRequest(floorId, dir);
    }
}
