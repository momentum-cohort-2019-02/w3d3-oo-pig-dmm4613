import random

class Game:
    """
    Represents the game of Pig. Contains temporary scores and calls 
    each player to a turn. 
    """
    def __init__(self, player01, player02 = 3):
        self.p1 = player01
        self.p2 = player02
        self.tempScore = 0

    def runGame (self):
        self.tempScore = 0
        self.currentPlayer = None

    def currentTurn(self):
        """

        """
        self.currentPlayer = None

    def temporary_score(self, dice_roll):
        """
        Given the dice roll, keep a running track of the score the current player's turn
        """

        temporary_score = 0
        if dice_roll > 1:
            temporary_score += dice_roll
        else:
            temporary_score = 0
        return temporary_score

class HumanPlayer:
    """
    Represents the human player. Contains total score.
    """
    def __init__(self, score=0):
        """
        Score is added as an input incase you want to provide a handycap at some point
        """
        self.score = score
    
    def roll_or_hold(self):
        """
        Simple input check to see if the human player wants to roll or hold.
        """
        decide_to_roll = input ("Would you like to roll the die or hold? (Enter anything) ")
        if Dice.rollDie() == 1:
            return "Turn over"
        if decide_to_roll != "":
            print ("Hey")
            return True
        else:
            print ("No")
            return False
    
    def adjust_score(self):
        """Given the value of HumanPlayer.score we want to adjust the score"""
        self.score += game.temporary_score        

class ComputerPlayer:
    """
    Represents the computer player. Contains total score.
    """
    def __init__(self, score = 0):
        """
        Score is added as an input incase you want to provide a handycap at some point
        """
        self.score = score

class Dice:
    """
    Represents the tool of the Game. Will hold a random value.
    """
    def __init__(self, sides=6):
        self.sides = sides
        
    def __str__(self):
        return f"You rolled a {self.sides}-sided die and got a "

    def rollDie(self):
        """
        Will roll the dice by selecting a random number from 1-6
        """
        return random.randint(1, self.sides)




if __name__ == "__main__":
    favoriteDie = Dice()
    player01 = HumanPlayer()
    player02 = ComputerPlayer()
    game = Game(player01, player02)
    print (f"{Dice.rollDie(favoriteDie)}")
   
    while player01.roll_or_hold():
        game.temporary_score(favoriteDie.rollDie())
        print (f"{Dice.rollDie(favoriteDie)}")
    player01.adjust_score()
    