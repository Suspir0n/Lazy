def read_int(message):
    """
    This function handles integer erros.
    Does not accept floating numbers.
    Does not accept letters or special characters.
    :param message: receives the message for the input.
    :return: number
    """
    while True:
        try:
            num = int(input(message))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mUsuário preferiu não digitar esse numero.\033[m')
            return 0
        else:
            return num


def options(message):
    """
    This function handles errors on two letter alternatives.
    Accepts only 'N' or 'S'.
    :param message: receives the message for the input.
    :return: string
    """
    while True:
        try:
            option = str(input(message)).upper()
        except KeyboardInterrupt:
            print('\n\033[1;31mUsuário preferiu não digitar esse numero.\033[m')
            option = 'N'
            return option
        else:
            if option in 'NS':
                return option
            else:
                print('\033[1;31mERRO! Digite "N" or "S".).\033[m')


def line(tam=40):
    """
    This function creates lines according to the size I want
    :param tam: Optional variable that receives an integer value
    :return: '=' times the size I say
    """
    return '=' * tam


def title(message, options='', name=''):
    """
    This function creates custom titles according to my usage.
    :param message: Describes the title to be created.
    :param options: (Optional) describes any option you want to place with the title.
    :param name: (Optional) describes any name you want to place with the title.
    :return: An impression with the requested data
    """
    if options == '' and name == '':
        print(f'{line()}\n{message}\n{line()}')
    else:
        print(f'{line()}\n{message}\n{options}\n{name}\n{line()}')


def options_number(my_actions):
    """
    This function creates an initial menu in the terminal interface
    :param my_actions: Receives a list with the data.
    :return: An impression with the requested data
    """
    option_number = 0
    for action in my_actions:
        option_number += 1
        print(f'{option_number} - {action}')


