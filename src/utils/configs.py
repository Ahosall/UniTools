'''
Configs - Utils
'''

# Imports
import json

from src.utils.colorFunc import colorTreatment
from time import sleep as wait

# Vars
with open('./src/datas/configs.json', encoding='utf-8') as f:
    configs = json.load(f)

# Functions
def getConfigs():
  return configs

def setLanguage(lang):
  configs['language'] = lang
  
  with open('./src/datas/configs.json', 'w+', encoding='utf-8') as f: json.dump(configs, f)

def setNewPathTools(path):
  configs['folders']['tools'] = path
  
  with open('./src/datas/configs.json', 'w+', encoding='utf-8') as f: json.dump(configs, f)

def menu():
  toolsPath = configs['folders']['tools']
  colorLang = []

  if configs['language'] == 'en':
    colorLang = ['_GREEN_', '_WHITE_', '_WHITE_']
  elif configs['language'] == 'es':
    colorLang = ['_WHITE_', '_GREEN_', '_WHITE_']
  elif configs['language'] == 'pt':
    colorLang = ['_WHITE_', '_WHITE_', '_GREEN_']

  items = [
    '{}  ╔═════════════{} SETTINGS                                    {}'.format('_RED_', '_WHITE_', '_RESET_'),    
    '{}  ║                                                            {}'.format('_RED_', '_RESET_'),
    '{}  ╠══════{} Folders                                            {}'.format('_RED_', '_WHITE_', '_RESET_'),
    '{}  ║                                                            {}'.format('_RED_', '_RESET_'),
    '{}  ╠══{}[1]{} Tools ({}"{}"{})                                  {}'.format('_RED_', '_CYAN_', '_WHITE_', '_YELLOW_', toolsPath, '_WHITE_', '_RESET_'),
    '{}  ║                                                            {}'.format('_RED_', '_RESET_'),
    '{}  ╠══════{} Language                                           {}'.format('_RED_', '_WHITE_', '_RESET_'),
    '{}  ║                                                            {}'.format('_RED_', '_RESET_'),

    '{}  ╠══{}[4]{} English                                           {}'.format('_RED_', '_CYAN_', colorLang[0], '_RESET_'),
    '{}  ╠══{}[5]{} Español                                           {}'.format('_RED_', '_CYAN_', colorLang[1], '_RESET_'),
    '{}  ╠══{}[6]{} Português                                         {}'.format('_RED_', '_CYAN_', colorLang[2], '_RESET_'),
    
    '{}  ║                                                            {}'.format('_RED_', '_RESET_'),
    '{}  ╚══{}[0]{} Back                                              {}'.format('_RED_', '_CYAN_', '_WHITE_', '_RESET_'),
    '',
  ]
  
  for item in items:
    print(colorTreatment(item))
    wait(0.01)

  choice = input('  Select an option: ')

  if choice.replace(' ', '') != '':
      if choice in ['0', '00']:
        return 'restart'
      if choice in ['1', '01']:
        print('\n  Set new path to folder "tools"...')
        newPath = input('  : >> ')
        setNewPathTools(newPath)
        print(f'  New path as setted. ({newPath}')
        wait(1)
      elif choice in ['4', '04']:
        print('\n  The language has been changed to English.')
        setLanguage('en')
        wait(1)
      elif choice in ['5', '05']:
        print('\n  El idioma se cambió al Español.')
        setLanguage('es')
        wait(1)
      elif choice in ['6', '06']:
        print('\n  O idioma foi alterado para Português (BRA).')
        setLanguage('pt')
        wait(1)
        return 'restart'
      else:
        items = [
          '\n  A correct option was not selected, setting to Portuguese-Brazilian',
          '\n  Change this language in the settings'
        ]

        for item in items:
          print(item)
        
        setLanguage('pt')
        return 'restart'
  else: return 'error'
