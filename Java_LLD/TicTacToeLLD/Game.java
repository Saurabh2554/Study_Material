package TicTacToeLLD;

import java.util.Deque;
import java.util.LinkedList;
import java.lang.Thread;
import java.util.Scanner;

public class Game {
    Deque<Player>players;

    public Game(){
        initialiseGame();
    }
    

    public void initialiseGame(){
        players = new LinkedList<>();

        //considering a 2 player game;

        Player playerX = new Player("playerX", new PlayingPiece(PieceType.X));
        Player playerO = new Player("playerO", new PlayingPiece(PieceType.O));

      players.add(playerX);
      players.add(playerO);
      
      Board board1 = new Board(3);
      board1.printBoard();

      try {
        startGame(board1);
    } catch (InterruptedException e) {
        // TODO Auto-generated catch block
        e.printStackTrace();
    }
    }

    public void startGame(Board board1) throws InterruptedException{
        
        Scanner scanner = new Scanner(System.in);

        while(true){
           Player tempPlayer = players.remove(); 
           System.out.println(tempPlayer.getName() + " turn");
           System.out.print("Enter row (0-2): ");
            int row = scanner.nextInt();
            System.out.print("Enter column (0-2): ");
            int col = scanner.nextInt();

            // Validate row and column
            if (row < 0 || row > 2 || col < 0 || col > 2) {
                System.out.println("Invalid position! Please enter values between 0 and 2.");
                continue;
            }
            board1.insertPiece(tempPlayer.getPiece(),row,col);
           Thread.sleep(3);
           if(board1.checkWinner()){
            System.out.println(tempPlayer.getName() + "Won...");
              
              break;
           } 
           else if(board1.checkTie()){
            System.out.println("Game Tie...");
           }
           players.add(tempPlayer);
           
        }
    }
}
