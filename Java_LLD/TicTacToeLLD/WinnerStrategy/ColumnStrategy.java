package TicTacToeLLD.WinnerStrategy;

import TicTacToeLLD.PlayingPiece;

public class ColumnStrategy implements CheckWinnerStrategy {
    
    @Override
     public boolean checkWinner(PlayingPiece [][]board){
            
        for (int i = 0; i < board.length; i++) {
          PlayingPiece first = board[0][i];
          if (first == null) continue;
          boolean allMatch = true;
  
          for (int j = 1; j < board[i].length; j++) {
              if (board[j][i] == null || board[j][i].getPieceType() != first.getPieceType()) {
                  allMatch = false;
                  break;
              }
          }
  
          if (allMatch) return true;
      }
      return false;
        
     }
}