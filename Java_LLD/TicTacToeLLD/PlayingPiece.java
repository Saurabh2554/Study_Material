package TicTacToeLLD;
import TicTacToeLLD.PieceType;

public class PlayingPiece {
    private PieceType type;
    
    public PlayingPiece(){
        this.type = PieceType.X;
    }

    public PlayingPiece(PieceType t){
        this.type = t;
    }
    public PieceType getPieceType(){
        return this.type;
    }
}



