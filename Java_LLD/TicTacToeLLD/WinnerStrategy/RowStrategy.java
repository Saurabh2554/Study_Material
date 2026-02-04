package TicTacToeLLD.WinnerStrategy;

import TicTacToeLLD.Board;
import TicTacToeLLD.PlayingPiece;

public class RowStrategy implements CheckWinnerStrategy {
    
    @Override
     public boolean checkWinner(PlayingPiece [][]board){
            
            for (int i = 0; i < board.length; i++) {
                PlayingPiece first = board[i][0];
                if (first == null) continue;
                boolean allMatch = true;
        
                for (int j = 1; j < board[i].length; j++) {
                    if (board[i][j] == null || board[i][j].getPieceType() != first.getPieceType()) {
                        allMatch = false;
                        break;
                    }
                }
        
                if (allMatch) return true;
            }
            return false;
        
     }
}
