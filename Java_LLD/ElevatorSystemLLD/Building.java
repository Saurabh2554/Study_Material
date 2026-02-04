package ElevatorSystemLLD;

import java.util.ArrayList;
import java.util.List;

public class Building {
    String buildingName;
    List<Floor>floorList;

    public Building (String name,int floor){
        this.buildingName = name;
        floorList = new ArrayList<>();
      for(int i=0;i<floor;i++){
        floorList.add(new Floor(i+1));
      }
    }

    public void createElevator(int numElevator){
        ElevatorCreator.CreateElevator(numElevator);
    }

}
