from war import Player, Deck

class Game():
    def __init__(self):
        name1 = input("p1 name: ")
        name2 = input("p2 name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)
        
    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} | {} drew {}."
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)
    
    def winner(self, p1, p2):
        if p1.win > p2.win:
            return p1.name
        if p2.win > p1.win:
            return p2.name
        else:
            return "It is a tie!"            
    
    def play_game(self):
        cards = self.deck.cards
        print("Beginning War!")
        while len(cards) >= 2:
            m = "q to Quit. " + "Any key to play: "
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_cards()
            p2c = self.deck.rm_cards()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.win += 1
                self.wins(self.p1.name)
            else:
                self.p2.win += 1
                self.wins(self.p2.name)
            win = self.winner(self.p1, self.p2)
            print("War is over. {} wins!". format(win))


play = Game()
play.play_game()

