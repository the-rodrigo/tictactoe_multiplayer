def choose_simbol():

    symbol = ''
    valid = True
    while valid:
        symbol = input('Choose X or O.\n')
        if symbol == 'O' or symbol == 'o' :
            option = 1
            valid = False
        elif symbol == 'X' or symbol == 'x':
            option = 0
            valid = False
            
    return symbol, option