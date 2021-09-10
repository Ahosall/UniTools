'''
Language - Functions
'''

# Imports
import json

from src.utils.configs import getConfigs

# Vars
with open('./src/datas/languages.json', encoding='utf-8') as f:
    languages = json.load(f)

# Functions
def lang(): 
  lang = getConfigs()['language']
  return languages[lang]
