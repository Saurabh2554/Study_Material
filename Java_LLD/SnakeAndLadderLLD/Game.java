package SnakeAndLadderLLD;

import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;

public class Game {
    Board b1;
    Dice d1;
    Deque<Players>pl = new LinkedList<>();
    Players[] winner=new Players[5];
    ArrayList<Players> winnerList = new ArrayList<>();

    public Game(){
        initialiseGame();
    }
    private void initialiseGame(){
        b1 = new Board(10,5,4);
        d1 = new Dice();
        Players pl1 = new Players("player-1", 0);
        Players pl2 = new Players("player-2",0);
        Players pl3 = new Players("player-3", 0);
        Players pl4 = new Players("player-4",0);
        Players pl5 = new Players("player-5", 0);
 
        pl.add(pl1);
        pl.add(pl2);
        pl.add(pl3);
        pl.add(pl4);
        pl.add(pl5);
        
        
        //start Game--->
        play();
    }
    private void play(){
        System.out.println("Game Started ");

        while(winnerList.size()!=4){
            Players pl1 = pl.removeFirst();
            System.out.println("It's Player: "+ pl1.id + " turn and he is currently at: "+ pl1.position + " Position");
            int diceResult = d1.rollDice();

            int newPos = jumpCheck(pl1.position+diceResult);

            if(b1.checkWinner(newPos)){
                winnerList.add(pl1);
                System.out.println(pl1.id + " came " + winnerList.size());
            }else{
                pl1.position = newPos;
                pl.add(pl1);
            }
            
        }


    }

    private int jumpCheck (int playerNewPosition) {

        if(playerNewPosition > b1.cells.length * b1.cells.length-1 ){
            return playerNewPosition;
        }

        Cell cell = b1.getCell(playerNewPosition);
        if(cell.jump != null && cell.jump.start == playerNewPosition) {
            String jumpBy = (cell.jump.start < cell.jump.end)? "ladder" : "snake";
            System.out.println("jump done by: " + jumpBy);
            return cell.jump.end;
        }
        return playerNewPosition;
    }

}
