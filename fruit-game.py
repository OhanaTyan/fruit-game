import random
from typing import Tuple

def is_all_equal(l):
    assert len(l) == 4
    return l[0] == l[1] == l[2] == l[3]

class Fruit_game:
    def __init__(self) -> None:
        while True:
            # abcde for 5 kinds of cards
            l = ['a']*4+['b']*4+['c']*4+['d']*4+['e']*4
            random.shuffle(l)
            self.table = l[0:4]
            self.p0 = l[4:8]
            self.p1 = l[8:12]
            self.p2 = l[12:16]
            self.p3 = l[16:20]
            self.ps = [self.p0, self.p1, self.p2, self.p3]
            if is_all_equal(self.p0) or is_all_equal(self.p1) \
                or is_all_equal(self.p2) or is_all_equal(self.p3):
                continue
            else:
                break
        sorted(self.p0)
        sorted(self.p1)
        sorted(self.p2)
        sorted(self.p3)
        
        # it is turn to player 0 first
        self.turn = 0
    
    # functions with prefix 'get_' are only used to get the info of the cards
    # cannot be used to change the cards unless these functions are called by me
    def get_table(self):
        return self.table
    
    def get_p0(self):
        return self.p0
    
    def get_p1(self):
        return self.p1
    
    def get_p2(self):
        return self.p2
    
    def get_p3(self):
        return self.p3
   
    # get cards of all players
    def get_ps(self):
        return self.ps
    
    # get cards of i-th player
    def get_pi(self, i: int):
        assert 0 <= i <= 3
        return self.ps[i]
    
    def get_turn(self):
        return self.turn
        
    def self_assert(self):
        assert self.ps[0] is self.p0
        assert self.ps[1] is self.p1
        assert self.ps[2] is self.p2
        assert self.ps[3] is self.p3
        assert is_all_equal(self.table)
        counta = countb = countc = countd = counte = 0
        for i in self.p0 + self.p1 + self.p2 + self.p3 + self.table:
            if i == 'a':    counta += 1
            if i == 'b':    countb += 1
            if i == 'c':    countc += 1
            if i == 'd':    countd += 1
            if i == 'e':    counte += 1
        assert counta==countb==countc==countd==counte==4
    
    # player i change the card-in-hand m-th with the card-on-table n-th
    # return 0 if change successfully and no other special things happenw
    # or return a number if not (might because of reasons below)
    # 1. after changing, the cards on the table are the same, which is not allowed in the game
    # 2. the player i have won, which means he've had his cards all the same
    # 3. player i won because of this change
    # 4. not the turn for player i
    def change(self, i: int, m: int, n: int):
        if self.turn != i:
            return 4

        pi =  self.get_pi(i)
        table = self.get_table()
        if is_all_equal(pi):
            return 2
        # try to change on new-cards
        new_pi = pi.copy()
        new_table = table.copy()
        new_pi[m], new_table[n] = new_table[n], new_pi[m]
        
        if is_all_equal(new_table):
            return 1
        # change on new-cards
        self.pi[m], self.table[n] = self.table[n], self.pi[m]
        sorted(self.pi)
        sorted(self.table)
        # change turn 
        while True:
            self.turn += 4
            self.turn %= 4
            if is_all_equal(self.get_pi(self.turn)):
                continue
            else:
                break
            
        
        if is_all_equal(new_pi):
            return 3
        return 0
    
    # random change for player i
    def random_change(self, i: int):
        while True:
            l = [0, 1, 2, 3]
            random.shuffle(l)
            m = l[0]
            random.shuffle(l)
            n = l[1]
            ans = self.change(i, m, n)
            if ans == 1:
                continue
            else:
                return ans
        
        
    def print(self):
        def f(s, l):
            assert len(l) == 4
            print(s+'\n'+l[0]+' '+l[1]+' '+l[2]+' '+l[3])
        
        f("table", self.table)
        f("p0", self.p0)
        f("p1", self.p1)
        f("p2", self.p2)
        f("p3", self.p3)

    

class Player_interfere:
    """
        The interfere a player should inheritance
    """
    def __init__(self) -> None:
        pass
    
     
    # the player will know he is the player n-th here
    def set_player_turn(self, n) -> None:
        pass
       
    # the cards of you 
    def set_init_cards(self, l) -> None:
        pass
        
    # the cards on the table 
    def set_init_table(self, l) -> None:
        pass
    
    # if a player want to exit the game then return True
    # when this function is called else return False
    def exit(self) -> bool:
        pass
    
    # the game is finished
    def finish(self) -> None:
        pass
    
    # the player n-th changed the table
    # if you changed the table, then you will not receive this function called
    def event(self, table_before, n:int, table_after) -> None:
        pass
   
    # should return a tuple (m, n)
    # which means change the m-th card of you with the n-th card on the table
    # remember that you should assume that after changing
    # the cards on the table should not the same
    def my_turn(self) -> Tuple[int, int]:
        pass
    
    # the player n-th won
    # warning: other player's winning can also call this function
    # so that we cannot infer that this player won from this function 
    # being called
    def win(self, n:int) -> None:
        pass
    
    
# TODO: 一个服务器开设好几个房间，如果某个房间刚好没人玩，则玩家
# 可以进入该房间

class Fruit_game_server:
    game: Fruit_game | None
    in_playing: bool
    p0: Player_interfere
    p1: Player_interfere
    p2: Player_interfere
    p3: Player_interfere
    
    
    def __init__(self) -> None:
        self.in_playing = False
    
     
    def add_player(self):
        if self.in_playing:
            return False
        else: 
            # TODO
            pass
    
    
    
    async def start(self):
        self.in_playing = True
        turn = self.game.get_turn()
        p0 = self.p0
        p1 = self.p1
        p2 = self.p2
        p3 = self.p3
        ps = [p0, p1, p2, p3]
        have_win = []
        game = self.game
        table = game.get_table
        p0.set_init_cards(game.get_p0())
        p1.set_init_cards(game.get_p1())
        p2.set_init_cards(game.get_p2())
        p3.set_init_cards(game.get_p3())
        for p in ps:
            p.set_init_table(table)
        while True:
            # whether there are some players wanting to exit the game
            for p in ps:
                if p.exit():
                    if p in have_win:
                        pass
                    else:
                        for p2 in ps:
                            p2.finish()
                        return
                    
            
            while True:
                pc = ps[turn]
                # TODO: 如果下面的函数给定时间之内不返回
                # 则令该玩家随机出牌
                m, n = pc.my_turn()
                
                table_before = game.get_table()
                ans = game.change(turn, m, n)
                table_after = game.get_table()
                assert ans != 4
                assert ans != 2
                if ans == 1:
                    continue
                elif ans == 3:
                    p0.win(turn)
                    p1.win(turn)
                    p2.win(turn)
                    p3.win(turn)
                    have_win.append(pc)
                else:
                    assert ans == 0
                for p in ps:
                    if p is pc:
                        continue
                    p.event(table_before, turn, table_after)
                break

    
