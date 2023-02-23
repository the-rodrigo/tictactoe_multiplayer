from func_board import change_board as cb
from func_selection import selection as sl
from func_start import start
from func_winner import winner as wn

x_values, o_values, options, board, turn = start()

while True:

    if turn == 2:
        break

    elif options == []:
        print('It is a draw.')
        break

    else:

        if turn == 0:
            print('It is the X turn.')
            symbol = 'X'
        else:
            print('It is the O turn.')
            symbol = 'O'

        print(f'The disponible options are: {options}')
        value = input('Choose a value.')

        value, options = sl(value, options)

        print(f'The chosen value was {value}.')

        if turn == 0:
            x_values += value
        else:
            o_values += value

        board = cb(value, board, symbol)

        turn = wn(turn, x_values, o_values)

        print(board)
        print()
