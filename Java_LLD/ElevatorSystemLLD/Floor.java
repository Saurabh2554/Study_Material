package ElevatorSystemLLD;

public class Floor {
    int floorId;
    ExternalButton exButton;
    
    public Floor(){
        
    }

    public Floor(int floorId){
        this.floorId = floorId;
        this.exButton = ExternalButton.getInstance(floorId);
    }
    
    public void makeActivity(Direction dir){
      exButton.pressButton(floorId,dir);
    }
}
