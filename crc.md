Class: HumanPlayer()
Resposibilities:
    -gather input
    -retain personal score
    -receive temporary score
    -continue/end turn if roll a 1(no add) or decide to save(add)
Collaborators: 
    -Game()
    -Dice()

Class: ComputerPlayer()
Responsibilities:
    -retain personal score
    -receive temporary score
    -continue/end turn if temporary score >= 20(add) or if roll a 1(no add)
Collaborators:
    -Game()
    -Dice()

Class: Game()
Responibilities:
    -Compare HumanPlayer() and ComputerPlayer() score
    -Call Dice()
    -retain who's turn it currently is
    -retain temporary score
    -output current temporary score
    -select first player
    -check to see if a 1 was rolled. end turn no add. 
Collaborators:
    -Dice()
    -HumanPlayer()
    -ComputerPlayer()

Class: Dice()
Responsibilities:
    -Get a random number from range 1-6
    -Display the number rolled
Collaborators:
    -HumanPlayer()
    -ComputerPlayer()
    -Game()