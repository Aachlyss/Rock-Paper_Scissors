import random

def play():
    user = input("'R' for Rock, 'P' for Paper and 'S' for Scissors: ")
    computer = random.choice(['R', 'P', 'S'])
    print(f'Computers\' choice: {computer}')
    if user == computer:
        return 'It\'s s a tie!'
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'
    
def is_win(player, opponent):
    if (player =='R' and opponent =='S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True


print(play())
