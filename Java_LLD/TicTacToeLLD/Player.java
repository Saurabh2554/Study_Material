package TicTacToeLLD;

public class Player {
   private String name;
   private PlayingPiece piece;
   
   public Player(){
    this.name = "random";
    this.piece = new PlayingPiece();
   }
   public Player(String name, PlayingPiece piece){
    this.name = name;
    this.piece = piece;
   }

   public String getName(){
    return this.name;
   }
   public void updateName(String newName){
     this.name = newName;
   }
   public PlayingPiece getPiece(){
    return this.piece;
   }
}
