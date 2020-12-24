import os
import urllib.request
from pathvalidate import sanitize_filename
from lib.config import __init__

# Variables
result = __init__()


def __create_folders_from_list(folders, base_folder=''):
    """
    This function creates folders described in a list.
    :param folders: Receives a list of folder names
    :param base_folder: Gets formatted folder name
    :return: Nothing
    """
    try:
        base_folder = sanitize_filename(base_folder)

        for folder in folders:
            folder_name = os.path.join(result['path'], base_folder, folder)
            os.makedirs(folder_name, True)
    except AttributeError as error:
        print(f'\033[1;31mERRO! Esta "função" não tem um atributo chamado {error.__context__}\033[m')
    except KeyError as error:
        print(f'\033[1;31mERRO! Chave \"{error.__context__}\" não encontrada.\033[m')


def __download_files_from_list(files, base_folder=''):
    """
    This function downloads files through the links contained in a list.
    :param files: Receives a list of file links
    :param base_folder: Gets formatted folder name
    :return: Nothing
    """
    try:
        base_folder = sanitize_filename(base_folder)

        for file in files:
            link = file['from']
            destination = file['to']
            file_name = link.rsplit('/', 1)[-1]
            full_path_file = os.path.join(result['path'], base_folder, destination, file_name)

            if not os.path.isfile(full_path_file):
                print(f'BAIXANDO.....{link}')
                urllib.request.urlretrieve(link, full_path_file)
    except AttributeError as error:
        print(f'\033[1;31mERRO! Esta "função" não tem um atributo chamado {error.__context__}\033[m')
    except KeyError as error:
        print(f'\033[1;31mERRO! Chave \"{error.__context__}\" não encontrada.\033[m')


def do_actions(action_type, folder_name):
    """
    This function receives the lists and creates both the folders and downloads the files.
    :param action_type: Receives the package type
    :param folder_name: Receives the name of the project that will be created
    :return: Nothing
    """
    try:
        [actions] = [item['actions'] for item in result['config'] if (item['type'] == action_type)]

        __create_folders_from_list(actions['folders'], folder_name)
        __download_files_from_list(actions['files'], folder_name)
    except AttributeError as error:
        print(f'\033[1;31mERRO! Esta "função" não tem um atributo chamado {error.__context__}\033[m')
    except KeyError as error:
        print(f'\033[1;31mERRO! Chave \"{error.__context__}\" não encontrada.\033[m')