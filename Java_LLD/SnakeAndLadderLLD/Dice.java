package SnakeAndLadderLLD;

import java.util.concurrent.ThreadLocalRandom;

public class Dice {
    int min =1;
    int max=6;

    public int rollDice(){
        int totalSum=0;
        return  totalSum += ThreadLocalRandom.current().nextInt(min,max+1);
    }
}
