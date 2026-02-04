package SnakeAndLadderLLD;

import java.util.concurrent.ThreadLocalRandom;

public class Board {
    Cell [][] cells;
    Board(int boardSize, int numSnakes, int numLadder){
        initialiseCells(boardSize);
        addSnakesLadders(cells,numLadder,numSnakes);
    }

    private void initialiseCells(int boardSize){
        cells = new Cell[boardSize][boardSize];
        for(int i=0;i<boardSize;i++){
            for(int j=0;j<boardSize;j++){
                Cell cellObj = new Cell();
                cells[i][j] = cellObj;
            }
        }
    }

    private void addSnakesLadders(Cell[][] cells, int numLadder, int numSnakes){
        while(numSnakes>0){
            int snakeHead = ThreadLocalRandom.current().nextInt(1,cells.length*cells.length-1);
            int snakeTail = ThreadLocalRandom.current().nextInt(1,cells.length*cells.length-1);

            if(snakeTail>=snakeHead)
            continue;

            Jump snakeObj = new Jump(snakeHead, snakeTail);
            
            Cell cell = getCell(snakeHead);
            cell.jump = snakeObj;
            numSnakes--;

        }

        while(numLadder>0){
            int ladderHead = ThreadLocalRandom.current().nextInt(1,cells.length*cells.length-1);
            int ladderTail = ThreadLocalRandom.current().nextInt(1,cells.length*cells.length-1);

            if(ladderHead>=ladderTail)
            continue;

            Jump ladderObj = new Jump(ladderHead, ladderTail);
            
            Cell cell = getCell(ladderHead);
            cell.jump = ladderObj;
            numLadder--;

        }
    }

    public Cell getCell(int playerPosition){

        int boardRow = playerPosition / cells.length;
        int boardColumn = (playerPosition % cells.length);
        return cells[boardRow][boardColumn];
    
       
    }

    public boolean checkWinner(int pos){
        return pos >= cells.length*cells.length-1;
    }

    
}
