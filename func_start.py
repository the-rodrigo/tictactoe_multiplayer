from random import randint

def start():

    x_values = []
    o_values = []
    options = ['1','2','3','4','5','6','7','8','9']
    board = '     |     |     \n  1  |  2  |  3  \n_____|_____|_____\n     |     |     \n  4  |  5  |  6  \n_____|_____|_____\n     |     |     \n  7  |  8  |  9  \n     |     |     '
    turn = randint(0,1)

    return x_values, o_values, options, board, turn