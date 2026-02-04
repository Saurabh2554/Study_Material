package TicTacToeLLD.WinnerStrategy;

import TicTacToeLLD.Board;
import TicTacToeLLD.PlayingPiece;

public interface CheckWinnerStrategy{
    public boolean checkWinner(PlayingPiece [][]board);
}
