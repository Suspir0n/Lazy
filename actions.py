import sys
from lib.interface import title, options_number, read_int, options
from lib.config import __init__
from lib.actions import do_actions


def init_app(my_actions):
    while True:
        title('  ESCOLHA UMA OPÇÃO:')
        options_number(my_actions)
        option_selected = read_int('> ')

        title('  NOME DA PASTA:')
        folder_name = str(input('> '))

        title(' CONFIRMA ? (S/N)', f'{"Opção escolhida: "}{my_actions[option_selected-1]}', f'{"Nome da Pasta: "}{folder_name}')
        confirm = options('> ')

        if confirm.upper() == 'S':
            do_actions(my_actions[option_selected-1], folder_name)
            input(': Pressione ENTER para Terminar...')
            break
        if confirm.upper() == 'N':
            option = options(' Deseja escolher outra opção (S/N)?')
            if option == 'N':
                input(': Pressione ENTER para Terminar...')
                break


path = '.' if sys.argv else sys.argv[1]
result = __init__(path)
init_app(result['actions'])