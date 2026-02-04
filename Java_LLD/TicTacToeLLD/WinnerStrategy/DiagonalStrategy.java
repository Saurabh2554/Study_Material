package TicTacToeLLD.WinnerStrategy;

import TicTacToeLLD.PlayingPiece;

public class DiagonalStrategy implements CheckWinnerStrategy {
    
    @Override
    public boolean checkWinner(PlayingPiece [][]board){
            
        PlayingPiece firstPiece = board[0][0];
        if (firstPiece == null) return false;
        
        for (int i = 1; i < board.length; i++) {
            if (board[i][i] == null || board[i][i].getPieceType() != firstPiece.getPieceType()) {
                break;
            }
            if (i == board.length - 1) return true;
        }
    
        // Check top-right to bottom-left diagonal
        firstPiece = board[0][board.length - 1];
        if (firstPiece == null) return false;
    
        for (int i = 1; i < board.length; i++) {
            if (board[i][board.length - 1 - i] == null || 
                board[i][board.length - 1 - i].getPieceType() != firstPiece.getPieceType()) {
                break;
            }
            if (i == board.length - 1) return true;
        }
    
        return false;

    }
    
}
