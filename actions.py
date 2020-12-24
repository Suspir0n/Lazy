import os
import sys
import json
import urllib.request
from pathvalidate import sanitize_filename
import configparser
from time import sleep


class Actions:
      
  def __init__(self, path=''):
        path_config_file = self.__getIniPath('config.ini')
        config = configparser.ConfigParser()
        config.read(path_config_file)
        config_link = config['DEFAULT']['config_link']
        
        self.path = path
        self.config = self.__loadConfig(config_link)
        self.actions = self.__loadActions(self.config)
        
  
  def __loadConfig(self, link):
        with urllib.request.urlopen(link) as url:
          data = json.loads(url.read().decode())
        return data
      
      
  def __loadActions(self, config):
        return [item['type'] for item in config]
        
        
  def __getIniPath(self, filename):
        return filename if os.path.isfile(filename) else os.path.join(os.path.dirname(sys.executable), filename)


  def __createFoldersFromList(self, folders, baseFolder=''):
      baseFolder = sanitize_filename(baseFolder)
      
      for folder in folders:
          folderName = os.path.join(self.path, baseFolder, folder)
          os.makedirs(folderName, True)
     
      
  def __downloadFilesFromList(self, files, baseFolder=''):
      baseFolder = sanitize_filename(baseFolder)
      
      for file in files:
          link = file['from']
          destination = file['to']
          fileName = link.rsplit('/', 1)[-1]
          fullPathFile = os.path.join(self.path, baseFolder, destination, fileName)
          
          if not os.path.isfile(fullPathFile):
              print(f'BAIXANDO.....{link}')
              urllib.request.urlretrieve(link, fullPathFile)
              
  
  def doActions(self, actionType, folderName):
        [actions] = [item['actions'] for item in self.config if (item['type'] == actionType)]
        
        self.__createFoldersFromList(actions['folders'], folderName)
        self.__downloadFilesFromList(actions['files'], folderName)
        

def initApp(myActions):
  # INTERFACE VIA TERMINAL
  print('=' * 40)
  print(f'{"  ESCOLHA UMA OPÇÃO:"}')
  print('=' * 40)
  
  optionNumber = 0
  for action in myActions.actions:
    optionNumber += 1
    print(f'{optionNumber} - {action}')
  
  optionSelected = int(input('> '))
  
  print('=' * 40)
  print(f'{"  NOME DA PASTA:"}')
  print('=' * 40)
  folderName = input('> ')
  
  print('=' * 40)
  print(' CONFIRMA ? (S/N)')
  print(f'{"Opção escolhida: "}{myActions.actions[optionSelected-1]}')
  print(f'{"Nome da Pasta: "}{folderName}')
  print('=' * 40)
  confirm = str(input('> '))
  
  if confirm.upper() == 'S':
        myActions.doActions(myActions.actions[optionSelected-1], folderName)
        
  input(': Pressione ENTER para Terminar...')
  sleep(60)


path = '.' if sys.argv else  sys.argv[1]
actions = Actions(path)
initApp(actions)

  