package ElevatorSystemLLD;

public  abstract class Display {
    int floor;
    Direction dir;
    public Display(){
        this.floor = 0;
        this.dir = Direction.UP;
    }
    public Display(int floor, Direction dir){
        this.floor = floor;
        this.dir = dir;
    }
}
