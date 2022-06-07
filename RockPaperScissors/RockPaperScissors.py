import random


def play():
    user = input(
        "What is you choice?\n'r' for rock, 'p' for paper, 's' for scissors: ").lower
    computer = random.choice(['r', 'p', 's'])

    if (user == computer):
        return "It's a TIE!!! :|"

    if(is_win(user, computer)):
        return 'You WON!! :)'

    return "You LOST!! :("


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
