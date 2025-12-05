import numpy as np

class TicTacToe:
    def __init__(self) -> None:
        self.grid=np.array([[-1 for _ in range(3)]for _ in range(3)])
        self.cur_player=0
        self.iswon=True
    
    def check_move_validity(self, movex, movey):
        #to complete
        pass

    def check_win(self):
        #to complete
        pass
    
    def play_move(self,movex, movey):
        if self.check_move_validity(movex, movey):
            self.grid[movex, movey]=self.cur_player
            self.cur_player=(self.cur_player+1)%2
    
    

        