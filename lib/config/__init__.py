import os
import sys
import configparser
import json
import urllib.request


def __init__(path=''):
    """
    Main function
    This function takes all necessary data and initializes the other functions.
    :param path: (Optional) Receives the package path
    :return: Three values within a dictionary (actions, path, config)
    """
    try:
        path_config_file = __get_ini_path('config.ini')
        config_parser = configparser.ConfigParser()
        config_parser.read(path_config_file)
        config_link = config_parser['DEFAULT']['config_link']
        _path = path
        config = __load_config(config_link)
        actions = __load_actions(config)
    except AttributeError as error:
        print(f'\033[1;31mERRO! Esta "função" não tem um atributo chamado {error.__context__}\033[m')
    except KeyError as error:
        print(f'\033[1;31mERRO! Chave \"{error.__context__}\" não encontrada.\033[m')
    else:
        return {'actions': actions, 'path': _path, 'config': config}


def __load_config(link):
    """
    This function reads the config.ini file to be able to receive the lists that were declared in a .json
    :param link: Receives a link to where the .json file is
    :return: The lists in the .json file
    """
    try:
        with urllib.request.urlopen(link) as url:
            data = json.loads(url.read().decode())
    except AttributeError as error:
        print(f'\033[1;31mERRO! Esta "função" não tem um atributo chamado {error.__context__}\033[m')
    except KeyError as error:
        print(f'\033[1;31mERRO! Chave \"{error.__context__}\" não encontrada.\033[m')
    else:
        return data


def __load_actions(_config):
    """
    This function read the data that was brought from the link where the .json file contained
    :param _config: Receive a json
    :return: The data read
    """
    try:
        result = [item['type'] for item in _config]
    except AttributeError as error:
        print(f'\033[1;31mERRO! Esta "função" não tem um atributo chamado {error.__context__}\033[m')
    except KeyError as error:
        print(f'\033[1;31mERRO! Chave \"{error.__context__}\" não encontrada.\033[m')
    else:
        return result


def __get_ini_path(filename):
    """
    This function finds the config.ini file to be able to run the program
    :param filename: Receives the folder name
    :return: The path
    """
    try:
        result = filename if os.path.isfile(filename) else os.path.join(os.path.dirname(sys.executable), filename)
    except AttributeError as error:
        print(f'\033[1;31mERRO! Esta "função" não tem um atributo chamado {error.__context__}\033[m')
    except KeyError as error:
        print(f'\033[1;31mERRO! Chave \"{error.__context__}\" não encontrada.\033[m')
    else:
        return result




