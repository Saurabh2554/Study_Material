package TicTacToeLLD;

import TicTacToeLLD.WinnerStrategy.*;

public class Board {
   private int size;
   private PlayingPiece [][]board;
   private CheckWinnerStrategy winnerStrategy;

    public Board(){
        // Do nothing
    }
    public Board(int size){
       this.size = size;
       board = new PlayingPiece[size][size];
    }
    public int getSize(){
      return this.size;
    }
    public void printBoard(){
        System.out.println(" ");
       for(PlayingPiece row[]: board){
           for(PlayingPiece col: row){
            if (col != null) {
                System.out.print(col.getPieceType());
            } else {
                System.out.print(col);
            }
            System.out.print(" || ");
           }
           System.out.println(" ");
       }
       System.out.println(" ");
    }

    public void insertPiece(PlayingPiece piece, int row, int col){
        if(board[row][col]==null){
            board[row][col]=piece;
        }
        printBoard();
    }
    public boolean checkTie(){
      return false;
    }
    public boolean checkWinner(){
        CheckWinnerStrategy winnerRowStrategy = new RowStrategy();
        CheckWinnerStrategy winnerColumnStrategy = new ColumnStrategy();
        CheckWinnerStrategy winnerDiagStrategy = new DiagonalStrategy();
        

        return winnerRowStrategy.checkWinner(board) || winnerColumnStrategy.checkWinner(board) || winnerDiagStrategy.checkWinner(board);
    }
  

}
