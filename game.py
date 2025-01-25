import random

class Rps:

    def __init__(self):
        self = self

    # mainscript
    def main(self) -> None:
        playerChose: str = self.playerChoose(self=self)
        aiChose: str = self.aiChoose()

        winner: bool = self.compareValue(self=self, playerChose=playerChose, aiChose=aiChose)
        if None is winner:
            print(f"you tied!")
            exit(0)
        elif winner:
            print(f"you won!")
            exit(0)
        print(f"you lost!")
        exit(0)

    # let the player choose an option
    def playerChoose(self) -> str:
        playerChose: str = input(f"Choose an option (rock, paper, scissor): ")
        if playerChose.isdigit():
            print(f"Invalid input, please try again.")
            self.playerChoose(self=self)
        if playerChose.lower() != 'rock' and 'paper' and 'scissor':
            print(f"Invalid input, please try again.")
            self.playerChoose(self=self)
        return playerChose

    def aiChoose() -> str:

        valueMap: dict = {1: 'rock', 2: 'paper', 3: 'scissor', 4: 'rock', 5: 'paper', 6: 'scissor', 7: 'rock', 8: 'paper', 9: 'scissor'}
        return valueMap.get(random.choice(list(valueMap.keys())))

    def compareValue(self, playerChose: str, aiChose: str) -> bool:  # returns true if player win, else returns false
        playerChose = playerChose.lower()
        if playerChose.lower() == aiChose.lower() or aiChose.lower() == playerChose.lower():
            return None
        elif aiChose == 'rock' and playerChose.lower() == 'paper':
            return True
        elif aiChose == 'rock' and playerChose.lower() == 'scissor':
            return False
        elif aiChose == 'paper' and playerChose.lower() == 'scissor':
            return True
        elif aiChose == 'paper' and playerChose.lower() == 'rock':
            return False
        elif aiChose == 'scissor' and playerChose.lower() == 'rock':
            return True
        elif aiChose == 'scissor' and playerChose.lower() == 'paper':
            return False
        exit(1)

class number_sim:
    # to be finished
    ...