def winner(turn, x_values, o_values):

    wins = [
        ['1','2','3'],
        ['1','4','7'],
        ['1','5','9'],
        ['2','5','8'],
        ['3','6','9'],
        ['3','5','7'],
        ['4','5','6'],
        ['7','8','9'],
    ]
    
    if turn == 0:
        for win in wins:
            point = 0
            for k in x_values:
                for x in win:
                    if x == k:
                        point += 1
            if point == 3:
                print('##################### X WON!!! #####################')
                turn = 2
                return turn
    else:
        for win in wins:
            point = 0
            for k in o_values:
                for i in win:
                    if i == k:
                        point += 1
            if point == 3:
                print('##################### O WON!!! #####################')
                turn = 2
                return turn
    
    if turn == 0:
        return turn + 1
    else:
        return turn - 1