def selection(value, options):
    while True:
        if value in options:
            options.remove(value)
            return value, options
        else:
            print('Escolha um valor válido.')
            value = input('Escolha um valor.')